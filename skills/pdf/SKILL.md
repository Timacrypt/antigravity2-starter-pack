---
name: pdf
description: "Extract text, parse tables, merge, split, and inspect Portable Document Format (.pdf) files. Use when the user asks to read PDF documents, extract content from PDFs, summarize PDF research papers, or handle PDF files."
---

# pdf: PDF Processing Skill for Antigravity 2.0

This skill enables Antigravity 2.0 to inspect, extract text, parse tables, split, and merge Adobe Portable Document Format (`.pdf`) files with high accuracy.

---

## 🛠️ Dependency Self-Healing (執行前環境檢查)

Before running PDF operations, ensure `pypdf` or `pymupdf` is installed.
In your Python script or terminal:
```python
import subprocess, sys
try:
    import pypdf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf", "pymupdf"])
    import pypdf
```

---

## 🚀 Core Capabilities

1. **Extract Full Text & Metadata**:
   - Extract text page-by-page.
   - Inspect PDF metadata (Author, Creation Date, Page Count, Title).
2. **Search & Extract Specific Sections**:
   - Locate keywords, section headers, or abstract paragraphs.
3. **Merge & Split PDFs**:
   - Combine multiple PDF files into one.
   - Extract specific page ranges (e.g. Pages 1-5).

---

## 📝 Example Python Workflow

### Extracting Text from a PDF:
```python
import pypdf

reader = pypdf.PdfReader("sample.pdf")
num_pages = len(reader.pages)
print(f"📄 總頁數: {num_pages}")

extracted_text = []
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        extracted_text.append(f"--- [Page {i+1}] ---\n{text.strip()}")

full_content = "\n\n".join(extracted_text)
print(full_content[:1000]) # Print first 1000 characters
```

### Merging Multiple PDFs:
```python
import pypdf

merger = pypdf.PdfWriter()

for pdf in ["part1.pdf", "part2.pdf"]:
    merger.append(pdf)

merger.write("merged_output.pdf")
merger.close()
print("✅ 合併完成：merged_output.pdf")
```
