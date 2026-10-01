# Antigravity 2.0 Agent Automation Protocol (AGENTS.md)

This file contains automated instructions for **Google Antigravity 2.0** and compatible AI coding agents.
When a user asks you to "install", "setup", or "import" the skills and tools from this repository, or asks to "下載專案" (download practice project), follow these precise instructions step by step.

---

## 🤖 Part 1: Starter Pack Installation Protocol

### Step 1: Identify Installation Directories
1. Global Skills Directory:
   - Path: `~/.gemini/config/skills/` (expand `~` to the user's home directory).
   - If this directory does not exist, create it.
2. Global MCP Directory:
   - Path: `~/.gemini/antigravity/mcp/notebooklm/`
   - If this directory does not exist, create it.

### Step 2: Install Skills
Copy every folder inside the `skills/` directory of this repository into the user's global skills directory (`~/.gemini/config/skills/`):
- `brainstorming/`
- `teach/`
- `grill-me/`
- `grilling/`
- `grill-with-docs/`
- `wait-what/` (Customized: Traditional Chinese zhtw, 10th-grade high school level, English technical terms)
- `handoff/`
- `to-questionnaire/`
- `writing-for-agents/`
- `ask-matt/`
- `diagnosing-bugs/`
- `research/`
- `prototype/`
- `to-spec/`
- `slide-simple/`
- `frontend-design/`
- `docx/`
- `xlsx/`
- `pptx/`
- `pdf/`
- `skill-creator/`
- `find-skills/`
- `officecli/`
- `setup-google-workspace-mcp/`
- `setup-opencode/`

*Note: Overwrite any existing files if the user requested a fresh installation or upgrade.*

> ⚠️ **On-Demand 技能守則（重要）**：
> - `setup-google-workspace-mcp` 與 `setup-opencode` 屬於**按需提供（On-Demand）技能**，僅在學員明確提出需求（如輸入「Google Workspace MCP 安裝」或「OpenCode 安裝」）時才啟動逐步引導。平常一般對話中**切勿主動推銷或主動詢問**是否需要安裝此二者。
> - 在 `setup-opencode` 流程中，若學員不熟悉終端機，AI 應直接在背景代為執行安裝與金鑰配置，勿讓學員自行開啟終端機敲指令。
> - 其餘所有 Skills、CLI、相依套件與教學專案皆為標準自動下載安裝。

### Step 3: Install Python Dependencies
The document processing skills (`docx`, `xlsx`, `pptx`, `pdf`) require standard Python libraries.
Run the following shell command using your terminal tool:
```bash
pip install -r requirements.txt --break-system-packages 2>/dev/null || pip install -r requirements.txt
```
*(Libraries installed: `python-docx`, `openpyxl`, `python-pptx`, `pypdf`, `pymupdf`)*

### Step 4: Install clasp (Google Apps Script CLI)
Check if Node.js (`npm`) is available in the user's system:
```bash
npm install -g @google/clasp
```
If npm is not installed or permission is denied, notify the user and provide instructions from `mcp-and-tools/clasp/README.md`.

### Step 5: Configure NotebookLM MCP
1. Copy the configuration and instruction files from `mcp-and-tools/notebooklm/` to `~/.gemini/antigravity/mcp/notebooklm/`.
2. Inform the user to run `nlm login` in their terminal to authenticate with their Google account for NotebookLM.

### Step 6: Confirmation & Summary
Once installation is complete, output a clear summary to the user in Traditional Chinese (繁體中文):
- List all 25 installed Skills with their visual emoji icons and brief descriptions.
- Explain how to trigger `/ask-matt` for routing and `/wait-what` for plain explanations.
- Explain how to use engineering skills (`/diagnosing-bugs`, `/prototype`, `/research`).
- Explain how to use `officecli`, `slide-simple`, `frontend-design`, and Office document skills (Word, Excel, PowerPoint, PDF).
- Clarify that Google Workspace MCP and OpenCode are available on-demand whenever requested.
- Provide next steps for `clasp login` and `nlm login`.

---

## 🩺 Part 2: Automated Practice Project Setup Protocol (學員下載專案自動協定)

### Trigger Phrases:
When the user enters any of the following phrases in chat:
- **「下載專案」**
- **「下載練習專案」**
- **「建立練習專案」**
- **「初始化 1002 練習」**
- **"download project"** / **"setup practice project"**

### Automated Actions for Antigravity 2.0:
1. **執行專案建立**：
   - 執行腳本 `python3 create-practice-project.py`（或在目前工作區下建立 `AI-Practice-Project/` 資料夾，並將 `practice-materials/` 中的檔案與產生的 `README.md` 完整複製過去）。
2. **初始化內容驗證**：
   - 確認目標目錄包含：
     - `糖尿病個案2026年8月.xlsx`（雙工作表，24 筆虛構個案追蹤與每日紀錄）。
     - `糖尿病患者個人檔案與照護紀錄_單頁美化版.pdf`。
     - `病人紀錄/`（包含手寫筆記 PDF、LINE 對話截圖 PDF、記事本文字檔 txt）。
     - 自動產生的 `README.md`（包含任務一至任務四）。
3. **回覆引導訊息給學員 (Traditional Chinese)**：
   - 清楚告知練習專案已建立完成，並展示檔案結構。
   - 重點提示 **任務一（/xlsx 篩選）** 與 **任務二（多模態資料辨識與匯入 Excel）**。
   - 提醒學員在操作過程中可隨時輸入 `/ask-matt` 或 `/wait-what` 尋求協助。
