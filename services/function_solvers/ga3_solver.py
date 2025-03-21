from fastapi import UploadFile
from typing import Optional
from textblob import TextBlob
from utils.image_utils import generate_test_image  # ✅ new import

async def solve(question: str, file: Optional[UploadFile] = None) -> str:
    try:
        if not file:
            return "GA3 expected a .txt file upload."

        content = await file.read()
        text = content.decode("utf-8")

        if not text.strip():
            return "Uploaded text file is empty."

        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        # 🔁 If the question mentions image, return a base64 image
        if "image" in question.lower():
            return generate_test_image(f"Sentiment: {sentiment}")

        # 🔁 Otherwise return plain text
        return f"The sentiment of the uploaded text is {sentiment}."

    except Exception as e:
        return f"Error in GA3 solver: {str(e)}"
