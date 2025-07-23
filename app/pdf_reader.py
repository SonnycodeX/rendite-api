import os
from PyPDF2 import PdfReader

def extract_texts_from_pdfs():
    texts = []
    folder = "app/pdfs"

    for filename in os.listdir(folder):
        if filename.endswith(".pdf"):
            path = os.path.join(folder, filename)
            reader = PdfReader(path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            texts.append({"filename": filename, "text": text})

    return texts
