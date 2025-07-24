# core/constants.py

from pyrogram.enums import ChatType

# Bot Modes
AI_MODES = {
    "default": "Default",
    "romantic": "Romantic",
    "serious": "Serious",
    "jugaadu": "Jugaadu",
    "deep_ai": "Deep Thinker",
    "openrouter": "OpenRouter",
}

# Gender Modes
GENDER_MODES = {
    "male": "💪 Boy Mode",
    "female": "💃 Girl Mode",
    "neutral": "⚧️ Neutral Mode"
}

# Chat Types
CHAT_TYPES = {
    ChatType.PRIVATE: "Private",
    ChatType.GROUP: "Group",
    ChatType.SUPERGROUP: "Supergroup",
    ChatType.CHANNEL: "Channel"
}

# Supported Code Languages
SUPPORTED_LANGUAGES = [
    "python", "cpp", "c", "csharp", "go", "java", "javascript",
    "kotlin", "php", "ruby", "rust", "scala", "swift", "ts"
]

# Default Settings
DEFAULT_BRAIN = "default"
DEFAULT_MOOD = "neutral"
DEFAULT_LANG = "en"

# Inline Button Emojis
BUTTONS = {
    "like": "👍",
    "dislike": "👎",
    "next": "⏭️",
    "back": "⏮️",
    "zip": "🗜️",
    "unzip": "📂",
    "music": "🎵",
    "video": "🎬",
    "ai": "🤖",
}

# Other Constants
OWNER_ID = 123456789  # Replace with your Telegram user ID
BOT_NAME = "Infinity AI 🤖"
VERSION = "1.0.0"
