# 💻 OpenCode 安裝與 Zen 免費金鑰手冊

本手冊供學員或助教離線查閱，提供 OpenCode 官方連結與常用指令。

> [!NOTE]
> 平常此功能為 **On-Demand（按需提供）**。學員若在對話中詢問「OpenCode 安裝」，AI Agent 將自動啟動 `setup-opencode` 技能。學員不需要親自操作終端機，AI Agent 會在系統後台代為完成安裝與設定！

---

## 快速摘要

* **官方領取 Zen 免費金鑰網址**：[https://opencode.ai/zen](https://opencode.ai/zen)
  * 使用 Google 帳號一鍵登入。
  * 複製首頁顯示的 `API Key`（`zen_...`）。
* **AI Agent 代勞安裝指令（學員免開終端機）**：
  * macOS / Linux：`curl -fsSL https://opencode.ai/install | bash`
  * NPM 方式：`npm install -g opencode-ai`
* **設定檔位置**：
  * `~/.config/opencode/opencode.json`
* **啟動方式**：
  * 終端機直接輸入：`opencode`
  * 查看模型：`/models`
  * 編輯器擴充：在 VS Code / Cursor 外掛市集搜尋「OpenCode」安裝。
