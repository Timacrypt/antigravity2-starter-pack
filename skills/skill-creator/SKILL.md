---
name: skill-creator
description: "建立新技能：引導你一步一步設計、編寫並驗證新的 Agent 技能。"
metadata:
  icon: "🛠️"
  emoji: "🛠️"
---

# Skill Creator (技能設計與建置專家)

此技能指引 Agent 與使用者互動，將工作流程、業務邏輯或外部工具封裝為標準、高效且符合規範的 Agent Skill。

---

## 核心設計原則 (Design Principles)

1. **漸進式揭露 (Progressive Disclosure)**：
   - `SKILL.md` 應保持精簡（建議 500～1500 字元核心指令），專注於流程決策與操作步驟。
   - 冗長的規格、API 手冊或複雜說明應拆解放入 `references/` 目錄，僅在需要時讀取。
2. **觸發描述至關重要 (Trigger Optimization)**：
   - YAML frontmatter 中的 `description` 是 Agent 決定是否啟動此技能的唯一依據。必須清楚說明「要做什麼」以及「何時觸發（Use when...）」。
3. **程式碼優先採 CLI 模式 (CLI Helper Pattern)**：
   - 凡涉及外部 API、資料轉換、檔案讀寫等程式性邏輯，優先封裝至 `scripts/` 下的 Python CLI 腳本（使用 stdlib 與 `argparse`）。
   - 純引導或邏輯推斷類任務才使用純文字 instruction。
4. **命名與路徑標準**：
   - Skill 名稱必須為小寫連字號（例如：`github-pr-analyzer`）。
   - 全域安裝路徑：`~/.gemini/config/skills/<skill-name>/`
   - 專案工作區安裝路徑：`.agents/skills/<skill-name>/`

---

## 標準目錄結構

```text
<skill-name>/
├── SKILL.md                 # 必填：YAML frontmatter + 核心工作流與規則
├── scripts/                 # 選填：Python 腳本 (使用 uv run 執行)
│   └── helper.py
├── references/              # 選填：長篇文件、API 規格、字典對照
│   └── guide.md
├── resources/               # 選填：靜態資源、樣板檔案
└── examples/                # 選填：使用範例與預期產出
```

---

## 建置流程 (Step-by-Step Workflow)

### 階段一：需求訪談與範圍確認 (Scoping & Brainstorming)
與使用者對話釐清以下要點（每次提出 2-3 個核心問題）：
1. **目標與觸發情境**：這個技能要解決什麼問題？使用者通常會輸入什麼指令來召喚它？
2. **輸入與輸出**：需要使用者提供哪些參數或檔案？期望產出什麼格式（Markdown、JSON、圖表）？
3. **是否需要輔助腳本**：是否需要調用外部 API 或處理檔案？（若需要，定義需要的子命令）。
4. **安裝層級**：建議安裝為**專案專用**（`.agents/skills/`）還是**全域通用**（`~/.gemini/config/skills/`）？

### 階段二：設計與架構確認 (Design & Plan)
在動手寫檔前，向使用者提出包含以下內容的簡要確認：
- 技能名稱（`kebab-case`）
- Frontmatter `description` 內容
- 目錄結構與檔案清單
- 核心步驟綱要

### 階段三：實作與生成 (Implementation)
1. **建立目錄結構**：建立對應資料夾。
2. **撰寫 `SKILL.md`**：
   - 必須包含完整的 YAML frontmatter（`name` 與 `description`）。
   - 明確定義工作流程、各步驟的邊界條件、失敗復原策略。
3. **撰寫 Helper Scripts (若有)**：
   - 參考 [cli_script_template.py](references/cli_script_template.py)。
   - 使用標準庫（stdlib），避免不必要的第三方相依。
   - 所有子命令強制輸出至指定檔案（`--output`）。
   - 內建 Rate Limiting 與重試機制（Exponential Backoff）。

### 階段四：驗證與自我檢查 (Validation Checklist)
完成後逐一確認：
- [ ] `name` 是否符合小寫連字號規範？
- [ ] `description` 是否包含明確的「何時使用」與關鍵字？
- [ ] 是否落實 Progressive Disclosure（細部文件外移至 `references/`）？
- [ ] 腳本是否能獨立正常執行？
