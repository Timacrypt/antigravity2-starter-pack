# Antigravity 2.0 Agent Starter Pack - Design Specification

* **Date**: 2026-09-29
* **Target Audience**: AI Agent 初學者、Antigravity 2.0 使用者
* **Target Platform**: Google Antigravity 2.0 (macOS, Windows, Linux)
* **Status**: Proposed / Under Review

---

## 1. Executive Summary (執行摘要)

本專案旨在建立一個開源、免費、高性能的 GitHub Repository（`antigravity2-starter-pack`）。
使用者只需將該 Repo 網址提供給自己的 Antigravity 2.0 Agent，Agent 即會自動閱讀 Repo 內的 `AGENTS.md` 規範，將精選的 11 個核心 Skills、clasp CLI 工具與 NotebookLM MCP 完整安裝到使用者的 Antigravity 2.0 本機環境中。

---

## 2. Core Goals & Constraints (核心目標與約束)

### 2.1 核心目標 (Goals)
1. **零門檻自動安裝**：新手在 Antigravity 2.0 中輸入一句話即可自動完成安裝與配置。
2. **開箱即用與易編輯**：所有 Skill 與 MCP 設定均為乾淨、標準的 Markdown / JSON / Python，初學者下載後可隨時微調與編輯。
3. **無瑕運行 (Flawless Execution)**：全面適配 Antigravity 2.0 的執行環境，包含 YAML Frontmatter 規範、Python 相依性自動檢查與補齊、腳本開箱即用。
4. **專屬特調 `wait-what`**：當指令未達預期或概念艱澀時，以「台灣高一程度（10th grade level in Taiwan）」、繁體中文（zhtw）、生活化比喻重新解釋，專有名詞保留 English。

### 2.2 約束與技術標準 (Constraints)
* **語言規範**：文檔與說明一律使用繁體中文（zhtw），技術術語保留 English。
* **路徑規範**：
  * 全域 Skills 目錄：`~/.gemini/config/skills/<skill-name>/`
  * 全域 MCP 目錄：`~/.gemini/antigravity/mcp/<server-name>/`
* **授權原則**：MIT License，並對 Matt Pocock 與 Anthropic 原創專案提供明確 Attribution。

---

## 3. Included Components (收錄清單)

### 3.1 🎓 Matt Pocock 系列 Skills (思維與協作流程)
1. **`brainstorming`**：引導需求探索、方案評估、分段設計到規格書產出。
2. **`teach`**：將工作區轉化為教學空間，建立 `MISSION.md` 與 `learning-records` 循序授課。
3. **`grill-me`**：透過多輪深度提問質詢使用者的計畫，排查邏輯漏洞與邊界情境。
4. **`wait-what` (客製特調版)**：
   * 語言：繁體中文（zhtw），專有名詞保留 English。
   * 程度：台灣高中一年級（10th grade）水準。
   * 形式：一句話核心重點 + 貼近生活的情境比喻 + 核心概念拆解 + 下一步行動。
5. **`handoff`**：將當前會話狀態濃縮成交接 Markdown 文檔，讓後續 Agent 接續工作。
6. **`to-questionnaire`**：將開放式架構或業務決策拆解為結構化問卷。
7. **`writing-for-agents`**：為 AI Agent 撰寫清晰文檔、規範與 Skill 的指導方針。

### 3.2 📄 Anthropic Document 系列 Skills (辦公文檔處理)
8. **`docx`**：Microsoft Word 文檔生成、格式排版、樣式套用、批註與內容解析。
9. **`xlsx`**：Microsoft Excel 試算表生成、公式計算、數據分析與工作表管理。
10. **`pptx`**：Microsoft PowerPoint 簡報建立、版面配置、文字方塊與圖表組織。
11. **`pdf`**：PDF 文字萃取、表格解析、格式化分析與報告產出。

### 3.3 🛠️ 生態擴充系列 Skills
12. **`skill-creator`**：引導初學者從零建立自己的 Antigravity Skill。
13. **`find-skills`**：探索與安裝開源社群中的優質 Agent Skills。

### 3.4 🔌 外部工具與 MCP 整合 (Tools & MCP)
1. **Google Apps Script CLI (`clasp`)**：
   * 提供一鍵式安裝腳本（`npm install -g @google/clasp`）。
   * 初學者操作教學（`clasp login`、`clasp clone`、`clasp push`）。
2. **NotebookLM MCP**：
   * Antigravity 2.0 專用 MCP 配置範本與工具定義。
   * `nlm login` 授權指引（讀取筆記本、新增來源、生成 Audio/Studio 內容）。

---

## 4. Repository File Structure (專案目錄結構)

```text
antigravity2-starter-pack/
├── README.md                      # 繁中新手說明書與一鍵安裝提示詞
├── AGENTS.md                      # 寫給 Antigravity 2.0 的全自動安裝規範
├── LICENSE                        # MIT License
├── requirements.txt               # Document 系列所需 Python 套件
├── install.py                     # 本機跨平台一鍵安裝 Python 腳本
├── skills/
│   ├── brainstorming/
│   │   ├── SKILL.md
│   │   └── visual-companion.md
│   ├── teach/
│   │   ├── SKILL.md
│   │   ├── MISSION-FORMAT.md
│   │   ├── RESOURCES-FORMAT.md
│   │   └── LEARNING-RECORD-FORMAT.md
│   ├── grill-me/
│   │   └── SKILL.md
│   ├── wait-what/
│   │   └── SKILL.md               # 台灣高一繁中特調版
│   ├── handoff/
│   │   └── SKILL.md
│   ├── to-questionnaire/
│   │   └── SKILL.md
│   ├── writing-for-agents/
│   │   ├── SKILL.md
│   │   └── SKILL-MECHANICS.md
│   ├── docx/
│   │   ├── SKILL.md
│   │   └── scripts/helper_docx.py
│   ├── xlsx/
│   │   ├── SKILL.md
│   │   └── scripts/helper_xlsx.py
│   ├── pptx/
│   │   ├── SKILL.md
│   │   └── scripts/helper_pptx.py
│   ├── pdf/
│   │   ├── SKILL.md
│   │   └── scripts/helper_pdf.py
│   ├── skill-creator/
│   │   ├── SKILL.md
│   │   └── references/
│   └── find-skills/
│       └── SKILL.md
└── mcp-and-tools/
    ├── clasp/
    │   ├── README.md
    │   └── setup-clasp.sh
    └── notebooklm/
        ├── README.md
        ├── instructions.md
        └── mcp-config.example.json
```

---

## 5. Technical Mechanics for Antigravity 2.0 (運作機制與技術細節)

### 5.1 自動安裝協議 (`AGENTS.md`)
當 Antigravity 2.0 收到使用者指示「請安裝這個 Repo 的技能」時：
1. **讀取 Repo 根目錄的 `AGENTS.md`**。
2. **複製 Skills**：
   * 檢查本機目錄 `~/.gemini/config/skills/`，若不存在則建立。
   * 將 `skills/` 下的各個技能資料夾完整複製至 `~/.gemini/config/skills/`。
3. **檢查 Python 依賴**：
   * 執行 `pip install -r requirements.txt`，確保 `python-docx`、`openpyxl`、`python-pptx`、`pypdf`、`pymupdf` 安裝完畢。
4. **設定 Tools 與 MCP**：
   * 檢查 Node.js 環境，執行 `npm install -g @google/clasp`。
   * 建立 `~/.gemini/antigravity/mcp/notebooklm/` 並配置相應設定檔與說明。
5. **回報安裝摘要**：向使用者回報已完成安裝的項目清單與使用方式。

### 5.2 自修復環境 (Self-healing Dependency Strategy)
在各個 Document Skill（`docx`、`xlsx`、`pptx`、`pdf`）的 `SKILL.md` 中，開頭均包含指令：
```python
# 執行前自動檢查套件，若缺失則自動安裝
import subprocess, sys
def ensure_package(pkg):
    try:
        __import__(pkg)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
```
確保 Antigravity 2.0 在執行文檔處理時，即使在全新電腦上也不會因為缺少套件而中斷報錯。

---

## 6. Verification and Testing (驗證與測試計畫)

1. **Frontmatter 格式驗證**：檢查所有 11 個 `SKILL.md` 的 YAML frontmatter 均符合規範且包含 `name`、`description`。
2. **`wait-what` 語義驗證**：驗證特調 prompt 是否明確要求繁體中文、台灣高一程度、生活比喻、專有名詞保留 English。
3. **Document 腳本驗證**：
   * `docx` 生成與讀取測試。
   * `xlsx` 試算表計算測試。
   * `pptx` 簡報投影片建立測試。
   * `pdf` 文本萃取測試。
4. **安裝腳本測試**：測試 `install.py` 與 `AGENTS.md` 引導流程，確認目錄建立與複製無誤。
