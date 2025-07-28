import os
import json
from utils import extract_outline_from_pdf

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            result = extract_outline_from_pdf(pdf_path)

            out_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, out_filename)

            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
