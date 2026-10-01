# 🌐 Google Workspace MCP 安裝參考手冊

本手冊供學員或助教離線查閱，提供直達連結與畫面點擊提示（針對 Google Drive、Google Sheets、Google Docs）。

> [!NOTE]
> 平常此功能為 **On-Demand（按需提供）**。學員若在對話中詢問「Google Workspace MCP 安裝」，AI Agent 將自動啟動 `setup-google-workspace-mcp` 技能進行逐步帶領。

---

## 快速直達連結一覽表

| 步驟 | 目標操作 | 官方直達網址 | 重點按鈕標記 |
| :--- | :--- | :--- | :--- |
| **1. 專案建立** | 建立 Google Cloud 專案 | [前往建立專案](https://console.cloud.google.com/projectcreate) | 輸入名稱 ➔ 左下角藍色 `[建立 / Create]` |
| **2.1 Drive API** | 開啟雲端硬碟 API | [前往 Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com) | 中間偏左藍色 `[啟用 / Enable]` |
| **2.2 Sheets API** | 開啟試算表 API | [前往 Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com) | 中間偏左藍色 `[啟用 / Enable]` |
| **2.3 Docs API** | 開啟文件 API | [前往 Docs API](https://console.cloud.google.com/apis/library/docs.googleapis.com) | 中間偏左藍色 `[啟用 / Enable]` |
| **3. 同意畫面** | 設定 OAuth 同意畫面 | [前往同意畫面](https://console.cloud.google.com/apis/credentials/consent) | 選「外部」➔ 填 Gmail ➔ **新增自己為測試使用者** |
| **4. 下載憑證** | 建立桌面憑證 | [前往憑證主頁](https://console.cloud.google.com/apis/credentials) | `[+ 建立憑證]` ➔ `[OAuth 用戶端 ID]` ➔ 選「桌面應用程式」➔ 下載 JSON 改名 `credentials.json` |

---

## 首次登入「安全性警告」破解指引
當授權視窗彈出「Google 尚未驗證此應用程式 (Google hasn't verified this app)」時：
1. 點擊畫面左下角灰字 **「進階 (Advanced)」**。
2. 點擊展開的文字 **「前往 MyAgent（不安全）/ Go to MyAgent (unsafe)」**。
3. 勾選所有存取權限方框，點擊「繼續 / Continue」即可成功。
