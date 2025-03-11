import json

with open("tds_ga_questions.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

def identify_question(question_text, file=None):
    # Simple keyword match or default response
    for qid, qtext in QUESTIONS.items():
        if qtext.lower() in question_text.lower():
            return f"Matched {qid} - Answer logic not yet implemented."
    return "This question is not yet supported."
