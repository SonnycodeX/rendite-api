from fastapi import FastAPI
from app.pdf_reader import extract_texts_from_pdfs

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PDF-API läuft"}

@app.get("/texts")
def get_texts():
    return extract_texts_from_pdfs()
