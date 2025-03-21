from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from services.dispatcher import solve_question
from utils.file_url_handler import fetch_file_from_url

router = APIRouter()

@router.post("/solve-question")
async def solve_question_api(
    question: str = Form(...),
    file: Optional[UploadFile] = File(None),
    file_url: Optional[str] = Form(None),
):
    # If file is not uploaded, but file_url is given → download it
    if not file and file_url:
        file = await fetch_file_from_url(file_url)

    result = await solve_question(question, file)
    return {"answer": result}