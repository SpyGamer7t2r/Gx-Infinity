import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# AI settings
AI_MODE = os.getenv("AI_MODE", "openai")  # openai / openrouter / deepai
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
DEEPAI_API_KEY = os.getenv("DEEPAI_API_KEY", "")

DEFAULT_MOOD = os.getenv("DEFAULT_MOOD", "neutral")  # romantic / angry / funny / neutral

# Admins
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))

# Music or Download folders
DOWNLOAD_FOLDER = "downloads"
TEMP_FOLDER = "temp"

# Feature toggles
ALLOW_NSFW = os.getenv("ALLOW_NSFW", "false").lower() == "true"
