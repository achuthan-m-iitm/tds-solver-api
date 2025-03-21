import zipfile
import io
from fastapi import UploadFile
from typing import Optional

async def solve(question: str, file: Optional[UploadFile] = None) -> str:
    try:
        if not file:
            return "GA2 expected a ZIP file upload, but none was provided."

        filename = file.filename.lower()
        if not filename.endswith(".zip"):
            return f"GA2 only accepts .zip files. You uploaded: {filename}"

        content = await file.read()
        zip_data = zipfile.ZipFile(io.BytesIO(content))

        txt_files = [f for f in zip_data.namelist() if f.endswith(".txt")]

        if not txt_files:
            return "No .txt files found in the ZIP archive."

        total_lines = 0

        for txt_filename in txt_files:
            with zip_data.open(txt_filename) as f:
                lines = f.read().decode("utf-8").splitlines()
                total_lines += len(lines)

        return f"The ZIP contains {len(txt_files)} text files with a total of {total_lines} lines."

    except Exception as e:
        return f"Error in GA2 solver: {str(e)}"
