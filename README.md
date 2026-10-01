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

### 1. 🎓 思維與協作流程技能組
| 圖示 | 技能指令 / 目錄 | 核心功能說明 |
| :---: | :--- | :--- |
| 💡 | `/brainstorming` | **腦力激盪**：在開始實作前，探索需求與設計方向，並整理成具體規格。 |
| 🎓 | `/teach` | **教學引導**：在當前專案中設定學習目標，循序漸進引導你學習新技能或概念。 |
| 🔥 | `/grill-me` | **追問**：透過持續提問與對話，深入檢視並完善你的計畫或設計。 |
| 🥩 | `/grilling` | **嚴格追問**：針對計畫、決策或想法進行連續深入提問，找出思考盲點。 |
| 📑 | `/grill-with-docs` | **文檔追問**：透過持續提問完善計畫，並同步記錄架構決策（ADR）、規格與術語。 |
| 🤔 | `/wait-what` | **等等沒聽懂**：以生活比喻和白話重新解釋剛才的內容，專有名詞保留 English。 |
| 🤝 | `/handoff` | **交接紀錄**：將目前的對話與工作進度整理成交接文件，讓下一個 Agent 接續進行。 |
| 📋 | `/to-questionnaire` | **轉為問卷**：當問題資訊不足以做決定時，整理成結構化問卷供他人填寫。 |
| ✍️ | `/writing-for-agents` | **Agent 文件撰寫**：指導如何撰寫 Agent 使用的提示詞、規則文件與技能說明。 |

---

### 2. ⚡ 軟體工程與開發實戰利器
| 圖示 | 技能指令 / 目錄 | 核心功能說明 |
| :---: | :--- | :--- |
| 🧭 | `/ask-matt` | **技能推薦**：根據你目前的狀況與需求，推薦最適合使用的技能或工作流程。 |
| 🐛 | `/diagnosing-bugs` | **診斷錯誤**：排查難解的程式錯誤與效能問題，在確認根本原因前不盲目修改。 |
| 🔍 | `/research` | **資料調研**：查詢官方權威文檔與資料來源，調查問題並記錄整理調查結果。 |
| ⚡ | `/prototype` | **快速原型**：用最小程式碼快速建立概念驗證原型，確認設計或功能邏輯。 |
| 📐 | `/to-spec` | **轉為規格書**：將當前對話中的討論與共識，整理成標準的工程規格書。 |

---

### 3. 🎨 視覺美學、簡報設計與 Office 辦公系列
| 圖示 | 技能名稱 | 核心功能說明 |
| :---: | :--- | :--- |
| 🎨 | **`slide-simple`** | **簡報圖片設計**：以簡潔設定選定排版風格與插畫，確認文字稿後生成投影片圖片。 |
| 🏢 | **`officecli`** | **Office 命令列工具**：使用 officecli 工具讀寫與修改 Office 文件，並支援即時預覽。 |
| ✨ | **`frontend-design`** | **前端視覺設計**：在建立或調整網頁介面時，提供精緻的版面配置、字體與色彩建議。 |
| 📄 | **`docx`** | **Word 文件**：建立、編輯、分析與排版 Microsoft Word (.docx) 文件與報告。 |
| 📊 | **`xlsx`** | **Excel 試算表**：建立、讀取、編輯、分析與格式化 Microsoft Excel (.xlsx) 試算表。 |
| 📽️ | **`pptx`** | **PowerPoint 簡報**：建立、編輯、分析與排版 Microsoft PowerPoint (.pptx) 簡報。 |
| 📕 | **`pdf`** | **PDF 文件**：擷取文字與表格、合併拆分、分析與處理 PDF 文件。 |

> 💡 **環境自修復保證**：Document 系列已內建 Python 自動偵測機制，若電腦缺少 `python-docx` 或 `openpyxl`，Agent 在執行時會自動一鍵補裝，絕不報錯中斷！

---

### 4. 🛎️ 選擇性進階安裝引導（On-Demand 按需呼叫）
專為零技術背景、不會操作終端機的學員打造的保母級指引。**平常對話中 AI 不會主動推銷或打擾**，僅在學員主動提出需求時觸發：

| 圖示 | 觸發語句 / 技能名稱 | 核心引導特色（專為台灣新手設計） |
| :---: | :--- | :--- |
| 🌐 | 「Google Workspace MCP 安裝」<br>`setup-google-workspace-mcp` | **Google Workspace MCP 安裝**：一步一步引導開啟雲端硬碟、試算表與文件 API 並設定憑證（按需使用）。 |
| 💻 | 「OpenCode 安裝」<br>`setup-opencode` | **OpenCode 安裝**：引導取得 Zen 免費金鑰，並由 AI 在後台代為安裝與設定 OpenCode（按需使用）。 |

---

### 5. 🛠️ 生態擴充技能組
| 圖示 | 技能名稱 | 核心功能說明 |
| :---: | :--- | :--- |
| 🛠️ | **`skill-creator`** | **建立新技能**：引導你一步一步設計、編寫並驗證新的 Agent 技能。 |
| 🌐 | **`find-skills`** | **搜尋技能**：協助尋找並安裝開源社群中的各類 Agent 技能。 |

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
