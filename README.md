# 📊 GitHub Repos Dashboard - Hathanhlong2002

## 🚀 Detailed Setup Guide

> **Note for forked users**: After forking, run the workflow on your fork so all links and content update to your username.

### 1. Enable the workflow (required on forks)

[![Open Actions](https://img.shields.io/badge/Open_Actions-blue?style=for-the-badge)](https://github.com/Hathanhlong2002/github-repos-dashboard/actions)

1. Click **Update Repos Dashboard** in the left sidebar
2. Click **Enable workflow** (if it shows as Disabled)

### 2. Create your profile repository

[![Create Profile Repo](https://img.shields.io/badge/Create_Profile_Repo-purple?style=for-the-badge)](https://github.com/new?name=Hathanhlong2002&description=Profile+README)

- Name must be exactly: **`Hathanhlong2002`**
- Visibility: **Public**

### 3. Create a Personal Access Token

[![Get Token](https://img.shields.io/badge/Get_Token-orange?style=for-the-badge)](https://github.com/settings/tokens/new?scopes=repo&description=github-repos-dashboard)

- Select **Generate new token (classic)**
- Check the **`repo`** scope
- Copy the token immediately

### 4. Add the token as a secret

[![Add Secret](https://img.shields.io/badge/Add_Secret-yellow?style=for-the-badge)](https://github.com/Hathanhlong2002/github-repos-dashboard/settings/secrets/actions)

- Name: `PERSONAL_ACCESS_TOKEN`
- Paste your token as the value

### 5. Enable GitHub Pages

[![Open Pages Settings](https://img.shields.io/badge/Open_Pages_Settings-blue?style=for-the-badge)](https://github.com/Hathanhlong2002/github-repos-dashboard/settings/pages)

1. Source: **Deploy from a branch**
2. Branch: `main` / `/ (root)`
3. Click **Save**

Dashboard will be available at: [https://Hathanhlong2002.github.io/github-repos-dashboard/](https://Hathanhlong2002.github.io/github-repos-dashboard/)

### 6. (Optional) Add Contribution Snake

To show the animated contribution snake on your profile:

1. Go to your profile repo: [https://github.com/Hathanhlong2002/Hathanhlong2002](https://github.com/Hathanhlong2002/Hathanhlong2002)
2. Create file `.github/workflows/snake.yml` with this content:

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
          github_user_name: Hathanhlong2002
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

3. Go to [Actions](https://github.com/Hathanhlong2002/Hathanhlong2002/actions) → run **Generate Snake**

### 7. Run the dashboard workflow

[![Run Workflow](https://img.shields.io/badge/Run_Workflow-success?style=for-the-badge)](https://github.com/Hathanhlong2002/github-repos-dashboard/actions/workflows/update-dashboard.yml)

This updates this README and your profile README.

### 8. View your profile

[![View Profile](https://img.shields.io/badge/View_Profile-blue?style=for-the-badge)](https://github.com/Hathanhlong2002/Hathanhlong2002)

---

**Web Dashboard**: [https://Hathanhlong2002.github.io/github-repos-dashboard/](https://Hathanhlong2002.github.io/github-repos-dashboard/)

**Updated**: 2026-11-10 04:49 UTC  
**Total**: 25 repos (0 private / 25 public)

---

## 🌐 Web / Frontend (5)

| Repo | Language | Updated | Stars | Visibility | Description |
|------|----------|---------|-------|------------|-------------|
| [github-repos-dashboard](https://github.com/Hathanhlong2002/github-repos-dashboard) | HTML | 2026-11-10 | 0 | 🌐 | Automated overview & manager for all personal GitHub reposit |
| [gflow-cli](https://github.com/Hathanhlong2002/gflow-cli) | TypeScript | 2026-10-14 | 0 | 🌐 | GFlow CLI — Command-line tool that automates Google Flow in  |
| [eyetube-control](https://github.com/Hathanhlong2002/eyetube-control) | JavaScript | 2026-09-13 | 0 | 🌐 | - |
| [tool-capture](https://github.com/Hathanhlong2002/tool-capture) | TypeScript | 2026-09-13 | 0 | 🌐 | - |
| [wxt](https://github.com/Hathanhlong2002/wxt) | - | 2026-09-12 | 0 | 🌐 | ⚡ Next-gen Web Extension Framework |

## 🎮 Unity / Game (10)

| Repo | Language | Updated | Stars | Visibility | Description |
|------|----------|---------|-------|------------|-------------|
| [BallPlatform3d-Casual-Game_Unity](https://github.com/Hathanhlong2002/BallPlatform3d-Casual-Game_Unity) | ShaderLab | 2026-10-18 | 0 | 🌐 | unity 3d casual game |
| [UniTask](https://github.com/Hathanhlong2002/UniTask) | - | 2026-09-12 | 0 | 🌐 | Provides an efficient allocation free async/await integratio |
| [unity-actions](https://github.com/Hathanhlong2002/unity-actions) | - | 2026-09-12 | 0 | 🌐 | Github actions for testing and building Unity projects |
| [unity-mcp](https://github.com/Hathanhlong2002/unity-mcp) | - | 2026-09-12 | 0 | 🌐 | Unity MCP acts as a bridge between AI assistants and your Un |
| [ml-agents](https://github.com/Hathanhlong2002/ml-agents) | - | 2026-09-12 | 0 | 🌐 | The Unity Machine Learning Agents Toolkit (ML-Agents) is an  |
| [TimDoi](https://github.com/Hathanhlong2002/TimDoi) | C# | 2023-07-19 | 0 | 🌐 | unity 2d  |
| [QHTT](https://github.com/Hathanhlong2002/QHTT) | ShaderLab | 2023-07-19 | 0 | 🌐 | unity matrix |
| [Game-2d-ban-may-bay-c--b-n](https://github.com/Hathanhlong2002/Game-2d-ban-may-bay-c--b-n) | C# | 2023-07-19 | 0 | 🌐 | unity game |
| [flappy-bird](https://github.com/Hathanhlong2002/flappy-bird) | C# | 2023-07-19 | 0 | 🌐 | unity game flappy bird |
| [Doan-So-udemy](https://github.com/Hathanhlong2002/Doan-So-udemy) | C# | 2023-07-19 | 0 | 🌐 | unity c# |

## 📁 Other (6)

| Repo | Language | Updated | Stars | Visibility | Description |
|------|----------|---------|-------|------------|-------------|
| [Hathanhlong2002](https://github.com/Hathanhlong2002/Hathanhlong2002) | - | 2026-11-10 | 0 | 🌐 | Profile README |
| [playwright-mcp](https://github.com/Hathanhlong2002/playwright-mcp) | - | 2026-09-12 | 0 | 🌐 | Playwright MCP server |
| [uv](https://github.com/Hathanhlong2002/uv) | - | 2026-09-12 | 0 | 🌐 | An extremely fast Python package and project manager, writte |
| [dagger](https://github.com/Hathanhlong2002/dagger) | - | 2026-09-12 | 0 | 🌐 | Automation engine to build, test and ship any codebase. Runs |
| [superpowers](https://github.com/Hathanhlong2002/superpowers) | - | 2026-09-12 | 0 | 🌐 | An agentic skills framework & software development methodolo |
| [spec-kit](https://github.com/Hathanhlong2002/spec-kit) | - | 2026-09-12 | 0 | 🌐 | 💫 Toolkit to help you get started with Spec-Driven Developme |

## 🤖 AI / ML (4)

| Repo | Language | Updated | Stars | Visibility | Description |
|------|----------|---------|-------|------------|-------------|
| [awesome-llm-apps](https://github.com/Hathanhlong2002/awesome-llm-apps) | - | 2026-04-23 | 0 | 🌐 | 100+ AI Agent & RAG apps you can actually run — clone, custo |
| [learn_code_python-and-analysts-for-dataset](https://github.com/Hathanhlong2002/learn_code_python-and-analysts-for-dataset) | Jupyter Notebook | 2023-08-01 | 0 | 🌐 | Code python |
| [Python-for-data-science](https://github.com/Hathanhlong2002/Python-for-data-science) | Jupyter Notebook | 2023-06-22 | 0 | 🌐 | Phân tích điểm thi |
| [Thi-giac-may-tinh](https://github.com/Hathanhlong2002/Thi-giac-may-tinh) | Jupyter Notebook | 2023-06-22 | 0 | 🌐 | thi giac may tinh  |

---

*Generated automatically. Run the workflow to refresh.*