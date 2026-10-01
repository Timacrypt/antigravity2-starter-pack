---
name: setup-google-workspace-mcp
description: 當使用者明確提出「Google Workspace MCP 安裝」或「安裝 Google Workspace MCP」時觸發。以純繁體中文、極致無腦、看圖點擊（方位+顏色+中英對照）方式，一步步引導完全不懂英文與技術的台灣學員開啟 Google Drive、Sheets、Docs API 並完成 OAuth 憑證設置。注意：此為 On-Demand 按需提供技能，平常對話中切勿主動推銷或主動詢問使用者是否要安裝。
metadata:
  icon: "🌐"
  emoji: "🌐"
---

# 🌐 Google Workspace MCP 保母級安裝引導 (setup-google-workspace-mcp)

本 Skill 專為**完全不懂英文、零技術背景、不熟悉雲端主控台的台灣學員**設計。核心原則是「**極致無腦、看圖點擊、零英文門檻、一動一問**」。

> [!IMPORTANT]
> **觸發守則（On-Demand Only）**：
> - 除非學員在對話中主動提出「Google Workspace MCP 安裝」或「安裝 Google Workspace MCP」，否則**絕對不要**在一般對話中主動推銷、詢問或提醒學員安裝此功能。
> - 一旦學員主動提出，立即啟動本引導流程。

---

## 🎯 引導基本原則（Agent 必須嚴格遵守）

1. **不講原理與技術術語**：不解釋什麼是 OAuth、Token、API、Scopes。只講「點哪裡、選哪項、按哪顆按鈕」。
2. **位置 + 顏色 + 中英對照**：
   - 學員使用的 Google 介面可能是英文版或中文版，因此所有按鈕**一律標註位置、顏色與雙語對照**。
   - 範例格式：`請點選【右上角】的【藍色按鈕】「建立 / Create」`。
3. **一動一問（單步節奏）**：
   - 每次只給一個單一畫面的操作指令。
   - 給完指令後，詢問：「請完成這一步後，跟我說一聲『好了』，我們再進行下一步！」。
   - 等學員回報「好了」或貼圖確認，才提供下一個步驟。
4. **直達連結優先**：
   - 絕不讓學員自己在選單中迷路搜尋，直接給出 Google Cloud Console 具體頁面的直達網址。

---

## 📋 逐步操作引導流程（5 大無腦步驟）

### 步驟 1：建立專屬通行證（Google Cloud 專案）

1. 請學員點擊此專案直達網址：
   👉 [https://console.cloud.google.com/projectcreate](https://console.cloud.google.com/projectcreate)
2. 指令：
   - 在中間的「專案名稱 (Project name)」欄位，填寫：`My-Workspace-MCP`（或任意英文字母）。
   - 請點選【左下角】的【藍色按鈕】「建立 / Create」。
   - 等待約 5~10 秒鐘，畫面會自動載入完成。
3. 停頓確認：請學員回報「好了」再進入步驟 2。

---

### 步驟 2：一鍵打開 3 大服務開關（Drive、Sheets、Docs）

請學員**依序點擊以下 3 個直達連結**，每一個網頁都只做同一個動作：

1. **開啟 Google 雲端硬碟 (Google Drive API)**：
   - 直達網址：👉 [https://console.cloud.google.com/apis/library/drive.googleapis.com](https://console.cloud.google.com/apis/library/drive.googleapis.com)
   - 動作：請點選【中間偏左】的【藍色按鈕】「啟用 / Enable」。
2. **開啟 Google 試算表 (Google Sheets API)**：
   - 直達網址：👉 [https://console.cloud.google.com/apis/library/sheets.googleapis.com](https://console.cloud.google.com/apis/library/sheets.googleapis.com)
   - 動作：請點選【中間偏左】的【藍色按鈕】「啟用 / Enable」。
3. **開啟 Google 文件 (Google Docs API)**：
   - 直達網址：👉 [https://console.cloud.google.com/apis/library/docs.googleapis.com](https://console.cloud.google.com/apis/library/docs.googleapis.com)
   - 動作：請點選【中間偏左】的【藍色按鈕】「啟用 / Enable」。
4. 停頓確認：請學員回報「3 個都按啟用了」再進入步驟 3。

---

### 步驟 3：設定授權同意畫面（OAuth 同意畫面）

1. 請學員點擊直達網址：
   👉 [https://console.cloud.google.com/apis/credentials/consent](https://console.cloud.google.com/apis/credentials/consent)
2. **選擇類型**：
   - 點選圓圈「外部 (External)」➔ 點選【藍色按鈕】「建立 / Create」。
3. **第 1 頁（應用程式資訊）**：
   - 第一欄「應用程式名稱 (App name)」：填入 `MyAgent`。
   - 第二欄「使用者支援電子郵件」：下拉選單選取學員自己的 Gmail。
   - 滑鼠滑到網頁最下方，最後一欄「開發人員聯絡資訊」：填寫學員自己的 Gmail。
   - 點選【最下方中央】的【藍色按鈕】「儲存並繼續 / Save and Continue」。
4. **第 2 頁（範圍 Scopes）**：
   - 什麼都不用改，直接滑到網頁最下方，點選【藍色按鈕】「儲存並繼續 / Save and Continue」。
5. **第 3 頁（測試使用者 Test users - 關鍵步驟！）**：
   - 點選上方【+ 新增使用者 / + ADD USERS】按鈕。
   - 在彈出的小視窗中，填入學員自己的 Gmail 帳號。
   - 點選【新增 / Add】儲存。
   - 滑到網頁最下方，點選【藍色按鈕】「儲存並繼續 / Save and Continue」。
6. 停頓確認：請學員回報「看到摘要頁面了」再進入步驟 4。

---

### 步驟 4：下載通關密碼（憑證 JSON 檔案）

1. 請學員點擊憑證頁面直達網址：
   👉 [https://console.cloud.google.com/apis/credentials](https://console.cloud.google.com/apis/credentials)
2. 指令：
   - 點選【上方橫列】的【+ 建立憑證 / + CREATE CREDENTIALS】。
   - 在下拉選單中，點選第 2 項「OAuth 用戶端 ID / OAuth client ID」。
   - 在「應用程式類型 (Application type)」下拉選單中，選擇「桌面應用程式 (Desktop app)」。
   - 「名稱 (Name)」保持預設不變，點選【右下角】的【藍色按鈕】「建立 / Create」。
3. **下載檔案**：
   - 畫面中央會彈出一個小視窗，請點選【下載 JSON / Download JSON】（或右側帶有下載圖示的按鈕）。
   - 請將下載到電腦「下載 (Downloads)」資料夾的檔案，重新命名為：`credentials.json`。
4. 停頓確認：請學員確認「已經改名為 credentials.json」。

---

### 步驟 5：配置 MCP 與首次登入允許授權

1. **協助放置檔案**：
   - 請學員告知 `credentials.json` 的下載路徑，或由 AI Agent 主動協助將其移動至工作目錄。
2. **首次授權點擊（破除安全警告教學）**：
   - 當系統啟動 Google 驗證時，瀏覽器會彈出 Google 登入畫面。
   - 選取學員自己的 Gmail 登入。
   - **關鍵安全提示破解**：若畫面上出現「Google 尚未驗證此應用程式 (Google hasn't verified this app)」的警示框，**完全不用擔心**，請照以下方式點擊：
     1. 點選【左下角灰色小字】「進階 (Advanced)」。
     2. 點選最下方展開的文字「前往 MyAgent（不安全）/ Go to MyAgent (unsafe)」。
     3. 勾選所有要授權的 Google Drive / Sheets / Docs 方框。
     4. 點選【繼續 / Continue】完成授權！
3. **恭喜完成**：回報學員已正式完成 Google Workspace MCP 連線，現在可以直接對話操作雲端硬碟、試算表與文件！
