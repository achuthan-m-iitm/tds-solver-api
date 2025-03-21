from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from routers import tds_solver

app = FastAPI(title="TDS Project 2 Solver API")

# CORS (optional, for testing with frontend or Postman)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the API route
app.include_router(tds_solver.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "TDS Solver API is running!"}
