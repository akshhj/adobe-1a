import fitz  # PyMuPDF
from collections import Counter

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)

    headings = []
    font_sizes = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]

                    if len(text) > 3 and not text.endswith(":"):
                        headings.append((size, text, page_num))
                        font_sizes.append(size)

    # Determine top 3 font sizes
    most_common = Counter(font_sizes).most_common()
    top_sizes = sorted({fs for fs, _ in most_common}, reverse=True)[:3]

    size_to_level = {}
    if len(top_sizes) > 0:
        size_to_level[top_sizes[0]] = "H1"
    if len(top_sizes) > 1:
        size_to_level[top_sizes[1]] = "H2"
    if len(top_sizes) > 2:
        size_to_level[top_sizes[2]] = "H3"

    outline = []
    for size, text, page in headings:
        if size in size_to_level:
            outline.append({
                "level": size_to_level[size],
                "text": text,
                "page": page
            })

    # Heuristic for title
    title_candidates = [
        span["text"].strip()
        for block in doc[0].get_text("dict")["blocks"]
        for line in block.get("lines", [])
        for span in line.get("spans", [])
        if span["text"].strip()
    ]

    title = max(title_candidates, key=lambda x: len(x), default="Untitled Document")

    return {
        "title": title,
        "outline": outline
    }
