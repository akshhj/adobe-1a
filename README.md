# adobe-1a
# Team - Orion
# PDF Outline Extractor – Adobe India Hackathon (Round 1A)

## 🚀 Goal
Extract a clean, hierarchical outline from a PDF including:
- Title
- Headings (H1, H2, H3) with page numbers

## 📂 Directory Structure
/app/input -> Contains input .pdf files (mounted by Docker)
/app/output -> Output .json files will be saved here

## 🧠 Approach
- Parsed PDFs using **PyMuPDF (fitz)** for lightweight, offline text extraction.
- Extracted text spans, font sizes, and locations.
- Used **font size frequency** to estimate heading levels:
  - Largest = H1
  - Next largest = H2
  - Next = H3
- Title is estimated as the longest or largest text on the first page.

## 🐳 Docker Build & Run

### Build Image
```bash
docker build --platform linux/amd64 -t pdfextractor:round1a .
