from pydantic import BaseModel
from typing import List, Optional

class ClinicalNote(BaseModel):
    patient_id: str
    note_text: str

class LabReport(BaseModel):
    patient_id: str
    lab_results: dict

class Diagnosis(BaseModel):
    primary_diagnosis: str
    differentials: List[str]
    clinical_flags: List[str]

class TriageResult(BaseModel):
    urgency_level: str
    recommended_action: str

class Recommendation(BaseModel):
    lab_tests: Optional[List[str]] = []
    medications: Optional[List[str]] = []
    treatment_plan: Optional[str] = ""

class FileUploadResponse(BaseModel):
    filename: str
    path: str
