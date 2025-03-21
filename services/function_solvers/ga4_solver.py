import pandas as pd
import io
import re
from fastapi import UploadFile
from typing import Optional

async def solve(question: str, file: Optional[UploadFile] = None) -> str:
    try:
        if not file:
            return "GA4 expected a CSV file upload, but none was provided."

        # Extract column name from question (e.g., "column age" or "column 'Age'")
        match = re.search(r"column\s['\"]?([\w\s]+?)['\"]?(?:\s+for|\s*$)", question, re.IGNORECASE)
        column_name = match.group(1).strip() if match else None

        if not column_name:
            return "Could not determine the column name from the question."

        # Read uploaded CSV
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))

        if column_name not in df.columns:
            return f"Column '{column_name}' not found in uploaded CSV. Available columns: {', '.join(df.columns)}"

        missing_count = df[column_name].isna().sum()
        return f"Column '{column_name}' contains {missing_count} missing values."

    except Exception as e:
        return f"Error in GA4 solver: {str(e)}"
