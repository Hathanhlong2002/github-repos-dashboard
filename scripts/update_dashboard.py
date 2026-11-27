#!/usr/bin/env python3
"""
Generate GitHub repos dashboard for the current repository owner.
Produces README.md, data/dashboard.json (zero-rate-limit web snapshot),
and updates the user's profile README (username/username) when PAT is set.
"""
import base64
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from urllib.parse import quote

import requests

OWNER = os.getenv("GITHUB_REPOSITORY_OWNER") or os.getenv("GITHUB_ACTOR") or "unknown"
PERSONAL_TOKEN = os.getenv("PERSONAL_ACCESS_TOKEN")
# Prefer personal token so we can read private repos and write to the profile repo
TOKEN = PERSONAL_TOKEN or os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY", f"{OWNER}/github-repos-dashboard").split("/")[-1]
REQUEST_TIMEOUT = 15

HEADERS = {"Accept": "application/vnd.github+json"}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"

CATEGORY_LABELS = {
    "Unity / Game": "🎮 Unity / Game",
    "AI / ML": "🤖 AI / ML",
    "Bot / Mini App": "💬 Bot / Mini App",
    "Web / Frontend": "🌐 Web / Frontend",
    "Other": "📁 Other",
}

# Priority 1: Explicit repository topics
TOPIC_MAP = {
    "unity": "Unity / Game",
    "unity3d": "Unity / Game",
    "game": "Unity / Game",
    "gamedev": "Unity / Game",
    "shader": "Unity / Game",
    "webgl": "Unity / Game",
    "threejs": "Unity / Game",
    "ai": "AI / ML",
    "ml": "AI / ML",
    "machine-learning": "AI / ML",
    "deep-learning": "AI / ML",
    "llm": "AI / ML",
    "gpt": "AI / ML",
    "openai": "AI / ML",
    "bedrock": "AI / ML",
    "nlp": "AI / ML",
    "computer-vision": "AI / ML",
    "data-science": "AI / ML",
    "bot": "Bot / Mini App",
    "zalo": "Bot / Mini App",
    "miniapp": "Bot / Mini App",
    "mini-app": "Bot / Mini App",
    "telegram": "Bot / Mini App",
    "discord": "Bot / Mini App",
    "react": "Web / Frontend",
    "nextjs": "Web / Frontend",
    "vue": "Web / Frontend",
    "svelte": "Web / Frontend",
    "angular": "Web / Frontend",
    "frontend": "Web / Frontend",
    "web": "Web / Frontend",
    "html": "Web / Frontend",
    "css": "Web / Frontend",
}

# Priority 2: Domain keywords on name + description (evaluated BEFORE language fallback)
# Keep identical with index.html so README and Web Dashboard never disagree.
KEYWORD_RULES = [
    (
        "Unity / Game",
        {
            "unity", "unity3d", "game", "gamedev", "shader", "shaderlab",
            "webgl", "threejs", "fps", "dungeon", "survivor", "zombie",
            "platformer", "metroidvania", "urp", "photon",
        },
        ("unity", "shader", "three js", "game", "platformer", "metroidvania", "farming"),
    ),
    (
        "AI / ML",
        {
            "ai", "ml", "llm", "gpt", "openai", "bedrock", "gemini",
            "onnx", "gnn", "opencv", "chatbot", "rag", "agent", "agents", "whisper",
        },
        ("machine learning", "deep learning", "data science", "voice agent", "neural", "bedrock", "openai", "chatbot"),
    ),
    (
        "Bot / Mini App",
        {"zalo", "bot", "miniapp", "telegram", "discord"},
        ("mini app", "miniapp", "zalo"),
    ),
    (
        "Web / Frontend",
        {"react", "nextjs", "vue", "svelte", "angular", "frontend", "html", "css", "tailwind", "dashboard"},
        ("next js", "frontend", "tailwind"),
    ),
]

# Priority 3: Primary language fallback
LANGUAGE_MAP = {
    "c#": "Unity / Game",
    "shaderlab": "Unity / Game",
    "hlsl": "Unity / Game",
    "glsl": "Unity / Game",
    "gdscript": "Unity / Game",
    "python": "AI / ML",
    "jupyter notebook": "AI / ML",
    "html": "Web / Frontend",
    "css": "Web / Frontend",
    "scss": "Web / Frontend",
    "javascript": "Web / Frontend",
    "typescript": "Web / Frontend",
    "vue": "Web / Frontend",
    "svelte": "Web / Frontend",
}

# Dynamic badge metadata for profile README toolchain section
LANGUAGE_BADGE_META = {
    "c#": ("239120", "csharp", "white"),
    "python": ("3776AB", "python", "white"),
    "typescript": ("3178C6", "typescript", "white"),
    "javascript": ("F7DF1E", "javascript", "black"),
    "html": ("E34F26", "html5", "white"),
    "css": ("1572B6", "css3", "white"),
    "scss": ("CC6699", "sass", "white"),
    "shaderlab": ("222C37", "unity", "white"),
    "jupyter notebook": ("F37626", "jupyter", "white"),
    "go": ("00ADD8", "go", "white"),
    "rust": ("000000", "rust", "white"),
    "java": ("ED8B00", "openjdk", "white"),
    "c++": ("00599C", "cplusplus", "white"),
    "c": ("A8B9CC", "c", "black"),
    "php": ("777BB4", "php", "white"),
    "ruby": ("CC342D", "ruby", "white"),
    "swift": ("F05138", "swift", "white"),
    "kotlin": ("7F52FF", "kotlin", "white"),
    "dart": ("0175C2", "dart", "white"),
    "shell": ("121011", "gnubash", "white"),
    "dockerfile": ("2496ED", "docker", "white"),
    "vue": ("4FC08D", "vuedotjs", "black"),
    "svelte": ("FF3E00", "svelte", "white"),
    "mathematica": ("DD1100", "wolframmathematica", "white"),
}


def _clean_description(desc) -> str:
    cleaned = " ".join((desc or "").split())
    return cleaned or "-"


def sanitize_private_repo(repo: dict) -> dict:
    """Keep ONLY name and description (tác dụng) for private repositories."""
    return {
        "name": (repo.get("name") or "-").strip() or "-",
        "description": _clean_description(repo.get("description")),
    }


def sanitize_public_repo(repo: dict) -> dict:
    """Keep public fields required by the web dashboard snapshot."""
    return {
        "name": repo.get("name") or "-",
        "html_url": repo.get("html_url") or "",
        "description": _clean_description(repo.get("description")),
        "language": repo.get("language"),
        "topics": list(repo.get("topics") or []),
        "updated_at": repo.get("updated_at") or "",
        "stargazers_count": repo.get("stargazers_count", 0),
        "forks_count": repo.get("forks_count", 0),
        "open_issues_count": repo.get("open_issues_count", 0),
        "private": False,
        "category": categorize_key(repo),
    }


def sanitize_profile(profile: dict | None, username: str, public_count: int) -> dict:
    data = profile or {}
    return {
        "login": data.get("login") or username,
        "name": data.get("name"),
        "avatar_url": data.get("avatar_url") or "",
        "bio": data.get("bio"),
        "created_at": data.get("created_at"),
        "public_repos": data.get("public_repos", public_count),
        "followers": data.get("followers", 0),
        "following": data.get("following", 0),
        "company": data.get("company"),
        "location": data.get("location"),
        "blog": data.get("blog") or "",
        "twitter_username": data.get("twitter_username"),
        "html_url": data.get("html_url") or f"https://github.com/{username}",
    }


def split_repos(repos):
    public_repos = [r for r in repos if not r.get("private")]
    private_repos = sorted(
        (sanitize_private_repo(r) for r in repos if r.get("private")),
        key=lambda r: r["name"].lower(),
    )
    return public_repos, private_repos


def _get_authenticated_login():
    if not PERSONAL_TOKEN:
        return None
    resp = requests.get("https://api.github.com/user", headers=HEADERS, timeout=REQUEST_TIMEOUT)
    if resp.status_code == 200:
        return (resp.json().get("login") or "").strip()
    print(f"Authenticated user check failed ({resp.status_code}), falling back to public repos")
    return None


def get_profile(username: str):
    resp = requests.get(
        f"https://api.github.com/users/{username}",
        headers=HEADERS,
        timeout=REQUEST_TIMEOUT,
    )
    if resp.status_code == 200:
        return resp.json()
    print(f"Error fetching profile for {username}: {resp.status_code}")
    return None


def _fetch_repo_pages(url: str, base_params: dict, owner_filter: str | None = None):
    repos = []
    for page in range(1, 11):
        params = {**base_params, "page": page}
        resp = requests.get(url, headers=HEADERS, params=params, timeout=REQUEST_TIMEOUT)
        if resp.status_code != 200:
            print(f"Error fetching repos from {url}: {resp.status_code}")
            return None if page == 1 else repos
        data = resp.json()
        if not data:
            break
        raw_count = len(data)
        if owner_filter:
            data = [
                r for r in data
                if (r.get("owner", {}).get("login") or "").lower() == owner_filter
            ]
        repos.extend(data)
        if raw_count < base_params.get("per_page", 100):
            break
    return repos


def get_repos(username: str):
    auth_login = _get_authenticated_login()
    if auth_login and auth_login.lower() == username.lower():
        repos = _fetch_repo_pages(
            "https://api.github.com/user/repos",
            {"per_page": 100, "sort": "updated", "affiliation": "owner"},
            owner_filter=username.lower(),
        )
        if repos is not None:
            return repos
        print("Falling back to /users/{username}/repos")

    repos = _fetch_repo_pages(
        f"https://api.github.com/users/{username}/repos",
        {"per_page": 100, "sort": "updated", "type": "owner"},
    )
    return repos or []


def categorize_key(repo: dict) -> str:
    topics = [t.lower() for t in (repo.get("topics") or [])]
    for topic in topics:
        if topic in TOPIC_MAP:
            return TOPIC_MAP[topic]

    raw_text = f"{repo.get('name') or ''} {repo.get('description') or ''}"
    normalized = re.sub(r"[^a-z0-9]+", " ", raw_text.lower()).strip()
    tokens = set(normalized.split()) if normalized else set()

    for category, rule_tokens, rule_phrases in KEYWORD_RULES:
        if tokens & rule_tokens:
            return category
        if any(phrase in normalized for phrase in rule_phrases):
            return category

    lang = (repo.get("language") or "").lower()
    if lang in LANGUAGE_MAP:
        return LANGUAGE_MAP[lang]

    return "Other"


def categorize(repo: dict) -> str:
    return CATEGORY_LABELS[categorize_key(repo)]


def build_language_badge(lang: str) -> str:
    shields_label = quote(lang.replace("-", "--").replace("_", "__"), safe="")
    meta = LANGUAGE_BADGE_META.get(lang.lower())
    if meta:
        color, logo, logo_color = meta
        return f"![{lang}](https://img.shields.io/badge/{shields_label}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color})"
    return f"![{lang}](https://img.shields.io/badge/{shields_label}-4B5563?style=for-the-badge)"


def build_toolchain_badges(public_repos, limit: int = 8) -> list[str]:
    counts = Counter(r.get("language") for r in public_repos if r.get("language"))
    if not counts:
        return ["_No languages detected yet._"]
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0].lower()))[:limit]
    return [build_language_badge(lang) for lang, _ in ranked]


def generate_profile_readme(repos):
    now_dt = datetime.now(timezone.utc)
    now = now_dt.strftime("%Y-%m-%d")
    public_repos, private_repos = split_repos(repos)
    total = len(public_repos) + len(private_repos)
    cache_bust = now_dt.strftime("%Y%m%d%H%M")

    header_text = quote(OWNER)
    header_desc = quote("Developer · Open Source · Building cool things")
    header = f"![Header](https://capsule-render.vercel.app/api?type=waving&height=220&color=gradient&customColorList=6,12,20,24&text={header_text}&fontColor=ffffff&fontSize=40&fontAlignY=35&desc={header_desc}&descAlignY=55&animation=fadeIn)"

    typing = "[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=800&color=70A5FD&center=true&vCenter=true&repeat=true&width=750&lines=Building+projects+and+exploring+new+tech;Managing+repositories+with+this+dashboard;Open+to+collaboration)](https://git.io/typing-svg)"

    dashboard_url = f"https://{OWNER}.github.io/{REPO_NAME}/"
    source_url = f"https://github.com/{OWNER}/{REPO_NAME}"
    workflow_url = f"https://github.com/{OWNER}/{REPO_NAME}/actions/workflows/update-dashboard.yml"
    profile_views = f"https://komarev.com/ghpvc/?username={OWNER}&style=for-the-badge&color=7c3aed&label=PROFILE+VIEWS"

    snake_dark = f"https://raw.githubusercontent.com/{OWNER}/{OWNER}/output/github-contribution-grid-snake-dark.svg"

    stats_url = f"https://github-readme-stats.vercel.app/api?username={OWNER}&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&cache_bust={cache_bust}"
    langs_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username={OWNER}&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&cache_bust={cache_bust}"
    trophies_url = f"https://github-profile-trophy.vercel.app/?username={OWNER}&theme=tokyonight&no-frame=true&no-bg=true&margin-w=4&cache_bust={cache_bust}"

    toolchain_badges = build_toolchain_badges(public_repos)

    lines = [
        "<div align=\"center\">",
        "",
        header,
        "",
        typing,
        "",
        f"<a href=\"https://github.com/{OWNER}\"><img src=\"https://img.shields.io/badge/GitHub-{OWNER}-181717?style=for-the-badge&logo=github&logoColor=white\"></a>",
        f"<a href=\"{dashboard_url}\"><img src=\"https://img.shields.io/badge/📊_View_Dashboard-blue?style=for-the-badge\"></a>",
        f"<img src=\"{profile_views}\">",
        "",
        "```text",
        f"📍 GitHub User: {OWNER}",
        "```",
        "",
        "</div>",
        "",
        "## `> whoami`",
        "",
        f"This profile is auto-generated by the [Repos Dashboard]({source_url}). It shows an overview of repositories, categories, and activity.",
        "",
        "```mermaid",
        "flowchart LR",
        "    REPOS[\"Your Repositories\"] --> DASH[\"Repos Dashboard\"]",
        "    DASH --> PROFILE[\"This Profile\"]",
        "```",
        "",
        "## `> toolchain`",
        "",
        "<div align=\"center\">",
        "",
        "### Languages & Tools",
        "",
        *toolchain_badges,
        "",
        "</div>",
        "",
        "## `> github stats`",
        "",
        "<div align=\"center\">",
        "",
        f"![GitHub Stats]({stats_url})",
        "",
        f"![Top Languages]({langs_url})",
        "",
        "</div>",
        "",
        "## `> trophies`",
        "",
        "<div align=\"center\">",
        "",
        f"![Trophies]({trophies_url})",
        "",
        "</div>",
        "",
        "## `> stats`",
        "",
        f"**Total repositories**: {total} ({len(public_repos)} public / {len(private_repos)} private)  ",
        f"**Last updated**: {now}",
        "",
        "### Categories",
        ""
    ]

    groups = defaultdict(int)
    for r in public_repos:
        groups[categorize(r)] += 1
    for cat, count in sorted(groups.items(), key=lambda x: -x[1]):
        lines.append(f"- {cat}: **{count}**")

    if private_repos:
        lines.extend([
            "",
            f"## `> private repos` ({len(private_repos)})",
            "",
            "| Repo | Tác dụng |",
            "|------|----------|"
        ])
        for r in private_repos:
            name = r["name"].replace("|", "/")
            desc = r["description"][:200].replace("|", "/")
            lines.append(f"| **{name}** | {desc} |")

    lines.extend([
        "",
        "## `> recent repos`",
        "",
        "| Repo | Language | Updated | Stars | Category |",
        "|------|----------|---------|-------|----------|"
    ])
    recent = sorted(public_repos, key=lambda x: x.get("updated_at") or "", reverse=True)[:12]
    for r in recent:
        name = r["name"]
        lang = r.get("language") or "-"
        updated = (r.get("updated_at") or "")[:10]
        stars = r.get("stargazers_count", 0)
        cat = categorize(r)
        url = r["html_url"]
        lines.append(f"| [{name}]({url}) | {lang} | {updated} | {stars} | {cat} |")

    lines.extend([
        "",
        "## `> contribution snake`",
        "",
        "<div align=\"center\">",
        "",
        "<picture>",
        f"  <source media=\"(prefers-color-scheme: dark)\" srcset=\"{snake_dark}\">",
        f"  <img alt=\"Contribution snake\" src=\"{snake_dark}\">",
        "</picture>",
        "",
        "</div>",
        "",
        "<div align=\"center\">",
        "",
        f"[![Update Profile](https://img.shields.io/badge/🔄_Update_Profile-success?style=for-the-badge)]({workflow_url})",
        f"[![Manage Dashboard](https://img.shields.io/badge/🔧_Manage_Dashboard-green?style=for-the-badge)]({source_url})",
        "",
        "![Footer](https://capsule-render.vercel.app/api?type=waving&height=100&section=footer&color=gradient&customColorList=6,12,20,24&animation=fadeIn)",
        "",
        "</div>"
    ])
    return "\n".join(lines)


def update_profile_readme(content: str):
    if not PERSONAL_TOKEN:
        print("No PERSONAL_ACCESS_TOKEN set, skip profile update")
        return
    url = f"https://api.github.com/repos/{OWNER}/{OWNER}/contents/README.md"
    resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    sha = None
    if resp.status_code == 200:
        sha = resp.json().get("sha")

    payload = {
        "message": "chore: auto-update dynamic profile",
        "content": base64.b64encode(content.encode()).decode(),
        "branch": "main"
    }
    if sha:
        payload["sha"] = sha

    put = requests.put(url, headers=HEADERS, json=payload, timeout=REQUEST_TIMEOUT)
    if put.status_code in (200, 201):
        print("Profile README updated successfully")
    else:
        print(f"Profile update failed: {put.status_code} - {put.text[:300]}")


def write_dashboard_json(profile, public_repos, private_repos, output_path: str = "data/dashboard.json"):
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    payload = {
        "schema_version": 1,
        "owner": OWNER,
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "profile": sanitize_profile(profile, OWNER, len(public_repos)),
        "public_repos": [sanitize_public_repo(r) for r in public_repos],
        "private_repos": [sanitize_private_repo(r) for r in private_repos],
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")


def generate_readme(repos):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    public_repos, private_repos = split_repos(repos)
    private = len(private_repos)
    public = len(public_repos)
    total = private + public

    workflow_url = f"https://github.com/{OWNER}/{REPO_NAME}/actions/workflows/update-dashboard.yml"
    token_url = "https://github.com/settings/tokens/new?scopes=repo&description=github-repos-dashboard"
    secrets_url = f"https://github.com/{OWNER}/{REPO_NAME}/settings/secrets/actions"
    pages_settings_url = f"https://github.com/{OWNER}/{REPO_NAME}/settings/pages"
    pages_url = f"https://{OWNER}.github.io/{REPO_NAME}/"
    profile_repo_url = f"https://github.com/new?name={OWNER}&description=Profile+README"
    profile_view_url = f"https://github.com/{OWNER}/{OWNER}"
    profile_actions_url = f"https://github.com/{OWNER}/{OWNER}/actions"
    actions_url = f"https://github.com/{OWNER}/{REPO_NAME}/actions"

    lines = [
        f"# 📊 GitHub Repos Dashboard - {OWNER}",
        "",
        "## 🚀 Detailed Setup Guide",
        "",
        "> **Note for forked users**: After forking, run the workflow on your fork so all links and content update to your username.",
        "",
        "### 1. Enable the workflow (required on forks)",
        "",
        f"[![Open Actions](https://img.shields.io/badge/Open_Actions-blue?style=for-the-badge)]({actions_url})",
        "",
        "1. Click **Update Repos Dashboard** in the left sidebar",
        "2. Click **Enable workflow** (if it shows as Disabled)",
        "",
        "### 2. Create your profile repository",
        "",
        f"[![Create Profile Repo](https://img.shields.io/badge/Create_Profile_Repo-purple?style=for-the-badge)]({profile_repo_url})",
        "",
        f"- Name must be exactly: **`{OWNER}`**",
        "- Visibility: **Public**",
        "",
        "### 3. Create a Personal Access Token",
        "",
        f"[![Get Token](https://img.shields.io/badge/Get_Token-orange?style=for-the-badge)]({token_url})",
        "",
        "- Select **Generate new token (classic)**",
        "- Check the **`repo`** scope",
        "- Copy the token immediately",
        "",
        "### 4. Add the token as a secret",
        "",
        f"[![Add Secret](https://img.shields.io/badge/Add_Secret-yellow?style=for-the-badge)]({secrets_url})",
        "",
        "- Name: `PERSONAL_ACCESS_TOKEN`",
        "- Paste your token as the value",
        "",
        "### 5. Enable GitHub Pages",
        "",
        f"[![Open Pages Settings](https://img.shields.io/badge/Open_Pages_Settings-blue?style=for-the-badge)]({pages_settings_url})",
        "",
        "1. Under **Build and deployment**, select Source: **GitHub Actions**",
        "2. The `Deploy to GitHub Pages` workflow packages only `index.html` and `data/dashboard.json` into `_site/` (never exposing `scripts/` or `README.md`)",
        "",
        f"Dashboard will be available at: [{pages_url}]({pages_url})",
        "",
        "### 6. (Optional) Add Contribution Snake",
        "",
        "To show the animated contribution snake on your profile:",
        "",
        f"1. Go to your profile repo: [https://github.com/{OWNER}/{OWNER}](https://github.com/{OWNER}/{OWNER})",
        "2. Create file `.github/workflows/snake.yml` with this content:",
        "",
        "```yaml",
        "name: Generate Snake",
        "on:",
        "  schedule:",
        "    - cron: \"0 0 * * *\"",
        "  workflow_dispatch:",
        "jobs:",
        "  generate:",
        "    runs-on: ubuntu-latest",
        "    steps:",
        "      - uses: Platane/snk@v3",
        "        with:",
        f"          github_user_name: {OWNER}",
        "          outputs: |",
        "            dist/github-contribution-grid-snake.svg",
        "            dist/github-contribution-grid-snake-dark.svg?palette=github-dark",
        "      - uses: crazy-max/ghaction-github-pages@v4",
        "        with:",
        "          target_branch: output",
        "          build_dir: dist",
        "        env:",
        "          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}",
        "```",
        "",
        f"3. Go to [Actions]({profile_actions_url}) → run **Generate Snake**",
        "",
        "### 7. Run the dashboard workflow",
        "",
        f"[![Run Workflow](https://img.shields.io/badge/Run_Workflow-success?style=for-the-badge)]({workflow_url})",
        "",
        "This updates `README.md`, `data/dashboard.json`, and your profile README.",
        "",
        "### 8. View your profile",
        "",
        f"[![View Profile](https://img.shields.io/badge/View_Profile-blue?style=for-the-badge)]({profile_view_url})",
        "",
        "---",
        "",
        f"**Web Dashboard**: [{pages_url}]({pages_url})",
        "",
        f"**Updated**: {now}  ",
        f"**Total**: {total} repos ({private} private / {public} public)",
        "",
        "---",
        ""
    ]

    if private_repos:
        lines.append(f"## 🔒 Private Repos ({len(private_repos)})")
        lines.append("")
        lines.append("| Repo | Tác dụng |")
        lines.append("|------|----------|")
        for r in private_repos:
            name = r["name"].replace("|", "/")
            desc = r["description"][:200].replace("|", "/")
            lines.append(f"| **{name}** | {desc} |")
        lines.append("")

    groups = defaultdict(list)
    for r in public_repos:
        groups[categorize(r)].append(r)

    for cat in sorted(groups.keys()):
        lines.append(f"## {cat} ({len(groups[cat])})")
        lines.append("")
        lines.append("| Repo | Language | Updated | Stars | Visibility | Description |")
        lines.append("|------|----------|---------|-------|------------|-------------|")
        for r in sorted(groups[cat], key=lambda x: x.get("updated_at") or "", reverse=True)[:30]:
            name = r["name"]
            lang = r.get("language") or "-"
            updated = (r.get("updated_at") or "")[:10]
            stars = r.get("stargazers_count", 0)
            vis = "🌐"
            desc = _clean_description(r.get("description"))[:60].replace("|", "/")
            url = r["html_url"]
            lines.append(f"| [{name}]({url}) | {lang} | {updated} | {stars} | {vis} | {desc} |")
        lines.append("")

    lines.extend([
        "---",
        "",
        "*Generated automatically. Run the workflow to refresh.*"
    ])
    return "\n".join(lines)


if __name__ == "__main__":
    print(f"Generating dashboard for: {OWNER}")
    print(f"Using personal token: {bool(PERSONAL_TOKEN)}")
    profile = get_profile(OWNER)
    repos = get_repos(OWNER)
    public_repos, private_repos = split_repos(repos)
    print(f"Found {len(repos)} repositories ({len(public_repos)} public, {len(private_repos)} private)")

    readme = generate_readme(repos)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)
    print("README.md updated")

    write_dashboard_json(profile, public_repos, private_repos)
    print("data/dashboard.json updated")

    profile_content = generate_profile_readme(repos)
    update_profile_readme(profile_content)
