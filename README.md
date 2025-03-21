
# TDS Project 2 – TDS Solver API

This project is built as part of the **Theory of Data Science** course at IIT Madras.  
It exposes a FastAPI-based server that can solve questions from GA1–GA5 (Graded Assignments) dynamically based on input.

---

## 🚀 Features

- ✅ Handles questions from **GA1 to GA5**
- ✅ Intelligent routing using keywords and file type
- ✅ Smart CSV analysis, HTML parsing, PDF extraction
- ✅ Web scraping support (GitHub, IMDb, YouTube)
- ✅ Text sentiment classification
- ✅ Image output as base64 (GA3)
- ✅ Fully testable with `test_runner.py`

---

## 📦 API Usage

### Endpoint
```http
POST /api/solve-question
```

### Request Format (multipart/form-data)
| Field | Type   | Description |
|-------|--------|-------------|
| `question` | string | The question to be solved |
| `file`     | file (optional) | An input file (JSON, CSV, PDF, ZIP, TXT) |

---

### ✅ Example curl
```bash
curl -X POST http://127.0.0.1:8000/api/solve-question \
  -F "question=Drop missing values in column Age" \
  -F "file=@sample_data/missing_age.csv"
```

---

## 🧪 Testing

Run all predefined test cases:

```bash
python final_test_runner.py
```

✅ Test data is in `sample_data/`  
✅ Test cases defined in `tds_test_cases.json`

---

## 🛠 Local Development

```bash
uvicorn main:app --reload
```

Visit Swagger docs at:  
👉 `http://127.0.0.1:8000/docs`

---

## 🌍 Deployment

You can deploy this project using:
- **Render** (free)
- **Azure (Student Credits)**
- **EC2 with Docker**

---

## 📁 Project Structure

```
llm_automation_p2/
├── main.py
├── routers/
│   └── tds_solver.py
├── services/
│   └── dispatcher.py
│   └── function_solvers/
│       ├── ga1_solver.py
│       ├── ga2_solver.py
│       ├── ga3_solver.py
│       ├── ga4_solver.py
│       └── ga5_solver.py
├── utils/
│   └── advanced_parsers.py
├── sample_data/
├── tds_test_cases.json
├── final_test_runner.py
└── README.md ✅
```

---

## 🧑‍⚖️ License

MIT License

---

## 👨‍💻 Author

Achuthan Mukundarajan  
BSc Data Science – IIT Madras  
2025 March Submission
