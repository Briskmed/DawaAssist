# services/triage.py

import random

async def triage_patient(file_path: str) -> dict:
    """
    Mock triage function: reads the note and assigns an urgency level.
    """
    # (In a real app you'd analyze content for red‐flags, vitals, etc.)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().lower()

    # Dummy logic
    if "pain" in content or "bleeding" in content:
        urgency = "High"
        action = "Immediate assessment"
    else:
        urgency = random.choice(["Low", "Medium", "High"])
        action = "Routine follow‐up" if urgency != "High" else "Expedited review"

    return {"urgency_level": urgency, "recommended_action": action}
