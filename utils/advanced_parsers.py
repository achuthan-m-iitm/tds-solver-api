# utils/advanced_parsers.py

import requests
import pandas as pd
from bs4 import BeautifulSoup
import fitz  # PyMuPDF

def scrape_web_data(url: str, keyword: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text()
        count = text.lower().count(keyword.lower())
        return f"The keyword '{keyword}' appears {count} times in the page."
    except Exception as e:
        return f"Error scraping URL: {str(e)}"

def parse_html_table_from_string(html: str) -> str:
    try:
        tables = pd.read_html(html)
        if not tables:
            return "No tables found in the HTML."
        df = tables[0]
        summary = df.head(3).to_dict(orient="records")
        return f"Extracted first 3 rows: {summary}"
    except Exception as e:
        return f"Error parsing HTML table: {str(e)}"

def extract_text_from_pdf(file_bytes: bytes) -> str:
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text[:500]
    except Exception as e:
        return f"Error parsing PDF: {str(e)}"
