---
name: pptx
description: "Create, edit, analyze, and format Microsoft PowerPoint (.pptx) presentation decks. Use when the user asks to generate slides, design presentation decks, add cards or bullet layouts, format slide titles, or handle PowerPoint files."
---

# pptx: PowerPoint Presentation Processing Skill for Antigravity 2.0

This skill enables Antigravity 2.0 to create, edit, and structure Microsoft PowerPoint (`.pptx`) presentations with clean 16:9 widescreen layouts, structured content cards, modern typography, and consistent color palettes.

---

## 🛠️ Dependency Self-Healing (執行前環境檢查)

Before running PowerPoint presentation operations, ensure `python-pptx` is installed.
In your Python script or terminal:
```python
import subprocess, sys
try:
    import pptx
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-pptx"])
    import pptx
```

---

## 🚀 Core Presentation Principles

1. **Widescreen 16:9 by Default**:
   ```python
   prs.slide_width = Inches(13.333)
   prs.slide_height = Inches(7.5)
   ```
2. **Design Structure**:
   - **Slide 1: Title Slide** (Bold title, subtitle, author metadata).
   - **Slide 2: Agenda / Overview** (3-4 numbered or icon sections).
   - **Content Slides**: Use a 2-column or 3-column card layout rather than a giant wall of plain bullet points.
   - **Final Slide: Summary & Call-to-action**.
3. **Contrast & Typography**:
   - Primary Header Color: Deep Navy (`#1F497D`) or Charcoal (`#222222`).
   - Accent Color: Tech Blue (`#0078D4`) or Coral.
   - Font: Arial, Calibri, or Helvetica.

---

## 📝 Example Python Workflow

### Creating a Clean 16:9 Slide Deck:
```python
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# --- Slide 1: Title Slide ---
slide1 = prs.slides.add_slide(blank_layout)

# Title Text Box
tx_box = slide1.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.33), Inches(3.0))
tf = tx_box.text_frame
tf.word_wrap = True

p_title = tf.paragraphs[0]
p_title.text = "AI Agent 架構與落地應用"
p_title.font.name = "Arial"
p_title.font.size = Pt(44)
p_title.font.bold = True
p_title.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

p_sub = tf.add_paragraph()
p_sub.text = "打造次世代自主工作流程  |  Antigravity 2.0"
p_sub.font.name = "Arial"
p_sub.font.size = Pt(20)
p_sub.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
p_sub.space_before = Pt(14)

# --- Slide 2: 3-Column Card Layout ---
slide2 = prs.slides.add_slide(blank_layout)

# Slide Header
header_box = slide2.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.33), Inches(1.2))
htf = header_box.text_frame
hp = htf.paragraphs[0]
hp.text = "核心功能亮點 (Key Highlights)"
hp.font.size = Pt(32)
hp.font.bold = True
hp.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

# 3 Cards
cards = [
    ("自動化執行", "自主呼叫工具與終端指令，免去手動繁瑣操作。"),
    ("跨工具協調", "整合 MCP 協議與各類外掛，打通資料孤島。"),
    ("狀態持續性", "支援學習歷程記錄與跨對話無縫交接。"),
]

col_w = Inches(3.5)
gap = Inches(0.4)
start_x = Inches(1.0)
card_y = Inches(2.4)
card_h = Inches(4.0)

for idx, (c_title, c_desc) in enumerate(cards):
    cx = start_x + idx * (col_w + gap)
    card_shape = slide2.shapes.add_textbox(cx, card_y, col_w, card_h)
    ctf = card_shape.text_frame
    ctf.word_wrap = True
    
    cp1 = ctf.paragraphs[0]
    cp1.text = f"0{idx+1}. {c_title}"
    cp1.font.size = Pt(20)
    cp1.font.bold = True
    cp1.font.color.rgb = RGBColor(0x00, 0x78, 0xD4)
    
    cp2 = ctf.add_paragraph()
    cp2.text = c_desc
    cp2.font.size = Pt(14)
    cp2.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    cp2.space_before = Pt(12)

prs.save("presentation_deck.pptx")
print("✅ PowerPoint 簡報已儲存至 presentation_deck.pptx")
```
