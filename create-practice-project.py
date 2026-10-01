#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
10/02 AI 教學 - 實戰練習專案一鍵建立腳本 (Practice Project Generator)
自動將 practice-materials/ 資料複製到目標目錄，並生成包含多模態工作流任務的 README.md。
"""

import os
import sys
import shutil

PRACTICE_README_CONTENT = """# 🩺 10/02 AI 教學：糖尿病照護與多模態 AI Agent 實戰練習專案

歡迎來到 **10/02 AI Agent 實戰教學練習專案**！  
本專案專為配合 **Antigravity 2.0 Agent Starter Pack** 打造，結合臨床真實工作情境，讓您透過 AI Agent 體驗從「試算表數據分析」、「非結構化多模態資料萃取」、「報告批次生成」到「衛教視覺簡報」的完整工作流。

---

## ⚠️ 重要免責聲明與資料背景 (Disclaimer)

1. **純屬虛構**：本專案內所有個案資料（包括姓名、身分證號、病歷號碼、聯絡電話、地址、Email、檢驗數值、文字紀錄、手寫紀錄及通訊對話）**均為純屬虛構之教學範例**。
2. **無真實個資**：任何與真實人物、地點或事件之相似處純屬巧合。
3. **非醫療決策依據**：本資料集僅供 AI Agent 學習、Prompt 工程測試與自動化多模態工作流操作練習，**嚴禁作為真實臨床醫療診斷或病人照護之依據**。

---

## 📂 專案檔案清單 (Project Manifest)

```text
AI-Practice-Project/
├── README.md                                          # 本練習說明書與任務清單
├── 糖尿病個案2026年8月.xlsx                           # 核心試算表（個案追蹤 24 列 21 欄 + 8月每日紀錄）
├── 糖尿病患者個人檔案與照護紀錄_單頁美化版.pdf        # 單頁專業照護報告參考範本
└── 病人紀錄/                                         # 真實情境多元非結構化紀錄
    ├── 林怡君_2026年9月手機記事本紀錄.txt             # 純文字生活記事紀錄
    ├── 陳志明_2026年9月手機記事本紀錄.txt             # 純文字生活記事紀錄
    ├── 李美玲_2026年9月LINE對話截圖紀錄.pdf          # 聊天通訊對話截圖
    └── 2026年9月_兩位虛構個案_手寫血糖血壓紀錄.pdf   # 紙本手寫日誌掃描檔
```

---

## 🎯 4 大核心實戰練習任務導引

請在您的 Antigravity 2.0 對話框中直接對 AI 下達自然語言指令，依序完成以下 4 項挑戰：

### 🎯 任務一：結構化數據查詢與高風險篩選 (Excel Analysis)
* **練習目標**：熟悉結構化試算表分析與條件篩選。
* **任務內容**：
  請 AI Agent 調用 `/xlsx` 技能讀取 `糖尿病個案2026年8月.xlsx`：
  1. 找出 **糖化血色素 HbA1c > 8.0%** 的所有個案。
  2. 檢查其「慢箋到期日」與「下次抽血預定日」，篩選出即將在一個月內到期需回診追蹤的名單。
  3. 列出每位個案的病歷號、姓名、最近血糖、HbA1c 與目前用藥，整理成清晰的追蹤清單。
* **推薦指令範例**：
  > 「請幫我讀取 `糖尿病個案2026年8月.xlsx`，篩選出 HbA1c 大於 8.0 的病人，並列出他們的慢箋到期日與用藥。」

---

### 🎯 任務二：多元非結構化資料多模態萃取與匯入 (Multimodal Ingestion) ★ 核心亮點！
* **練習目標**：體驗 AI Agent 的**多模態（Multimodal）工作流**——從雜亂的手機筆記、通訊軟體截圖與手寫掃描檔中萃取關鍵臨床數值，並回寫至 Excel。
* **任務內容**：
  在 `病人紀錄/` 資料夾中包含 4 位個案在 2026 年 9 月份的雜亂日常紀錄：
  * `林怡君_2026年9月手機記事本紀錄.txt`
  * `陳志明_2026年9月手機記事本紀錄.txt`
  * `李美玲_2026年9月LINE對話截圖紀錄.pdf`
  * `2026年9月_兩位虛構個案_手寫血糖血壓紀錄.pdf`
  請讓 AI Agent 透過多模態影像與文字辨識：
  1. 解析出每位病人的 **9 月份血壓平均值、空腹血糖值、餐後血糖、自述不適症狀與用藥依從性**。
  2. 自動將這些結構化後的 9 月數據，新增至 `糖尿病個案2026年8月.xlsx` 的新工作表（例如 `2026年9月追蹤匯入`）或補充至個案追蹤紀錄中。
* **推薦指令範例**：
  > 「請讀取 `病人紀錄/` 裡的所有檔案（包含手寫 PDF 與 LINE 截圖），幫我辨識出這幾位病人 9 月份的血壓、血糖數值與生活備註，整理成表格並追加匯入到 `糖尿病個案2026年8月.xlsx` 的新工作表中。」

---

### 🎯 任務三：個人化專業照護報告批次生成 (Word Document Generation)
* **練習目標**：學習自動化文檔生成與版面排版。
* **任務內容**：
  參考 `糖尿病患者個人檔案與照護紀錄_單頁美化版.pdf` 的版面風格與結構：
  1. 調用 `/docx` 技能，為剛才篩選出的高風險個案或 9 月有追蹤數據的個案，自動產生專業的單頁 Word 照護報告（`.docx`）。
  2. 文檔內需包含基本檔案、檢驗數據對比表格、警示標籤與醫師衛教建議欄位。
* **推薦指令範例**：
  > 「請參考 `糖尿病患者個人檔案與照護紀錄_單頁美化版.pdf` 的版面，調用 `/docx` 為林怡君產出一份 2026 年 9 月的個人照護摘要 Word 報告。」

---

### 🎯 任務四：瑞士編輯風衛教簡報與視覺圖片產出 (Visual Slide Design)
* **練習目標**：掌握無 AI 罐頭感的簡報排版與生圖引導。
* **任務內容**：
  1. 調用 `slide-simple` 技能，針對「糖尿病患者的低血糖自救指南」或「飲食三少一多守則」進行投影片設計。
  2. 透過一組字母（例如 `A B C A B`）一次決定 Swiss 編輯風格、Layout、插畫畫風與副色。
  3. 確認完整文字設計稿後產出高質感的衛教簡報圖片。
* **推薦指令範例**：
  > 「我想調用 `slide-simple`，為剛才的糖尿病個案設計一張『預防低血糖：發抖、冒冷汗的緊急應變 3 步驟』瑞士風格衛教投影片圖片。」

---

## 🛠️ 本專案推薦調用之 Starter Pack 技能庫

| 圖示 | 技能指令 | 何時使用？ |
| :---: | :--- | :--- |
| 🧭 | `/ask-matt` | **迷航時呼叫**：不知道下一步該做什麼，或不知道該選哪個技能時，用白話詢問它。 |
| 📊 | `/xlsx` | **任務一與任務二**：讀取、篩選、計算與回寫 Excel 試算表。 |
| 📄 | `/docx` | **任務三**：自動化建立與排版專業 Word 醫療報告。 |
| 🎨 | `slide-simple` | **任務四**：一次決定風格與版面，生成極簡瑞士風衛教簡報圖片。 |
| 🐛 | `/diagnosing-bugs` | **遇到報錯時**：如果腳本執行錯誤或檔案讀取失敗，強制 AI 系統化排查，不瞎猜。 |
| 🤔 | `/wait-what` | **名詞聽不懂時**：遇到臨床數值（如 eGFR, UACR）或程式專有名詞時，用生活比喻白話重述。 |
"""

def create_practice_project(target_dir="AI-Practice-Project"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_materials = os.path.join(base_dir, "practice-materials")
    
    if not os.path.exists(source_materials):
        print(f"❌ 錯誤：找不到來源教材目錄 {source_materials}")
        return False
        
    abs_target = os.path.abspath(target_dir)
    print(f"🚀 正在建立練習專案於：{abs_target} ...")
    os.makedirs(abs_target, exist_ok=True)
    
    # 複製教材資料
    for item in os.listdir(source_materials):
        src_path = os.path.join(source_materials, item)
        dst_path = os.path.join(abs_target, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            print(f"  ✓ 已複製目錄: {item}/")
        elif os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"  ✓ 已複製檔案: {item}")
            
    # 寫入 README.md
    readme_path = os.path.join(abs_target, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(PRACTICE_README_CONTENT.strip() + "\n")
    print(f"  ✓ 已生成練習專案說明書: README.md")
    
    print("\n" + "=" * 65)
    print("🎉 恭喜！10/02 AI 教學練習專案已成功建立！")
    print(f"專案路徑：{abs_target}")
    print("您現在可以打開該目錄，並在 Antigravity 2.0 中開始執行任務一至任務四！")
    print("=" * 65)
    return True

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "AI-Practice-Project"
    create_practice_project(target)
