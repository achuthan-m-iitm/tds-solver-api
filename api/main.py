from fastapi import FastAPI, File, UploadFile, Form
import json
from api.utils import identify_question

app = FastAPI()

@app.post("/api/")
async def solve_tds_question(
    question: str = Form(...),
    file: UploadFile = File(None)
):
    answer = identify_question(question, file)
    return {"answer": answer}
