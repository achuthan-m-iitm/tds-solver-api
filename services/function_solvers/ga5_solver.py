import pandas as pd
import io
import re
import shlex
from fastapi import UploadFile
from typing import Optional
from utils.advanced_parsers import (
    scrape_web_data,
    parse_html_table_from_string,
    extract_text_from_pdf,
)

async def solve(question: str, file: Optional[UploadFile] = None) -> str:
    try:
        question_lower = question.lower()

        # 🔍 1. Handle scraping logic
        if any(site in question_lower for site in ["imdb.com", "github.com", "youtube.com"]):
            keyword = "rating"
            if "keyword" in question_lower:
                try:
                    parts = shlex.split(question)
                    idx = parts.index("keyword")
                    keyword = parts[idx + 1]
                except (ValueError, IndexError):
                    pass
            url_match = re.search(r"(https?://[^\s]+)", question)
            url = url_match.group(1) if url_match else ""
            return scrape_web_data(url, keyword)

        # 🧾 2. Handle HTML table parsing
        if "<table" in question_lower and "</table>" in question_lower:
            return parse_html_table_from_string(question)

        # 📄 3. Handle PDF file parsing
        if file and file.filename.lower().endswith(".pdf"):
            pdf_bytes = await file.read()
            pdf_text = extract_text_from_pdf(pdf_bytes)
            return f"Extracted from PDF:\n{pdf_text[:300]}..."

        # 📊 4. GA5 CSV-based logic
        if not file:
            return "GA5 expected a CSV or PDF file upload."

        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))

        # 🧠 Extract column name
        match = re.search(r"column\s+['\"]?([\w\s]+?)['\"]?(?:\s|$)", question, re.IGNORECASE)
        column = match.group(1).strip() if match else None

        if not column:
            return "Could not detect the column name from the question."

        if column not in df.columns:
            return f"Column '{column}' not found in uploaded CSV. Available columns: {', '.join(df.columns)}"

        # ✅ Drop missing values in column
        if "drop" in question_lower and "missing" in question_lower:
            before = len(df)
            df = df.dropna(subset=[column])
            after = len(df)
            return f"{after} rows remain after dropping missing values in column '{column}'."

        # ✅ Lowercase normalization
        if "lowercase" in question_lower or "normalize" in question_lower:
            if df[column].dtype == "object":
                normalized = df[column].str.lower().dropna().head(5).tolist()
                return f"First 5 entries in column '{column}' after lowercasing: {normalized}"
            else:
                return f"Column '{column}' is not textual. Cannot lowercase."

        return f"GA5 recognized column '{column}', but no supported operation was identified in the question."

    except Exception as e:
        return f"Error in GA5 solver: {str(e)}"
