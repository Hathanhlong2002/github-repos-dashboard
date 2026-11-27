# 📊 GitHub Repos Dashboard — Long

Automated GitHub repository catalog, zero-rate-limit static Web Dashboard (`data/dashboard.json`), minimal private-repo listing (name + purpose only), and adaptive light/dark Profile README sync.

[![Open Web Dashboard](https://img.shields.io/badge/Open_Web_Dashboard-2563EB?style=for-the-badge&logo=githubpages&logoColor=white)](https://hathanhlong2002.github.io/github-repos-dashboard/) [![View Profile](https://img.shields.io/badge/Profile_Hathanhlong2002-1E293B?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hathanhlong2002/Hathanhlong2002) [![Use For Your Profile](https://img.shields.io/badge/Use_For_Your_Profile-16A34A?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/Hathanhlong2002/github-repos-dashboard/fork)

**Web Dashboard**: [https://hathanhlong2002.github.io/github-repos-dashboard/](https://hathanhlong2002.github.io/github-repos-dashboard/)  
**Updated**: `2026-11-27 10:25 UTC`  
**Total**: **38 repos** (`27` public · `11` private)

> **Using this for your own GitHub Profile?**
> 1. [Fork this repo](https://github.com/Hathanhlong2002/github-repos-dashboard/fork)
> 2. On **your copy's top bar**, open **Actions** → enable workflows *(already enabled if created from template)*
> 3. *(To sync your GitHub Profile & private repos)* Create public repo `<your-username>/<your-username>`, create a Classic PAT (`repo` scope), and save it in **your repo's Settings → Secrets and variables → Actions** as `PERSONAL_ACCESS_TOKEN`
> 4. On **your repo's top bar**, open **Actions → Update Repos Dashboard → Run workflow** (automatically updates your `README.md`, `data/dashboard.json`, and `<your-username>/<your-username>/README.md`)

## ✨ Features

- **Unified Categorization**: `scripts/update_dashboard.py` and `index.html` share identical priority rules (`topics → keyword tokens → language → Other`), keeping `README.md` and Web UI 100% consistent.
- **Zero Rate-Limit Snapshot**: GitHub Actions publishes `data/dashboard.json` alongside `README.md` so visitors load the dashboard without hitting GitHub's 60 req/hr unauthenticated limit.
- **Privacy-Safe Private Repos**: When `PERSONAL_ACCESS_TOKEN` is configured, private repos are fetched via `/user/repos?affiliation=owner` and stripped down to **name and purpose only** — no links, languages, stars, or timestamps.
- **Hardened Web UI & Scoped Pages Deploy**: `index.html` renders strictly with safe DOM APIs (zero `innerHTML` / inline handlers) and `pages.yml` deploys only `_site/` (`index.html` + `data/dashboard.json`).
- **Adaptive Profile README**: Automatically syncs `{owner}/{owner}/README.md` (auto-detecting `main`/`master` default branch) with light/dark `<picture>` cards, dynamic language & tech-stack badges, project highlights, and auto-detected contribution snake.

## 📈 Domain Breakdown (Public Repos)

| Domain | Public Repos | Share |
|--------|-------------:|-------|
| 🎮 Unity / Game | **11** | `█████░░░░░░░` 41% |
| 📁 Other | **7** | `███░░░░░░░░░` 26% |
| 🤖 AI / ML | **5** | `██░░░░░░░░░░` 19% |
| 🌐 Web / Frontend | **4** | `██░░░░░░░░░░` 15% |

## 🔒 Private Repos (11)

| Repo | Purpose |
|------|---------|
| **3D-Asset-Unity** | Save some asset 3d unity can used |
| **Build-Home** | Build Home 3d |
| **Cat-find-Home** | - |
| **Craw-Data-industryGroup** | craw data product from industry group |
| **HTL2910** | No |
| **muse-5-nghien-cuu-thi-truong-va-tao-mot-app-doc** | Muse Company · nhiệm vụ #5: nghiên cứu thị trường và tạo một app đôc đáo giải quyết nỗi đau của người dùng để đưa lên google play store |
| **MuseCompanAITeam** | Công ty AI nhiều tài khoản Muse: chia việc theo sơ đồ công ty, hỏi đáp, duyệt bài, CEO báo cáo |
| **react-native-demo** | - |
| **ReactNative** | - |
| **SwiftUI** | - |
| **test-lai-hocSai1** | Hoc Unity |

## 🎮 Unity / Game (11)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**ForgeTax-Mini-3D-Game**](https://github.com/Hathanhlong2002/ForgeTax-Mini-3D-Game) | `HTML` | `2026-11-11` | 0 | - |
| [**BallPlatform3d-Casual-Game_Unity**](https://github.com/Hathanhlong2002/BallPlatform3d-Casual-Game_Unity) | `ShaderLab` | `2026-10-18` | 0 | unity 3d casual game |
| [**UniTask**](https://github.com/Hathanhlong2002/UniTask) | `-` | `2026-09-12` | 0 | Provides an efficient allocation free async/await integration for Unity. |
| [**unity-mcp**](https://github.com/Hathanhlong2002/unity-mcp) | `-` | `2026-09-12` | 0 | Unity MCP acts as a bridge between AI assistants and your Unity Editor. Give your LLM… |
| [**unity-actions**](https://github.com/Hathanhlong2002/unity-actions) | `-` | `2026-09-12` | 0 | Github actions for testing and building Unity projects |
| [**ml-agents**](https://github.com/Hathanhlong2002/ml-agents) | `-` | `2026-09-12` | 0 | The Unity Machine Learning Agents Toolkit (ML-Agents) is an open-source project that… |
| [**TimDoi**](https://github.com/Hathanhlong2002/TimDoi) | `C#` | `2023-07-19` | 0 | unity 2d |
| [**QHTT**](https://github.com/Hathanhlong2002/QHTT) | `ShaderLab` | `2023-07-19` | 0 | unity matrix |
| [**Game-2d-ban-may-bay-c--b-n**](https://github.com/Hathanhlong2002/Game-2d-ban-may-bay-c--b-n) | `C#` | `2023-07-19` | 0 | unity game |
| [**flappy-bird**](https://github.com/Hathanhlong2002/flappy-bird) | `C#` | `2023-07-19` | 0 | unity game flappy bird |
| [**Doan-So-udemy**](https://github.com/Hathanhlong2002/Doan-So-udemy) | `C#` | `2023-07-19` | 0 | unity c# |

## 📁 Other (7)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**Hathanhlong2002**](https://github.com/Hathanhlong2002/Hathanhlong2002) | `-` | `2026-11-10` | 0 | Profile README |
| [**wxt**](https://github.com/Hathanhlong2002/wxt) | `-` | `2026-09-12` | 0 | ⚡ Next-gen Web Extension Framework |
| [**playwright-mcp**](https://github.com/Hathanhlong2002/playwright-mcp) | `-` | `2026-09-12` | 0 | Playwright MCP server |
| [**uv**](https://github.com/Hathanhlong2002/uv) | `-` | `2026-09-12` | 0 | An extremely fast Python package and project manager, written in Rust. |
| [**dagger**](https://github.com/Hathanhlong2002/dagger) | `-` | `2026-09-12` | 0 | Automation engine to build, test and ship any codebase. Runs locally, in CI, or… |
| [**superpowers**](https://github.com/Hathanhlong2002/superpowers) | `-` | `2026-09-12` | 0 | An agentic skills framework & software development methodology that works. |
| [**spec-kit**](https://github.com/Hathanhlong2002/spec-kit) | `-` | `2026-09-12` | 0 | 💫 Toolkit to help you get started with Spec-Driven Development |

## 🤖 AI / ML (5)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**gflow-cli**](https://github.com/Hathanhlong2002/gflow-cli) | `TypeScript` | `2026-10-14` | 0 | GFlow CLI — Command-line tool that automates Google Flow in your local Chrome browser.… |
| [**awesome-llm-apps**](https://github.com/Hathanhlong2002/awesome-llm-apps) | `-` | `2026-04-23` | 0 | 100+ AI Agent & RAG apps you can actually run — clone, customize, ship. |
| [**learn_code_python-and-analysts-for-dataset**](https://github.com/Hathanhlong2002/learn_code_python-and-analysts-for-dataset) | `Jupyter Notebook` | `2023-08-01` | 0 | Code python |
| [**Python-for-data-science**](https://github.com/Hathanhlong2002/Python-for-data-science) | `Jupyter Notebook` | `2023-06-22` | 0 | Phân tích điểm thi |
| [**Thi-giac-may-tinh**](https://github.com/Hathanhlong2002/Thi-giac-may-tinh) | `Jupyter Notebook` | `2023-06-22` | 0 | thi giac may tinh |

## 🌐 Web / Frontend (4)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**github-repos-dashboard-Fork**](https://github.com/Hathanhlong2002/github-repos-dashboard-Fork) | `Python` | `2026-11-27` | 0 | Automated GitHub repos dashboard and dynamic profile README |
| [**github-repos-dashboard**](https://github.com/Hathanhlong2002/github-repos-dashboard) | `HTML` | `2026-11-10` | 0 | Automated overview & manager for all personal GitHub repositories. Helps the owner and… |
| [**eyetube-control**](https://github.com/Hathanhlong2002/eyetube-control) | `JavaScript` | `2026-09-13` | 0 | - |
| [**tool-capture**](https://github.com/Hathanhlong2002/tool-capture) | `TypeScript` | `2026-09-13` | 0 | - |

---

<a id="setup-guide"></a>
<details>
<summary><strong>🚀 Detailed Setup Guide (for forked users)</strong></summary>

> **Note for forked users**: Always use the **Actions** and **Settings** tabs at the top of **your own fork** (never click links inside someone else's repo before running your own workflow). Running **Update Repos Dashboard** on your fork uses `${{ github.repository_owner }}`, so it automatically targets your account (`<your-username>`) and never the upstream repository.

### 1. Enable GitHub Actions on your fork

1. On **your fork's top bar**, open the **Actions** tab and click **I understand my workflows, go ahead and enable them**
2. Confirm **Update Repos Dashboard** ([.github/workflows/update-dashboard.yml](.github/workflows/update-dashboard.yml)) is enabled in the left sidebar

### 2. Enable GitHub Pages (before first run)

1. On **your fork's top bar**, open **Settings → Pages** and under **Build and deployment**, select Source: **GitHub Actions**
2. The `Deploy to GitHub Pages` workflow packages only `index.html` and `data/dashboard.json` into `_site/` (never exposing `scripts/` or `README.md`)

### 3. (Optional) Enable Private Repos & Profile README Sync

Skip this step if you only want a public repos dashboard. To include private repos (name + purpose only) and auto-update your GitHub profile:

1. **Create your profile repo** (if you don't have one yet): [![Create Profile Repo](https://img.shields.io/badge/Create_Profile_Repo-purple?style=for-the-badge)](https://github.com/new?description=GitHub%20Profile%20README&visibility=public)
   - Repository name must match **your exact GitHub username** · Visibility: **Public**
2. **Create a Classic PAT**: [![Get Token](https://img.shields.io/badge/Get_Token-orange?style=for-the-badge)](https://github.com/settings/tokens/new?scopes=repo&description=github-repos-dashboard)
   - Select **Generate new token (classic)**, check the **`repo`** scope, and copy the token
3. **Save it as a repo secret**: on **your fork's top bar**, open **Settings → Secrets and variables → Actions → New repository secret**
   - Name: `PERSONAL_ACCESS_TOKEN` · Value: paste your token

### 4. Run the dashboard workflow on your fork

1. On **your fork's top bar**, open **Actions → Update Repos Dashboard → Run workflow**
2. Because the workflow reads `${{ github.repository_owner }}`, it automatically updates **your** `README.md`, `data/dashboard.json`, and `<your-username>/<your-username>/README.md` (auto-detecting `main`/`master`), then triggers GitHub Pages deployment.

### 5. (Optional) Add Contribution Snake

The snake section is **automatically hidden** on your profile until the `output` branch exists (no broken image if skipped). To enable it:

1. In your profile repo (`<your-username>/<your-username>`), create `.github/workflows/snake.yml`:

```yaml
name: Generate Snake
on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

2. In your profile repo's **Actions** tab → run **Generate Snake**, then re-run **Update Repos Dashboard** on your fork.

</details>

*Generated automatically by `scripts/update_dashboard.py`. Run the workflow to refresh.*