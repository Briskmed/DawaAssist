from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from services.diagnostics import process_clinical_note
from services.triage import triage_patient
from services.recommendations import generate_recommendations
from utils.file_handler import save_uploaded_file
import os

app = FastAPI(title="DawaAssist API", version="0.1")

UPLOAD_DIR = "static/uploads/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "Welcome to DawaAssist API"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = await save_uploaded_file(file, UPLOAD_DIR)
    return {"filename": file.filename, "path": file_path}

@app.post("/analyze-note/")
async def analyze_clinical_note(file: UploadFile = File(...)):
    file_path = await save_uploaded_file(file, UPLOAD_DIR)
    try:
        diagnosis, differentials, flags = await process_clinical_note(file_path)
        return {
            "diagnosis": diagnosis,
            "differentials": differentials,
            "clinical_flags": flags,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/triage/")
async def patient_triage(file: UploadFile = File(...)):
    file_path = await save_uploaded_file(file, UPLOAD_DIR)
    try:
        triage_result = await triage_patient(file_path)
        return triage_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/recommendations/")
async def get_recommendations(file: UploadFile = File(...)):
    file_path = await save_uploaded_file(file, UPLOAD_DIR)
    try:
        recommendations = await generate_recommendations(file_path)
        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
