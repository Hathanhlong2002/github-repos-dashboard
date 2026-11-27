# 📊 GitHub Repos Dashboard — Hà Thành Long

Automated GitHub repository catalog, zero-rate-limit static Web Dashboard (`data/dashboard.json`), minimal private-repo listing (name + purpose only), and adaptive light/dark Profile README sync.

[![Open Web Dashboard](https://img.shields.io/badge/Open_Web_Dashboard-2563EB?style=for-the-badge&logo=githubpages&logoColor=white)](https://HTL2910.github.io/github-repos-dashboard/) [![View Profile](https://img.shields.io/badge/Profile_HTL2910-1E293B?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HTL2910/HTL2910) [![Run Sync Workflow](https://img.shields.io/badge/Run_Workflow-16A34A?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/HTL2910/github-repos-dashboard/actions/workflows/update-dashboard.yml)

**Web Dashboard**: [https://HTL2910.github.io/github-repos-dashboard/](https://HTL2910.github.io/github-repos-dashboard/)  
**Updated**: `2026-11-27 09:44 UTC`  
**Total**: **78 repos** (`43` public · `35` private)  
<sub>Forking this repo? Jump to the <a href="#setup-guide">Setup Guide</a> below — use the <strong>Actions</strong> &amp; <strong>Settings</strong> tabs at the top of your fork for the first run, then all links auto-update to your repo.</sub>

## ✨ Features

- **Unified Categorization**: `scripts/update_dashboard.py` and `index.html` share identical priority rules (`topics → keyword tokens → language → Other`), keeping `README.md` and Web UI 100% consistent.
- **Zero Rate-Limit Snapshot**: GitHub Actions publishes `data/dashboard.json` alongside `README.md` so visitors load the dashboard without hitting GitHub's 60 req/hr unauthenticated limit.
- **Privacy-Safe Private Repos**: When `PERSONAL_ACCESS_TOKEN` is configured, private repos are fetched via `/user/repos?affiliation=owner` and stripped down to **name and purpose only** — no links, languages, stars, or timestamps.
- **Hardened Web UI & Scoped Pages Deploy**: `index.html` renders strictly with safe DOM APIs (zero `innerHTML` / inline handlers) and `pages.yml` deploys only `_site/` (`index.html` + `data/dashboard.json`).
- **Adaptive Profile README**: Automatically syncs `{owner}/{owner}/README.md` (auto-detecting `main`/`master` default branch) with light/dark `<picture>` cards, dynamic language & tech-stack badges, project highlights, and auto-detected contribution snake.

## 📈 Domain Breakdown (Public Repos)

| Domain | Public Repos | Share |
|--------|-------------:|-------|
| 🎮 Unity / Game | **21** | `██████░░░░░░` 49% |
| 🤖 AI / ML | **14** | `████░░░░░░░░` 33% |
| 🌐 Web / Frontend | **6** | `██░░░░░░░░░░` 14% |
| 📁 Other | **2** | `█░░░░░░░░░░░` 5% |

## 🔒 Private Repos (35)

| Repo | Purpose |
|------|---------|
| **Adventure_3D** | Unity adventure 3D |
| **AI-Gen-Image-Local** | - |
| **ai-voice-assistant** | AI Voice Assistant for customer service |
| **ALl_mockup_app** | mockup for app demo |
| **android-hidden-api-bypass** | - |
| **AR_VR_for_Unity** | AR for Unity |
| **bus_travel** | Travel |
| **create_model** | create model fbx |
| **dola-render-gateway** | - |
| **Download_Image_sharepoint** | - |
| **Fit-Snap** | - |
| **FloorplanToQOC** | FloorplanToQOC predict |
| **Game-with-AI** | - |
| **Gift** | myGift |
| **hoplongtech_tool_web** | hoplongtech craw |
| **kahi-ai-pro** | - |
| **kiem-cu-duong-xua** | Kiếm Cũ Đường Xưa — game nhập vai kiếm hiệp 2.5D chơi trên trình duyệt (Vite + TypeScript + PixiJS) |
| **Machine-Learning-Model** | Use Machine Learning |
| **Many-feature** | có các chức năng sau này có thể cần dùng |
| **Misumi_data_Tool** | tool |
| **muse-6-bxv-address-autofill** | MuseAssistantTeam #6: bxv-address-autofill — Package TypeScript decideAddress cho opilot-pm (BXV Smart Call) |
| **MUSE-TOOL-VIDEO** | Independent Windows tool for Muse account management and image/video automation |
| **MuseAssistantTeam** | Công ty AI nhiều tài khoản Muse: chia việc theo sơ đồ công ty, hỏi đáp, duyệt bài, CEO báo cáo |
| **my-gift** | unity |
| **My_Asset_Unity** | save and test my new asset |
| **my_Game** | gift for me |
| **Onepiece-Asset** | - |
| **React-Native-Example** | Learn Code React |
| **React_web_gift** | private repo gift for friend |
| **Security_Game** | Security in Game |
| **shoot-to-win** | - |
| **SmartPhone-website** | - |
| **Unity_HDRP_Test** | unity project test feature in HDRP |
| **zalo-bot** | - |
| **Zalo-MiniApp** | Zalo Mini App - vote feature and future mini apps |

## 🎮 Unity / Game (21)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**FPS-Zombie-Suong-Mu**](https://github.com/HTL2910/FPS-Zombie-Suong-Mu) | `JavaScript` | `2026-11-22` | 0 | FPS Zombie Sương Mù v6.5 — 3D WebGL/Three.js Survival Horror FPS in Ha Don Village… |
| [**Dungeon-Survivor-3D**](https://github.com/HTL2910/Dungeon-Survivor-3D) | `JavaScript` | `2026-11-22` | 0 | Dungeon Survivor 3D — WebGL/Three.js Action Survivor with 26 A-Z VFX skills, 6 heroes… |
| [**Wocel**](https://github.com/HTL2910/Wocel) | `C#` | `2026-10-08` | 0 | - |
| [**Echo-of-the-Void**](https://github.com/HTL2910/Echo-of-the-Void) | `C#` | `2026-09-26` | 0 | Echo of the Void là tựa game 2D Precision-Platformer kết hợp Metroidvania nhịp độ… |
| [**education**](https://github.com/HTL2910/education) | `C#` | `2025-12-20` | 1 | unity 3d |
| [**Environmental-Education**](https://github.com/HTL2910/Environmental-Education) | `C#` | `2025-12-20` | 1 | Environmental Education Unity Game |
| [**Farm**](https://github.com/HTL2910/Farm) | `C#` | `2025-09-07` | 0 | Farming game made in Unity |
| [**SaveDataUnity**](https://github.com/HTL2910/SaveDataUnity) | `ShaderLab` | `2025-08-23` | 0 | Use Asset Bundles and addressable |
| [**Voice_Game**](https://github.com/HTL2910/Voice_Game) | `C#` | `2025-08-03` | 0 | use voice to play game |
| [**photon_Game**](https://github.com/HTL2910/photon_Game) | `C#` | `2025-08-03` | 0 | Photon Game Unity |
| [**Whisper-For-Unity**](https://github.com/HTL2910/Whisper-For-Unity) | `-` | `2025-07-22` | 0 | Use Whisper for Unity and select Model |
| [**TestBuildingSystem**](https://github.com/HTL2910/TestBuildingSystem) | `C#` | `2025-07-09` | 0 | testBuilding System - use System Surival |
| [**JellyField**](https://github.com/HTL2910/JellyField) | `ShaderLab` | `2025-05-25` | 0 | unity clone test Jelly-Field |
| [**Infinity-Ball**](https://github.com/HTL2910/Infinity-Ball) | `ShaderLab` | `2025-05-17` | 0 | unity beginer |
| [**URP_Game**](https://github.com/HTL2910/URP_Game) | `ShaderLab` | `2024-12-15` | 0 | Use for URP Project Test |
| [**Game-Developer-3D**](https://github.com/HTL2910/Game-Developer-3D) | `-` | `2024-12-02` | 0 | Udemy Course |
| [**Color-Maze-Adventure**](https://github.com/HTL2910/Color-Maze-Adventure) | `ShaderLab` | `2024-11-20` | 0 | Unity Game Color Maze Adventure |
| [**Game-Do_Vui**](https://github.com/HTL2910/Game-Do_Vui) | `ShaderLab` | `2024-08-26` | 0 | unity game 2D |
| [**UnityLearning**](https://github.com/HTL2910/UnityLearning) | `Mathematica` | `2024-08-04` | 0 | https://learn.unity.com/ed-pd/course/teach-unity |
| [**Casual-Game**](https://github.com/HTL2910/Casual-Game) | `ShaderLab` | `2024-07-26` | 0 | unity |
| [**BanMayBay2D**](https://github.com/HTL2910/BanMayBay2D) | `C#` | `2024-03-17` | 0 | 2D unity Basic |

## 🤖 AI / ML (14)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**OCR-Text-In-Vcam**](https://github.com/HTL2910/OCR-Text-In-Vcam) | `Python` | `2026-11-26` | 0 | Real-time Windows screen OCR (Vietnamese + English ONNX) with timestamped file logging |
| [**muse-3-vn-realtime-voice-agent**](https://github.com/HTL2910/muse-3-vn-realtime-voice-agent) | `Python` | `2026-11-22` | 0 | MuseAssistantTeam #3: vn-realtime-voice-agent — AI trợ lý giọng nói realtime trả lời… |
| [**muse-1-vn-address-autofill**](https://github.com/HTL2910/muse-1-vn-address-autofill) | `Python` | `2026-11-22` | 0 | Muse Company · nhiệm vụ #1: tôi có một bài toán như này : một cửa hàng bán đồ tiêu… |
| [**muse-2-multi-account-video-stats**](https://github.com/HTL2910/muse-2-multi-account-video-stats) | `Python` | `2026-11-22` | 0 | MuseAssistantTeam · #2: multi-account-video-stats — hệ thống quản lý account facebook… |
| [**laya_address_vn**](https://github.com/HTL2910/laya_address_vn) | `Python` | `2026-11-22` | 0 | Laya Address VN: Browser ONNX & CPU Backend Vietnamese Address Sufficiency Gates (v1… |
| [**AWS-AI-chatbot**](https://github.com/HTL2910/AWS-AI-chatbot) | `TypeScript` | `2026-11-04` | 0 | SafeGraph AI - VS Code AI coding assistant with Amazon Bedrock integration, local… |
| [**hypit**](https://github.com/HTL2910/hypit) | `-` | `2026-10-05` | 0 | Clone any viral video with AI agents. Not just a script, the whole workflow: swap the… |
| [**Full-Stack-Data-Science---Machine-Learning-BootCamp-Course**](https://github.com/HTL2910/Full-Stack-Data-Science---Machine-Learning-BootCamp-Course) | `Jupyter Notebook` | `2026-09-25` | 0 | Learn Udemy Full Stack Data Science & Machine Learning BootCamp Course |
| [**shorts**](https://github.com/HTL2910/shorts) | `Python` | `2026-09-10` | 0 | 🎥 AI Youtube Shorts video generator using Gemini API for images, voiceovers, music.… |
| [**Interview-Project**](https://github.com/HTL2910/Interview-Project) | `Python` | `2026-07-30` | 0 | Interview Job test |
| [**Chay-Code**](https://github.com/HTL2910/Chay-Code) | `Python` | `2025-08-29` | 0 | Chay code |
| [**Web-Scraping_Web-Crawling**](https://github.com/HTL2910/Web-Scraping_Web-Crawling) | `Python` | `2025-02-14` | 1 | Use Python 3, Selenium, BeautifulSoup and Chromium |
| [**OpenCV-with-Python**](https://github.com/HTL2910/OpenCV-with-Python) | `Python` | `2024-11-13` | 0 | OpenCV with Python:Recognition,Detection |
| [**Graph-based-recommend-system-using-GNN**](https://github.com/HTL2910/Graph-based-recommend-system-using-GNN) | `Jupyter Notebook` | `2024-07-26` | 0 | Đồ án tốt nghiệp |

## 🌐 Web / Frontend (6)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**social-flow-extension**](https://github.com/HTL2910/social-flow-extension) | `JavaScript` | `2026-11-26` | 0 | Social Flow - Chrome/Edge extension for automated page scrolling and configurable… |
| [**shopee-category-crawler**](https://github.com/HTL2910/shopee-category-crawler) | `JavaScript` | `2026-11-26` | 0 | Chrome extension to crawl multiple Shopee categories with pagination, saved progress… |
| [**page-harvest**](https://github.com/HTL2910/page-harvest) | `JavaScript` | `2026-11-26` | 0 | Page Harvest - Chrome/Edge extension to select repeating web items or tables and… |
| [**github-repos-dashboard**](https://github.com/HTL2910/github-repos-dashboard) | `HTML` | `2026-11-10` | 1 | Automated overview & manager for all personal GitHub repositories. Helps the owner and… |
| [**bang-cards-deck**](https://github.com/HTL2910/bang-cards-deck) | `TypeScript` | `2026-11-01` | 0 | - |
| [**JavaScript-Project**](https://github.com/HTL2910/JavaScript-Project) | `HTML` | `2025-02-17` | 0 | Learn JavaScript |

## 📁 Other (2)

| Repo | Language | Updated | Stars | Description |
|------|----------|---------|------:|-------------|
| [**HTL2910**](https://github.com/HTL2910/HTL2910) | `-` | `2026-11-10` | 0 | Config files for my GitHub profile. |
| [**Power-BI**](https://github.com/HTL2910/Power-BI) | `-` | `2024-08-21` | 0 | Hoc Power BI |

---

<a id="setup-guide"></a>
<details>
<summary><strong>🚀 Detailed Setup Guide (for forked users)</strong></summary>

> **Note for forked users**: For your very first setup, open the **Actions** and **Settings** tabs at the top of **your own fork** (GitHub Markdown strips relative links out of `/blob/...`). Once you run Step 4, every badge URL below automatically updates to your username and repository.

### 1. Enable GitHub Actions on your fork

[![Open Actions](https://img.shields.io/badge/Open_Actions-blue?style=for-the-badge)](https://github.com/HTL2910/github-repos-dashboard/actions)

1. Open the **Actions** tab on your fork and click **I understand my workflows, go ahead and enable them**
2. Confirm **Update Repos Dashboard** is enabled in the left sidebar

### 2. Enable GitHub Pages (before first run)

[![Open Pages Settings](https://img.shields.io/badge/Open_Pages_Settings-blue?style=for-the-badge)](https://github.com/HTL2910/github-repos-dashboard/settings/pages)

1. Open **Settings → Pages** on your fork and under **Build and deployment**, select Source: **GitHub Actions**
2. The `Deploy to GitHub Pages` workflow packages only `index.html` and `data/dashboard.json` into `_site/` (never exposing `scripts/` or `README.md`)

### 3. (Optional) Enable Private Repos & Profile README Sync

Skip this step if you only want a public repos dashboard. To include private repos (name + purpose only) and auto-update your GitHub profile:

1. **Create your profile repo** (if you don't have one yet): [![Create Profile Repo](https://img.shields.io/badge/Create_Profile_Repo-purple?style=for-the-badge)](https://github.com/new)
   - Repository name must match **your exact GitHub username** · Visibility: **Public**
2. **Create a Classic PAT**: [![Get Token](https://img.shields.io/badge/Get_Token-orange?style=for-the-badge)](https://github.com/settings/tokens/new?scopes=repo&description=github-repos-dashboard)
   - Select **Generate new token (classic)**, check the **`repo`** scope, and copy the token
3. **Save it as a repo secret**: [![Add Secret](https://img.shields.io/badge/Add_Secret-yellow?style=for-the-badge)](https://github.com/HTL2910/github-repos-dashboard/settings/secrets/actions)
   - In **Settings → Secrets and variables → Actions** on your fork, add `PERSONAL_ACCESS_TOKEN` and paste your token

### 4. Run the dashboard workflow

[![Run Workflow](https://img.shields.io/badge/Run_Workflow-success?style=for-the-badge)](https://github.com/HTL2910/github-repos-dashboard/actions/workflows/update-dashboard.yml)

Click **Run workflow** → updates `README.md`, `data/dashboard.json`, and your profile README (auto-detecting `main`/`master`), then automatically deploys GitHub Pages.

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

2. Open your profile repo Actions (e.g. [Actions](https://github.com/HTL2910/HTL2910/actions)) → run **Generate Snake**, then re-run **Update Repos Dashboard**.

</details>

*Generated automatically by `scripts/update_dashboard.py`. Run the workflow to refresh.*