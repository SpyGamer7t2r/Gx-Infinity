import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Telegram Bot Credentials ---
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# --- AI Engine Settings ---
AI_MODE = os.getenv("AI_MODE", "openai").lower()  # openai / openrouter / deepai
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY", "")

# --- Owner/Admin ---
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# --- Default Bot Mood ---
DEFAULT_MOOD = os.getenv("DEFAULT_MOOD", "neutral")  # romantic / angry / funny / neutral / serious

# --- Feature Toggles ---
ALLOW_NSFW = os.getenv("ALLOW_NSFW", "false").lower() == "true"

# --- File Handling Paths ---
DOWNLOAD_FOLDER = "downloads"     # For downloads, zips, media
TEMP_FOLDER = "temp"              # For temporary processing

# --- Supported Command Prefixes ---
PREFIX = ["/", "!", ".", "?"]     # Support for multiple prefix symbols