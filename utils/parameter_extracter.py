import re

def extract_keywords(question: str):
    # Very naive version for now
    matches = re.findall(r'GA[1-5]_Q\d+', question.upper())
    return matches[0].lower() if matches else "unknown"
