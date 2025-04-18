# services/recommendations.py

async def generate_recommendations(file_path: str) -> dict:
    """
    Mock recommendations: suggests labs & meds based on simple rules.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().lower()

    # Simple rule-based suggestions
    labs = []
    meds = []
    plan = ""

    if "fever" in content:
        labs.append("CBC")
        meds.append("Paracetamol")
    if "chest pain" in content:
        labs.extend(["ECG", "Troponin I"])
        meds.extend(["Aspirin", "Nitroglycerin"])
    if not labs:
        labs = ["CMP", "Lipid profile"]
    if not meds:
        meds = ["Multivitamins"]

    plan = (
        "Follow standard treatment protocols per UCG-2023; "
        "adjust dosage based on patient factors."
    )

    return {"lab_tests": labs, "medications": meds, "treatment_plan": plan}
