# core/dir.py

import os
import logging

from config import TEMP_DOWNLOAD_DIR, LOG_DIR, STICKER_DIR, MUSIC_DIR

def ensure_directories():
    os.makedirs(TEMP_DOWNLOAD_DIR, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(STICKER_DIR, exist_ok=True)
    os.makedirs(MUSIC_DIR, exist_ok=True)
    logging.info("[INFO] Directories Verified and Ready.")

# Run when imported
ensure_directories()
