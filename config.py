# config.py

import os

# Directory for saving uploads
UPLOAD_DIR = "static/uploads/"

# Ensure upload dir exists on startup
os.makedirs(UPLOAD_DIR, exist_ok=True)
