#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper script for Word (.docx) manipulation in Antigravity 2.0.
"""

import sys
import subprocess

try:
    import docx
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    import docx
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH

def read_docx(file_path):
    """Extract paragraphs and tables from a docx file."""
    doc = docx.Document(file_path)
    content = {"paragraphs": [], "tables": []}
    for p in doc.paragraphs:
        if p.text.strip():
            content["paragraphs"].append(p.text)
    for table in doc.tables:
        t_data = []
        for row in table.rows:
            t_data.append([c.text.strip() for c in row.cells])
        content["tables"].append(t_data)
    return content

def create_report(title, sections, output_path="report.docx"):
    """
    sections: list of dicts with keys: 'heading', 'content', 'table' (optional)
    """
    doc = docx.Document()
    
    # Title
    t_para = doc.add_heading(level=0)
    run = t_para.add_run(title)
    run.font.size = Pt(22)
    run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
    
    for sec in sections:
        if "heading" in sec:
            doc.add_heading(sec["heading"], level=1)
        if "content" in sec:
            doc.add_paragraph(sec["content"])
        if "table" in sec and sec["table"]:
            rows_data = sec["table"]
            table = doc.add_table(rows=len(rows_data), cols=len(rows_data[0]))
            table.style = 'Table Grid'
            for r_idx, row in enumerate(rows_data):
                for c_idx, val in enumerate(row):
                    table.cell(r_idx, c_idx).text = str(val)
                    
    doc.save(output_path)
    return output_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = read_docx(sys.argv[1])
        print(f"Read {len(data['paragraphs'])} paragraphs and {len(data['tables'])} tables.")
