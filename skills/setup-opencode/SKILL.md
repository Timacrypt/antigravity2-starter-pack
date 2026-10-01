---
name: setup-opencode
description: 當使用者明確提出「OpenCode 安裝」或「安裝 OpenCode」時觸發。以純繁體中文、極致新手友善方式，引導完全不懂技術的台灣學員在網頁註冊 OpenCode 並取得 Zen 免費 API Key。學員無需自行打開終端機輸入指令，AI Agent 會主動在後台代為執行安裝與金鑰配置。注意：此為 On-Demand 按需提供技能，平常對話中切勿主動推銷或主動詢問使用者是否要安裝。
metadata:
  icon: "💻"
  emoji: "💻"
---

# 💻 OpenCode 安裝與 Zen 免費金鑰引導 (setup-opencode)

本 Skill 專為**完全零技術背景、不熟悉命令列、不會操作終端機的台灣學員**設計。核心原則是「**學員只管網頁領金鑰，終端安裝由 AI Agent 全權代勞**」。

> [!IMPORTANT]
> **觸發守則（On-Demand Only）**：
> - 除非學員在對話中主動提出「OpenCode 安裝」或「安裝 OpenCode」，否則**絕對不要**在一般對話中主動推銷、詢問或提醒學員安裝此功能。
> - 一旦學員主動提出，立即啟動本引導流程。

---

## 🎯 核心原則（Agent 必須嚴格遵守）

1. **學員免開終端機（AI 代勞原則）**：
   - 絕不強迫學員手動打開 Terminal 或黑底命令列視窗敲指令。
   - 主動向學員說明：「**終端機安裝與設定由我來幫您執行，您只需要在瀏覽器領取免費金鑰貼給我就好！**」
   - 經學員同意或提供金鑰後，AI Agent 直接使用 `run_command` 工具在系統後台執行安裝與設定。
2. **極致清晰與零英文門檻**：
   - 網頁操作以「按鈕位置 + 顏色 + 中英標籤」明確指引。
3. **一步一步確認**：
   - 引導學員取得金鑰 ➔ 學員貼出金鑰 ➔ AI 執行安裝與寫入設定 ➔ 驗證回報。

---

## 📋 逐步操作引導流程（4 大極簡步驟）

### 步驟 1：網頁領取 Zen 免費 API 通關金鑰

向學員說明：
「請點擊以下官方網址，領取 OpenCode 的免費 AI 模型金鑰（Zen 免費額度）：
👉 [https://opencode.ai/zen](https://opencode.ai/zen)

**操作方式**：
1. 點選【右上角黑底按鈕】「Sign In」或「Get Started」。
2. 點選「Continue with Google」，使用您的 Google 帳號直接登入。
3. 登入成功後，在畫面中央會看到一個標記為 **API Key** 的欄位。
4. 請點選欄位右側的【Copy / 複製圖示】（複製那串以 `zen_` 開頭的英數字金鑰）。
5. **請把複製到的金鑰直接貼在聊天室回傳給我！**」

---

### 步驟 2：AI Agent 後台代為安裝 OpenCode

當學員提供金鑰或回覆已備妥金鑰後，AI Agent 告知學員：
「請稍候幾秒鐘，我正在您的系統後台自動安裝 OpenCode，您不需要打開任何黑底終端機視窗！」

**AI Agent 執行指令**（使用 `run_command`）：
1. 檢查系統環境與安裝：
   - macOS / Linux：
     ```bash
     curl -fsSL https://opencode.ai/install | bash
     ```
     （若系統已有 Node.js，亦可使用 `npm install -g opencode-ai`）
   - Windows：
     如在 WSL 環境下執行同上指令；若為原生 Windows 則執行官方 Windows 安裝指令。
2. 確認安裝結果：
   ```bash
   opencode --version || ~/.opencode/bin/opencode --version
   ```

---

### 步驟 3：AI Agent 後台代為配置 Zen API 金鑰

AI Agent 將學員在步驟 1 提供的 Zen API Key，直接設定至 OpenCode 配置環境：
1. 寫入或更新設定檔（通常位於 `~/.config/opencode/opencode.json`）：
   ```json
   {
     "$schema": "https://opencode.ai/config.json",
     "provider": {
       "zen": {
         "apiKey": "<學員提供的_ZEN_API_KEY>"
       }
     }
   }
   ```
2. 或在終端機背景執行登入/連線命令：
   ```bash
   opencode auth login --provider zen --key "<學員提供的_ZEN_API_KEY>"
   ```

---

### 步驟 4：驗證與完成通知

AI Agent 執行輕量檢查後，以繁體中文向學員回報：
「🎉 **太棒了！OpenCode 與 Zen 免費模型已為您成功安裝並設定完畢！**」

並附上極簡日常使用指南：
* **日常使用方式**：
  1. 如果想在終端機啟動：直接輸入 `opencode` 即可進入 AI 編程交談介面。
  2. 如果您平常使用 VS Code 或 Cursor：可在擴充套件市集搜尋並安裝「OpenCode」外掛，享受在編輯器內一鍵代碼生成。
  3. 平常有任何程式修改需求，也可以隨時直接跟我說，我會繼續協助您！
