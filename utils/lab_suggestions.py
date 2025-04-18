# utils/lab_suggestions.py

def suggest_labs_from_diagnosis(diagnosis: str) -> list:
    """
    Mock lab suggestions based on a primary diagnosis.
    """
    mapping = {
        "malaria": ["Peripheral smear", "Rapid diagnostic test"],
        "pneumonia": ["Chest X-Ray", "CBC"],
        "diabetes mellitus": ["HbA1c", "Fasting glucose"],
    }
    return mapping.get(diagnosis.lower(), ["CBC", "CMP"])
