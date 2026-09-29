#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper script for PDF manipulation in Antigravity 2.0.
"""

import sys
import subprocess

try:
    import pypdf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    import pypdf

def extract_pdf_text(file_path):
    """Extract text from all pages of a PDF."""
    reader = pypdf.PdfReader(file_path)
    pages_text = []
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages_text.append({"page": idx + 1, "text": text.strip()})
    return pages_text

def merge_pdfs(pdf_paths, output_path="merged.pdf"):
    """Merge a list of PDF files."""
    writer = pypdf.PdfWriter()
    for path in pdf_paths:
        writer.append(path)
    writer.write(output_path)
    writer.close()
    return output_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = extract_pdf_text(sys.argv[1])
        print(f"Extracted {len(data)} pages from {sys.argv[1]}")
