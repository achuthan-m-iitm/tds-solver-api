import json
from fastapi import UploadFile
from typing import Optional
from fastapi import UploadFile
from bs4 import BeautifulSoup 
async def solve(question: str, file: Optional[UploadFile] = None) -> str:
    try:
        #  STEP 1: Check if question contains HTML to parse
        if "<input" in question.lower() or "<form" in question.lower():
            soup = BeautifulSoup(question, "html.parser")
            input_elem = soup.find("input", {"type": "hidden"})
            if input_elem and input_elem.has_attr("value"):
                return f"The value of the hidden input is: {input_elem['value']}"
            else:
                return "Could not find a hidden input field with a value."

        # STEP 2: Standard GA1 JSON file logic
        if not file:
            return "GA1 expected a JSON file upload, but none was provided."

        # Read file content asynchronously
        content = await file.read()
        data = json.loads(content)

        # Count number of top-level keys/items
        if isinstance(data, dict):
            num_keys = len(data.keys())
            return f"The uploaded JSON contains {num_keys} top-level keys."
        elif isinstance(data, list):
            return f"The uploaded JSON is a list with {len(data)} items."
        else:
            return "Unsupported JSON format."

    except Exception as e:
        return f"Error in GA1 solver: {str(e)}"