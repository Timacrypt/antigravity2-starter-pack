# 🚀 Antigravity 2.0 Agent Starter Pack

> 專為 **Google Antigravity 2.0** 打造的開源、免費、高性能 Agent 技能與工具懶人包。  
> 整合 **Matt Pocock 經典思維與工程技能組** ＋ **Anthropic 官方前端美學與 Office 辦公系列** ＋ **Swiss 編輯風簡報設計** ＋ **clasp (Google Apps Script)** ＋ **NotebookLM MCP**。

---

## ⚡ 30 秒極速安裝（新手首選）

您不需要手動下載檔案或設定複雜路徑！只要打開您的 **Antigravity 2.0**，在對話框中貼上以下這段話（請將網址替換為您的 GitHub Repo 網址）：

```text
請閱讀這個 GitHub Repo：https://github.com/Timacrypt/antigravity2-starter-pack
並依照其中的 AGENTS.md 指引，將所有 Skills、clasp 與 NotebookLM MCP 自動安裝到我的 Antigravity 2.0 環境中。
```

Antigravity 2.0 就會自主讀取本專案、自動建立全域目錄（`~/.gemini/config/skills/`）、複製技能並安裝必要 Python 依賴！

---

## 🩺 10/02 AI 實戰教學練習專案（一鍵下載與初始化）

本倉庫特別為 **10/02 AI Agent 臨床照護實戰教學** 內建了完整的教學實戰練習包（包含虛構糖尿病追蹤試算表、多模態手寫與通訊紀錄、單頁美化照護 PDF 等）。

### ⚡ 學員如何一鍵下載專案？
安裝好 Starter Pack 後，學員只需在 Antigravity 2.0 對話框中輸入：

```text
下載專案
```
*(或「下載練習專案」、「建立練習專案」)*

Antigravity 2.0 就會自動在當前電腦目錄建立 `AI-Practice-Project/` 專案資料夾，自動載入真實情境教材，並產生包含 4 大挑戰的 `README.md`！

### 🎯 練習專案 4 大實戰任務：
1. **任務一（基礎 Excel 查詢）**：用 `/xlsx` 篩選 HbA1c > 8.0% 且慢箋即將到期之高風險個案。
2. **任務二（多模態非結構化資料萃取與匯入）★ 核心多模態工作流**：解析 `病人紀錄/` 內的真實手寫日誌 PDF、LINE 對話截圖與手機記事本，自動萃取 9 月血壓血糖數值並結構化回寫至 Excel！
3. **任務三（專業照護摘要文檔批次產出）**：用 `/docx` 自動批次產生個人化單頁 Word 照護與衛教摘要報告。
4. **任務四（瑞士編輯風衛教簡報設計）**：用 `slide-simple` 一次選定風格版面，產生極簡高質感衛教簡報圖片。

---

## 🛠️ 備用手動安裝方式

如果您習慣在終端機操作，也可以透過以下兩種方式之一完成安裝：

### 方式 A：一鍵 Python 安裝腳本（跨平台）
```bash
git clone https://github.com/Timacrypt/antigravity2-starter-pack.git
cd antigravity2-starter-pack
python3 install.py
```

### 方式 B：手動複製目錄
1. 將本專案的 `skills/` 資料夾內所有子資料夾複製到：
   * macOS / Linux: `~/.gemini/config/skills/`
   * Windows: `%USERPROFILE%\.gemini\config\skills\`
2. 安裝 Python 辦公依賴：
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 內建技能庫一覽 (25 Curated Skills)

每個技能均配置專屬的視覺 Emoji 與圖示（支援 `metadata.icon` 與 `metadata.emoji`）：

### 1. 🎓 Matt Pocock 經典思維與協作流程技能組
讓您與 AI Agent 的溝通如同學長姊或資深工程師協作般嚴謹精準：

| 圖示 | 技能指令 / 目錄 | 核心功能說明 |
| :---: | :--- | :--- |
| 💡 | `/brainstorming` | 透過多輪互動探索需求，收斂點子並自動生成標準架構規格書（Spec）。 |
| 🎓 | `/teach` | 將當前工作區轉為教學環境，追蹤學習歷程，循序漸進教授新技術。 |
| 🔥 | `/grill-me` | 嚴格質詢您的計畫，主動找出潛在邏輯漏洞與邊界情境。 |
| 🥩 | `/grilling` | 無情質詢的底層核心引擎，以決策樹與分輪提問挖掘最深層的架構前提。 |
| 📑 | `/grill-with-docs` | 結合現有文檔與程式碼進行質詢，邊面試邊自動維護 `GLOSSARY.md` 與架構決策紀錄（ADR）。 |
| 🤔 | `/wait-what` | **【台灣特調版】** 當 AI 講得太深聽不懂時，以**台灣高一程度、生動生活比喻、繁體中文**重新解釋（專有名詞保留 English）。 |
| 🤝 | `/handoff` | 跨對話交接！將目前對話的背景與進度濃縮成交接 Markdown，讓下個 Agent 無縫接手。 |
| 📋 | `/to-questionnaire` | 當決策資訊不足時，自動將模糊問題轉成結構化的是非/單選問卷。 |
| ✍️ | `/writing-for-agents` | 指導您如何為 AI Agent 撰寫最佳 Prompt、Rules 與 Skill 定義。 |

---

### 2. ⚡ Matt Pocock 軟體工程與 Vibe Coding 實戰利器
專為直覺式開發與防呆設計打造，徹底告別「AI 瞎猜、越修越爛」的死循環：

| 圖示 | 技能指令 / 目錄 | 核心功能說明 |
| :---: | :--- | :--- |
| 🧭 | `/ask-matt` | **【AI 技能導航員】** 當您不知道現在該用什麼技能或下一步該做什麼時，只需用白話發問，它會自動為您導流推薦最佳工作流。 |
| 🐛 | `/diagnosing-bugs` | **【系統化抓蟲偵探】** 在沒有定位出真正的 Root Cause 與重現步驟前**嚴禁動手亂改代碼**，帶領您一步步精準定位並除錯。 |
| 🔍 | `/research` | **【第一手權威調研員】** 強制 AI 翻閱最新官方 First-party 文件與 API 規範，防止引用過時語法或憑空產生幻覺。 |
| ⚡ | `/prototype` | **【閃電原型打造機】** 拒絕過度設計！專注於以最小、最乾淨的拋棄式代碼（Throwaway Code）快速驗證業務邏輯或 UI 效果。 |
| 📐 | `/to-spec` | **【規格書合成器】** 將當前的對話共識與需求自動彙整成嚴謹、可交付的工程規格書（Spec），不進行額外面試。 |

---

### 3. 🎨 視覺美學、簡報設計與 Office 辦公系列（無瑕適配 Antigravity）
擺脫千篇一律的「AI 罐頭感」，兼顧頂尖 UI 視覺設計與全方位辦公文檔自動化：

| 圖示 | 技能名稱 | 核心功能說明 |
| :---: | :--- | :--- |
| 🎨 | **`slide-simple`** | **【Swiss 編輯風簡報設計】** 以一組字母快速決定排版風格、Layout、表達形式、插畫與副色，確認完整文字設計稿後才產生高質感投影片圖片。 |
| 🏢 | **`officecli`** | **【AI 專屬 Office 套件】** 單一二進位工具，支援以命令列直接讀寫 Word、Excel、PPT，內建即時 HTML/PNG 渲染預覽伺服器（`officecli watch`）。 |
| ✨ | **`frontend-design`** | **【Anthropic 前端美學】** 避免模板化與陳腔濫調，針對主題提供獨特的調色盤、字體排版、視覺層次與現代佈局。 |
| 📄 | **`docx`** | 生成排版優美的 Word 報告（標題樣式、表格、頁眉頁腳、目錄），解析既有 Word 文檔與追蹤修訂。 |
| 📊 | **`xlsx`** | 建立專業 Excel 財務/數據試算表，內建公式運算、數據透視分析與格式設定。 |
| 📽️ | **`pptx`** | 自動生成簡報投影片，配置現代化版面與圖文方塊。 |
| 📕 | **`pdf`** | 精準萃取 PDF 內的文字與表格，並能生成結構化摘要與報告。 |

> 💡 **環境自修復保證**：Document 系列已內建 Python 自動偵測機制，若電腦缺少 `python-docx` 或 `openpyxl`，Agent 在執行時會自動一鍵補裝，絕不報錯中斷！

---

### 4. 🛎️ 選擇性進階安裝引導（On-Demand 按需呼叫）
專為零技術背景、不會操作終端機的學員打造的保母級指引。**平常對話中 AI 不會主動推銷或打擾**，僅在學員主動提出需求時觸發：

| 圖示 | 觸發語句 / 技能名稱 | 核心引導特色（專為台灣新手設計） |
| :---: | :--- | :--- |
| 🌐 | 「Google Workspace MCP 安裝」<br>`setup-google-workspace-mcp` | **【完全無腦看圖點擊】** 聚焦 Google Drive、Sheets、Docs 三大服務。提供直達官方連結、畫面按鈕方位與中英對照，帶您一步步完成 OAuth 憑證設置並破解安全警告。 |
| 💻 | 「OpenCode 安裝」<br>`setup-opencode` | **【學員免開終端機】** 引導學員在網頁一鍵註冊 OpenCode 並取得 Zen 免費 API Key；學員無需親自開黑底終端機，由 AI Agent 在後台代勞執行安裝與金鑰綁定！ |

---

### 5. 🛠️ 生態擴充技能組
| 圖示 | 技能名稱 | 核心功能說明 |
| :---: | :--- | :--- |
| 🛠️ | **`skill-creator`** | 引導您從零設計、編寫並測試屬於您自己的全新 Antigravity Skill。 |
| 🌐 | **`find-skills`** | 快速搜尋並安裝開源社群中的各類優秀 Agent Skills。 |

---

### 6. 🔌 外部工具與 MCP 整合 (Tools & MCP)
* **Google Apps Script CLI (`clasp`)**：
  * 支援直接在本地終端管理 Google 試算表/文件/表單的自動化腳本。
  * 執行 `npm i -g @google/clasp` 即可安裝，搭配 `clasp login` 即可開始使用。
* **NotebookLM MCP**：
  * 連接 Google NotebookLM（notebook.google.com），讓 Antigravity 2.0 擁有存取您私人知識庫、新增來源與生成 Studio 音訊/投影片的能力。
  * 授權方式只需在終端執行 `nlm login` 即可完成 Google 帳號綁定。

---

## ✏️ 初學者如何自行編輯與客製技能？

本 Repo 所有技能均遵循開源標準 Markdown 格式：
1. 進入 `skills/<技能名稱>/SKILL.md`。
2. 您可以在 YAML 區域修改觸發條件或圖示（`metadata.emoji` / `metadata.icon`），或直接在內文修改給 AI 的提示詞（Prompt）。
3. 儲存檔案後，Antigravity 2.0 就會即時套用您的最新修改，不需編譯或重啟！

---

## 📜 授權協議 (License)

本專案採用 **MIT License** 開源釋出。  
特別致敬並感謝：
* [Matt Pocock](https://github.com/mattpocock/skills) 貢獻之 Agent 思維與工程實戰技能庫。
* [Anthropic](https://github.com/anthropics/skills) 貢獻之前端設計美學與辦公文檔處理規範。
