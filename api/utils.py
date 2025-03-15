import json
import zipfile
import pandas as pd
import os
from difflib import get_close_matches

# Load the question map
with open("tds_ga_questions.json", "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

# Fuzzy match the incoming question to known GA questions
def match_question_id(incoming_question: str) -> str:
    incoming_question = incoming_question.lower()
    question_texts = {qid: qtext.lower() for qid, qtext in QUESTIONS.items()}

    close_matches = get_close_matches(incoming_question, question_texts.values(), n=1, cutoff=0.6)

    if close_matches:
        for qid, qtext in question_texts.items():
            if qtext == close_matches[0]:
                return qid
    return "unknown"

# Route the question to the appropriate solver
def identify_question(question_text, file=None):
    qid = match_question_id(question_text)

    if qid == "GA1_Q1":
        return solve_ga1_q1(file)
    elif qid == "GA1_Q2":
        return solve_ga1_q2(file)
    elif qid == "GA2_Q2":
        return solve_ga2_q2(file)
    elif qid == "GA3_Q3":
        return solve_ga3_q3(file)
    elif qid == "GA4_Q1":
        return solve_ga4_q1(file)
    elif qid == "GA5_Q1":
        return solve_ga5_q1(file)

    return "Unsupported question or not implemented yet."

# GA1_Q1: Unzip and count rows in CSV
def solve_ga1_q1(file):
    with open("temp.zip", "wb") as f_out:
        f_out.write(file.file.read())

    with zipfile.ZipFile("temp.zip", "r") as zip_ref:
        zip_ref.extractall("unzipped")

    for fname in os.listdir("unzipped"):
        if fname.endswith(".csv"):
            df = pd.read_csv(os.path.join("unzipped", fname))
            return str(len(df))
    return "CSV not found in ZIP"

# GA1_Q2: Parse JSON and return 'total_users'
def solve_ga1_q2(file):
    with open("uploaded.json", "wb") as f_out:
        f_out.write(file.file.read())

    with open("uploaded.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return str(data.get("total_users", "Key 'total_users' not found"))

# GA2_Q2: Check if image is under 1500 bytes
def solve_ga2_q2(file):
    content = file.file.read()
    file_size = len(content)

    if file_size < 1500:
        return f"File is already compressed: {file_size} bytes"
    else:
        return f"File too large: {file_size} bytes. Needs compression."

# GA3_Q3: Simulated sentiment analysis (simple version)
def solve_ga3_q3(file):
    text = file.file.read().decode("utf-8").lower()
    if "bad" in text or "terrible" in text:
        return "Negative"
    return "Positive"

# GA4_Q1: Count missing values in 'age' column
def solve_ga4_q1(file):
    with open("temp.csv", "wb") as f_out:
        f_out.write(file.file.read())

    df = pd.read_csv("temp.csv")
    if 'age' not in df.columns:
        return "Column 'age' not found"
    return str(df['age'].isna().sum())

# GA5_Q1: Drop NaNs and return row count
def solve_ga5_q1(file):
    with open("uploaded.csv", "wb") as f_out:
        f_out.write(file.file.read())

    df = pd.read_csv("uploaded.csv")
    df_clean = df.dropna()
    return str(len(df_clean))
