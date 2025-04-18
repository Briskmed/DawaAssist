from pydantic import BaseModel
from typing import List, Optional

class UploadResponse(BaseModel):
    filename: str
    path: str

class AnalyzeNoteResponse(BaseModel):
    diagnosis: str
    differentials: List[str]
    clinical_flags: List[str]

class TriageResponse(BaseModel):
    urgency_level: str
    recommended_action: str

class RecommendationsResponse(BaseModel):
    lab_tests: Optional[List[str]] = []
    medications: Optional[List[str]] = []
    treatment_plan: Optional[str] = ""
