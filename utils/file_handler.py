# utils/file_handler.py

import os
from fastapi import UploadFile

async def save_uploaded_file(file: UploadFile, destination: str) -> str:
    """
    Saves an UploadFile to the given directory.
    Returns the path to the saved file.
    """
    os.makedirs(destination, exist_ok=True)
    file_path = os.path.join(destination, file.filename)

    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)

    return file_path
