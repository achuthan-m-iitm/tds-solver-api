import os
import json

# Create the directory
os.makedirs("api", exist_ok=True)

# main.py
main_py = '''from fastapi import FastAPI, File, UploadFile, Form
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
'''

with open("api/main.py", "w") as f:
    f.write(main_py)

# utils.py
utils_py = '''import json

with open("tds_ga_questions.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

def identify_question(question_text, file=None):
    # Simple keyword match or default response
    for qid, qtext in QUESTIONS.items():
        if qtext.lower() in question_text.lower():
            return f"Matched {qid} - Answer logic not yet implemented."
    return "This question is not yet supported."
'''

with open("api/utils.py", "w") as f:
    f.write(utils_py)

# requirements.txt
requirements = """fastapi
uvicorn
python-multipart
openai
"""

with open("requirements.txt", "w") as f:
    f.write(requirements)

# vercel.json
vercel_config = '''{
  "builds": [
    { "src": "api/main.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "api/main.py" }
  ]
}
'''

with open("vercel.json", "w") as f:
    f.write(vercel_config)

# README.md
readme = (
    "# TDS Solver API\n"
    "\n"
    "An API to solve IITM's Tools in Data Science graded assignment questions using a hybrid of function-based and LLM approaches.\n"
    "\n"
    "## ✅ Endpoint\n"
    "**POST** `/api/`\n"
    "- Accepts: `question` (text), optional `file`\n"
    "- Returns: `{ \"answer\": \"...\" }`\n"
    "\n"
    "## 💡 Example CURL\n"
    "\n"
    "```bash\n"
    "curl -X POST https://your-app.vercel.app/api/ \\\n"
    "  -F \"question=Download and unzip file abcd.zip...\" \\\n"
    "  -F \"file=@abcd.zip\"\n"
    "```\n"
)
