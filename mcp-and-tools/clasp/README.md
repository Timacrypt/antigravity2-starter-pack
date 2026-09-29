# ☁️ Google Apps Script CLI (clasp) 新手指南

`clasp`（Command Line Apps Script Projects）是 Google 官方釋出的命令列工具，讓您可以直接在本地電腦使用 VS Code 或 Antigravity 2.0 撰寫 Google Apps Script（GAS），並將程式碼同步到 Google 雲端！

---

## 🚀 核心優勢
* **本地開發**：在 Antigravity 2.0 中直接利用 AI Agent 編寫 Google 試算表（Sheets）、文件（Docs）、表單（Forms）的自動化巨集。
* **版本控制**：可以使用 Git 管理您的 Google Apps Script 程式碼。
* **一鍵推送**：在終端機輸入 `clasp push` 即可將本地代碼發布至雲端。

---

## 🛠️ 安裝步驟

### 1. 前置需求
確保您的電腦已安裝 [Node.js](https://nodejs.org)（包含 `npm`）。

### 2. 全域安裝 clasp
在終端機中執行：
```bash
npm install -g @google/clasp
```
*(如果遇到權限問題，macOS/Linux 可加上 `sudo npm install -g @google/clasp`)*

也可以直接執行本目錄的一鍵安裝腳本：
```bash
bash setup-clasp.sh
```

### 3. 啟用 Google Apps Script API
在第一次登入前，請至 [Google Apps Script 使用者設定](https://script.google.com/home/usersettings) 開啟 **Google Apps Script API** 開關。

### 4. 登入 Google 帳號
在終端機執行：
```bash
clasp login
```
瀏覽器會自動彈出 Google 登入視窗，點擊「允許」即可完成授權。

---

## 📋 常用指令速查表

| 指令 | 說明 |
| :--- | :--- |
| `clasp login` | 登入 Google 帳號授權 clasp |
| `clasp logout` | 登出目前的 Google 帳號 |
| `clasp create --title "我的專案" --type sheets` | 建立一個綁定在 Google 試算表的新專案 |
| `clasp clone <scriptId>` | 下載既有的 Google Apps Script 專案到本地 |
| `clasp pull` | 從 Google 雲端拉取最新程式碼到本地 |
| `clasp push` | 將本地修改好的代碼推送到 Google 雲端 |
| `clasp open` | 在瀏覽器中直接開啟該 Apps Script 編輯器 |
