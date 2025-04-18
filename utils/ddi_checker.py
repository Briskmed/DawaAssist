# utils/ddi_checker.py

def check_ddi(medications: list) -> list:
    """
    Mock DDI checker. Returns a list of interaction warnings.
    """
    # In real system, call RxNorm or DrugBank API
    warnings = []
    # example stub:
    if "aspirin" in [m.lower() for m in medications] and "ibuprofen" in [m.lower() for m in medications]:
        warnings.append("Aspirin + Ibuprofen: increased GI bleeding risk.")
    return warnings
