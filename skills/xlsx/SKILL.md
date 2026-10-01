---
name: xlsx
description: "Excel 試算表：建立、讀取、編輯、分析與格式化 Microsoft Excel (.xlsx) 試算表。"
metadata:
  icon: "📊"
  emoji: "📊"
---

# xlsx: Excel Spreadsheet Processing Skill for Antigravity 2.0

This skill enables Antigravity 2.0 to create, read, edit, and analyze Microsoft Excel (`.xlsx`) files with formulas, styling, column widths, number formatting, and multi-sheet workbooks.

---

## 🛠️ Dependency Self-Healing (執行前環境檢查)

Before running Excel operations, ensure `openpyxl` is installed.
In your Python script or terminal:
```python
import subprocess, sys
try:
    import openpyxl
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    import openpyxl
```

---

## 🚀 Core Capabilities

1. **Create Structured Spreadsheets**:
   - Multiple sheets (Tabs) with meaningful names.
   - Header formatting (fill color, bold text, centered alignment).
   - Dynamic formulas (e.g. `=SUM(B2:B10)`, `=AVERAGE(...)`, `=IF(...)`).
   - Number formatting (currency, percentages, date/time, decimals).
   - Auto-fitting column widths.
2. **Read & Analyze Existing Spreadsheets**:
   - Read cell values, raw data, or computed formula results (`data_only=True`).
   - Extract sheets as tabular data for fast AI analysis.
3. **Modify Existing Workbooks**:
   - Update specific cell ranges without destroying existing charts or formulas.

---

## 📝 Example Python Workflow

### Creating an Excel Model with Formulas & Styling:
```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "季度財務摘要"

# Headers
headers = ["項目 (Item)", "Q1 (NT$)", "Q2 (NT$)", "Q3 (NT$)", "Q4 (NT$)", "總計 (Total)"]
ws.append(headers)

# Header Style
header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
for col_num in range(1, len(headers) + 1):
    cell = ws.cell(row=1, column=col_num)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center")

# Rows Data
rows = [
    ["軟體訂閱收入", 120000, 145000, 160000, 190000],
    ["專業諮詢服務", 80000, 95000, 85000, 110000],
    ["雲端運算成本", -35000, -42000, -48000, -55000],
]

for row_idx, row_data in enumerate(rows, start=2):
    ws.append(row_data + [f"=SUM(B{row_idx}:E{row_idx})"])

# Total Row
last_row = len(rows) + 2
ws.append(["淨額總計", f"=SUM(B2:B{last_row-1})", f"=SUM(C2:C{last_row-1})", f"=SUM(D2:D{last_row-1})", f"=SUM(E2:E{last_row-1})", f"=SUM(F2:F{last_row-1})"])

total_font = Font(name="Arial", size=11, bold=True)
for col_num in range(1, 7):
    c = ws.cell(row=last_row, column=col_num)
    c.font = total_font

# Auto-adjust column width
for col in ws.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws.column_dimensions[col_letter].width = max(max_len + 5, 12)

wb.save("financial_summary.xlsx")
print("✅ Excel 檔案已儲存至 financial_summary.xlsx")
```
