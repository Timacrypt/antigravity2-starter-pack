# 🚀 Antigravity 2.0 Agent Starter Pack

> 專為 **Google Antigravity 2.0** 打造的開源、免費、高性能 Agent 技能與工具懶人包。  
> 整合 **Matt Pocock 經典思維技能** ＋ **Anthropic 官方 Office 辦公系列** ＋ **clasp (Google Apps Script)** ＋ **NotebookLM MCP**。

---

## ⚡ 30 秒極速安裝（新手首選）

您不需要手動下載檔案或設定複雜路徑！只要打開您的 **Antigravity 2.0**，在對話框中貼上以下這段話（請將網址替換為您的 GitHub Repo 網址）：

```text
請閱讀這個 GitHub Repo：https://github.com/Timacrypt/antigravity2-starter-pack
並依照其中的 AGENTS.md 指引，將所有 Skills、clasp 與 NotebookLM MCP 自動安裝到我的 Antigravity 2.0 環境中。
```

Antigravity 2.0 就會自主讀取本專案、自動建立全域目錄（`~/.gemini/config/skills/`）、複製技能並安裝必要 Python 依賴！

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

## 📦 內建技能庫一覽 (Skills Manifest)

### 1. 🎓 Matt Pocock 經典思維技能組
讓您與 AI Agent 的溝通如同學長姊或資深工程師協作般嚴謹精準：

| 技能指令 | 核心功能說明 |
| :--- | :--- |
| `/brainstorming` | 透過多輪互動探索需求，收斂點子並自動生成標準架構規格書（Spec）。 |
| `/teach` | 將當前工作區轉為教學環境，追蹤學習歷程，循序漸進教授新技術。 |
| `/grill-me` | 嚴格質詢您的計畫，主動找出潛在邏輯漏洞與邊界情境。 |
| `/wait-what` | **【台灣特調版】** 當 AI 講得太深聽不懂時，以**台灣高一程度、生動生活比喻、繁體中文**重新解釋（專有名詞保留 English）。 |
| `/handoff` | 跨對話交接！將目前對話的背景與進度濃縮成交接 Markdown，讓下個 Agent 無縫接手。 |
| `/to-questionnaire` | 當決策資訊不足時，自動將模糊問題轉成結構化的是非/單選問卷。 |
| `/writing-for-agents` | 指導您如何為 AI Agent 撰寫最佳 Prompt、Rules 與 Skill 定義。 |

---

### 2. 📄 Anthropic 官方 Office 辦公系列（無瑕適配 Antigravity）
完整支援 Microsoft Office 與 PDF 檔案的建立、排版、計算與文字分析：

* **`docx`**：生成排版優美的 Word 報告（標題樣式、表格、頁眉頁腳、目錄），解析既有 Word 文檔與追蹤修訂。
* **`xlsx`**：建立專業 Excel 財務/數據試算表，內建公式運算、數據透視分析與格式設定。
* **`pptx`**：自動生成簡報投影片，配置現代化版面與圖文方塊。
* **`pdf`**：精準萃取 PDF 內的文字與表格，並能生成結構化摘要與報告。

> 💡 **環境自修復保證**：本系列已內建 Python 自動偵測機制，若電腦缺少 `python-docx` 或 `openpyxl`，Agent 在執行時會自動一鍵補裝，絕不報錯中斷！

---

### 3. 🛠️ 生態擴充技能組
* **`skill-creator`**：引導您從零設計、編寫並測試屬於您自己的全新 Antigravity Skill。
* **`find-skills`**：快速搜尋並安裝開源社群中的各類優秀 Agent Skills。

---

### 4. 🔌 外部工具與 MCP 整合 (Tools & MCP)
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
2. 您可以在 YAML 區域修改觸發條件，或直接在內文修改給 AI 的提示詞（Prompt）。
3. 儲存檔案後，Antigravity 2.0 就會即時套用您的最新修改，不需編譯或重啟！

---

## 📜 授權協議 (License)

本專案採用 **MIT License** 開源釋出。  
特別致敬並感謝：
* [Matt Pocock](https://github.com/mattpocock/skills) 貢獻之 Agent 思維架構。
* [Anthropic](https://github.com/anthropics/skills) 貢獻之辦公文檔處理規範。
