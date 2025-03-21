from services.function_solvers import (
    ga1_solver,
    ga2_solver,
    ga3_solver,
    ga4_solver,
    ga5_solver,
)
from fastapi import UploadFile

async def solve_question(question: str, file: UploadFile = None):
    question_lower = question.lower()

    # 🔍 HTML detection (GA1)
    if "<input" in question_lower or "<form" in question_lower or (file and file.filename.endswith(".json")):
        return await ga1_solver.solve(question, file)

    # 📦 ZIP or "text files in zip" (GA2)
    if (file and file.filename.endswith(".zip")) or "text file in zip" in question_lower:
        return await ga2_solver.solve(question, file)

    # 📊 Sentiment or .txt file (GA3)
    if (file and file.filename.endswith(".txt")) or "sentiment" in question_lower or "positive" in question_lower:
        return await ga3_solver.solve(question, file)

    # 🧠 GA5: drop missing, normalize, lowercase, scraping, pdf, html table
    if any(x in question_lower for x in ["drop missing", "normalize", "lowercase", "pdf", "<table", "github.com", "imdb.com", "youtube.com"]):
        return await ga5_solver.solve(question, file)

    # 📈 GA4: count missing values
    if "missing" in question_lower and "column" in question_lower:
        return await ga4_solver.solve(question, file)

    # Fallback
    return "Sorry, this question is not supported yet."