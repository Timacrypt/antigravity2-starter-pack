---
name: docx
description: "Create, edit, analyze, and format Microsoft Word (.docx) documents. Use when the user wants to generate reports, edit Word documents, extract text or tables from .docx, format headings, add tables, or handle Word files."
metadata:
  icon: "📄"
  emoji: "📄"
---

# docx: Word Document Processing Skill for Antigravity 2.0

This skill enables Antigravity 2.0 to create, read, edit, and format Microsoft Word (`.docx`) files with professional typography, headings, tables, and layouts.

---

## 🛠️ Dependency Self-Healing (執行前環境檢查)

Before running Word document operations, ensure `python-docx` is installed.
In your Python script or terminal:
```python
import subprocess, sys
try:
    import docx
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    import docx
```

---

## 🚀 Core Capabilities

1. **Create Professional Documents**:
   - Title, Subtitles, Headings (H1, H2, H3).
   - Paragraphs with bold, italic, font sizing, and color.
   - Bullet lists and numbered lists.
   - Styled data tables with header rows, borders, and alternating shading.
   - Page breaks and margins.
2. **Read & Extract Content**:
   - Extract raw text, paragraph by paragraph.
   - Extract tables into structured 2D arrays or Markdown tables.
3. **Modify Existing Documents**:
   - Append sections, insert tables, or replace target text blocks while preserving formatting.

---

## 📝 Example Python Workflow

### Creating a Word Report:
```python
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = docx.Document()

# Set standard 1-inch margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Title
title = doc.add_heading(level=0)
run = title.add_run("專案研究與分析報告")
run.font.name = "Arial"
run.font.size = Pt(22)
run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

# Subtitle / Metadata
p = doc.add_paragraph()
p.add_run("日期: 2026-09-29  |  作者: Antigravity AI").italic = True

# Heading 1
doc.add_heading("1. 執行摘要 (Executive Summary)", level=1)
doc.add_paragraph("本報告針對專案核心指標進行全面評估與梳理，以下為重點結論。")

# Add a styled table
table = doc.add_table(rows=1, cols=3)
table.style = 'Table Grid'
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "指標名稱 (Metric)"
hdr_cells[1].text = "數值 (Value)"
hdr_cells[2].text = "狀態 (Status)"

data = [
    ("回應延遲 (Latency)", "120ms", "優秀 (Good)"),
    ("準確率 (Accuracy)", "98.5%", "達標 (Pass)"),
]
for item in data:
    row_cells = table.add_row().cells
    for i in range(3):
        row_cells[i].text = item[i]

doc.save("output_report.docx")
print("✅ Word 報告已成功儲存至 output_report.docx")
```

### Reading an Existing Word Document:
```python
import docx

doc = docx.Document("input.docx")
full_text = []
for para in doc.paragraphs:
    if para.text.strip():
        full_text.append(para.text)

print("\n".join(full_text))
```
