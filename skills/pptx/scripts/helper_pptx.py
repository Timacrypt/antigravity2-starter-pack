#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper script for PowerPoint (.pptx) manipulation in Antigravity 2.0.
"""

import sys
import subprocess

try:
    import pptx
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-pptx"])
    import pptx
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor

def create_presentation(title, subtitle, slides_data, output_path="deck.pptx"):
    """
    slides_data: list of dicts with 'title' and 'bullets' (list of strings) or 'cards' (list of tuples: title, desc)
    """
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Title slide
    s1 = prs.slides.add_slide(blank_layout)
    tb = s1.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.33), Inches(3.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = title
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(18)
    p2.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    p2.space_before = Pt(12)

    # Content slides
    for s_info in slides_data:
        s = prs.slides.add_slide(blank_layout)
        # Header
        hb = s.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.33), Inches(1.0))
        hp = hb.text_frame.paragraphs[0]
        hp.text = s_info.get("title", "")
        hp.font.size = Pt(28)
        hp.font.bold = True
        hp.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

        if "cards" in s_info:
            cards = s_info["cards"]
            col_w = Inches(11.33 / max(len(cards), 1) - 0.3)
            for idx, (c_t, c_d) in enumerate(cards):
                cx = Inches(1.0) + idx * (col_w + Inches(0.3))
                cb = s.shapes.add_textbox(cx, Inches(2.2), col_w, Inches(4.0))
                ctf = cb.text_frame
                ctf.word_wrap = True
                cp1 = ctf.paragraphs[0]
                cp1.text = c_t
                cp1.font.size = Pt(18)
                cp1.font.bold = True
                cp1.font.color.rgb = RGBColor(0x00, 0x78, 0xD4)
                cp2 = ctf.add_paragraph()
                cp2.text = c_d
                cp2.font.size = Pt(14)
                cp2.space_before = Pt(8)
        elif "bullets" in s_info:
            cb = s.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(10.8), Inches(4.5))
            ctf = cb.text_frame
            ctf.word_wrap = True
            for idx, b in enumerate(s_info["bullets"]):
                bp = ctf.paragraphs[0] if idx == 0 else ctf.add_paragraph()
                bp.text = f"•  {b}"
                bp.font.size = Pt(16)
                bp.space_before = Pt(10)

    prs.save(output_path)
    return output_path

if __name__ == "__main__":
    create_presentation("示範簡報", "使用 Antigravity 2.0 製作", [
        {"title": "模組優勢", "bullets": ["高效", "穩定", "全白話"]},
    ], "demo.pptx")
    print("Created demo.pptx")
