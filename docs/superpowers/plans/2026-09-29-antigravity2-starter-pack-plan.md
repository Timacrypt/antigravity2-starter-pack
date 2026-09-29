# Antigravity 2.0 Starter Pack - Implementation Plan

* **Date**: 2026-09-29
* **Spec**: [`docs/superpowers/specs/2026-09-29-antigravity2-starter-pack-design.md`](../specs/2026-09-29-antigravity2-starter-pack-design.md)
* **Status**: In Progress

---

## 1. Goal (目標)
建立完整的 `antigravity2-starter-pack` 資料夾架構，包含：
1. 專為 Antigravity 2.0 撰寫的自動安裝引導（`AGENTS.md` 與 `README.md`）。
2. 7 個 Matt Pocock 經典技能（含繁中高一特調版 `wait-what`）。
3. 4 個 Anthropic Document 辦公技能（`docx`, `xlsx`, `pptx`, `pdf`）及輔助腳本。
4. 2 個生態擴充技能（`skill-creator`, `find-skills`）。
5. 2 套工具/MCP 整合教學與設定（`clasp` 與 `NotebookLM MCP`）。
6. 跨平台一鍵安裝腳本（`install.py`）與 MIT 授權文檔。

---

## 2. Tasks & Phases (實作階段與工作項目)

### Phase 1: 專案基礎與自動安裝系統 (Repository Foundation)
- [x] **Task 1.1**: 建立專案目錄 `antigravity2-starter-pack/`。
- [x] **Task 1.2**: 撰寫 `requirements.txt`（包含 `python-docx`, `openpyxl`, `python-pptx`, `pypdf`, `pymupdf`）。
- [x] **Task 1.3**: 撰寫 `LICENSE`（MIT 授權，註明 Matt Pocock 與 Anthropic 原創致敬）。
- [x] **Task 1.4**: 撰寫 `AGENTS.md`（Antigravity 2.0 專用安裝協議）。
- [x] **Task 1.5**: 撰寫 `README.md`（繁體中文新手說明書、一鍵複製 Prompt、自訂編輯指南）。
- [x] **Task 1.6**: 撰寫 `install.py`（跨平台備用安裝腳本，自動偵測 `~/.gemini/config/skills/` 與依賴安裝）。

### Phase 2: Matt Pocock 經典技能組 (7 Skills)
- [x] **Task 2.1**: 移植 `brainstorming`（含 `SKILL.md` 與 `visual-companion.md`）。
- [x] **Task 2.2**: 移植 `teach`（含 `SKILL.md`、`MISSION-FORMAT.md`、`RESOURCES-FORMAT.md`、`LEARNING-RECORD-FORMAT.md`）。
- [x] **Task 2.3**: 移植 `grill-me`（含 `SKILL.md`）。
- [x] **Task 2.4**: 客製撰寫 **特調版 `wait-what`**（繁中 zhtw、台灣高一程度、生活比喻、專有名詞保留 English）。
- [x] **Task 2.5**: 移植 `handoff`（含 `SKILL.md`）。
- [x] **Task 2.6**: 移植 `to-questionnaire`（含 `SKILL.md`）。
- [x] **Task 2.7**: 移植 `writing-for-agents`（含 `SKILL.md` 與 `SKILL-MECHANICS.md`）。

### Phase 3: Anthropic Document 辦公技能組 (4 Skills + Scripts)
- [x] **Task 3.1**: 實作 `docx` Skill（`SKILL.md` + `scripts/helper_docx.py`，支援自修復依賴檢查）。
- [x] **Task 3.2**: 實作 `xlsx` Skill（`SKILL.md` + `scripts/helper_xlsx.py`，支援公式計算與試算表結構）。
- [x] **Task 3.3**: 實作 `pptx` Skill（`SKILL.md` + `scripts/helper_pptx.py`，支援簡報生成與排版）。
- [x] **Task 3.4**: 實作 `pdf` Skill（`SKILL.md` + `scripts/helper_pdf.py`，支援文字與表格萃取）。

### Phase 4: 生態擴充技能組 (2 Skills)
- [x] **Task 4.1**: 移植 `skill-creator`（含 `SKILL.md` 與參考文檔）。
- [x] **Task 4.2**: 移植 `find-skills`（含 `SKILL.md`）。

### Phase 5: 外部工具與 MCP 整合 (Tools & MCP)
- [x] **Task 5.1**: 建立 `mcp-and-tools/clasp/`（含 `README.md` 操作手冊與 `setup-clasp.sh` 一鍵安裝腳本）。
- [x] **Task 5.2**: 建立 `mcp-and-tools/notebooklm/`（含 `README.md`、`instructions.md` 與 `mcp-config.example.json`）。

### Phase 6: 驗證與交付 (Verification & Delivery)
- [x] **Task 6.1**: 驗證所有 `SKILL.md` 的 YAML Frontmatter 與語法正確性。
- [x] **Task 6.2**: 測試 `install.py` 的路徑偵測與複製邏輯。
- [x] **Task 6.3**: 驗證特調版 `wait-what` 的 Prompt 結構。
- [x] **Task 6.4**: 整理 GitHub Repo 上傳指南（`git init`, `git add`, `git commit`, `git remote add`），方便使用者一鍵推送到自己的 GitHub。
