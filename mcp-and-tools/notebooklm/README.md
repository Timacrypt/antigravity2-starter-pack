# 📓 NotebookLM MCP 快速整合指南

本模組協助將 Google 官方的 **NotebookLM** 知識庫以 MCP (Model Context Protocol) 伺服器方式無縫介接至 **Antigravity 2.0**。

---

## 🌟 核心功能
* **跨筆記本智慧查詢**：Agent 可直接檢索您在 NotebookLM 中的所有筆記與上傳文件（PDF、Google Drive 文件、YouTube 逐字稿等）。
* **來源動態新增 (`source_add`)**：Agent 可自主將網址、文字、檔案或雲端硬碟檔案加進您的 NotebookLM 筆記本。
* **Studio 生成產物 (`studio_create`)**：直接調用 NotebookLM 生成 Audio Overview（雙人對談 Podcast 音訊）、簡報與視覺化資訊圖表！
* **下載與匯出產物 (`download_artifact`)**：自動將 NotebookLM 產出的音訊與內容下載至本機資料夾。

---

## 🔑 授權與登入（nlm login）

NotebookLM MCP 使用 Google 官方 CLI 認證：
1. 打開終端機（或在 Antigravity 2.0 終端中執行）：
   ```bash
   nlm login
   ```
2. 系統會自動喚醒瀏覽器並完成 Google 帳號授權。
3. 若有多個 Google 帳號需切換，可隨時執行：
   ```bash
   nlm login switch <profile_name>
   ```

---

## ⚙️ Antigravity 2.0 MCP 配置說明

在 Antigravity 2.0 中，MCP 伺服器配置位於：
* `~/.gemini/antigravity/mcp/notebooklm/`

當您執行本專案的 `python install.py` 或由 Agent 自動安裝時，相關指令與 Schema 會自動部署至該目錄。
若您使用的是其他支援 MCP 的編輯器（如 Claude Desktop 或 Cursor），可參考 `mcp-config.example.json` 的配置範例。
