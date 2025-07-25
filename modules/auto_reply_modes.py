# modules/auto_reply_modes.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
from brain import get_ai_reply
from utils.language import detect_language, translate_text

# In-memory user mood states
user_moods = {}

# Available moods
MOODS = {
    "default": "💬 Normal",
    "romantic": "❤️ Romantic",
    "serious": "🧠 Serious",
    "angry": "😡 Angry",
    "funny": "🤣 Funny",
    "friendly": "😊 Friendly"
}

def set_mood(user_id: int, mood: str):
    user_moods[user_id] = mood

def get_mood(user_id: int) -> str:
    return user_moods.get(user_id, "default")

def mood_prefix(mood: str) -> str:
    return {
        "romantic": "Talk like a sweet lover, always romantic:",
        "serious": "Give serious and logical replies:",
        "angry": "Reply with savage, angry tone:",
        "funny": "Reply sarcastically in a funny way:",
        "friendly": "Talk like a close friend, casual tone:",
        "default": ""
    }.get(mood, "")

# Owner-only command to change mood
@Client.on_message(filters.command(["mood", "setmood"]) & filters.user(OWNER_ID))
async def change_user_mood(_, message: Message):
    if len(message.command) < 2:
        mood_list = "\n".join([f"`{k}` → {v}" for k, v in MOODS.items()])
        await message.reply_text(
            f"🎭 **Available Moods:**\n\n{mood_list}\n\nUse `/mood romantic` or `/mood funny`"
        )
        return

    mood = message.command[1].lower()
    if mood in MOODS:
        set_mood(message.from_user.id, mood)
        await message.reply_text(f"✅ Mood set to **{MOODS[mood]}**")
    else:
        await message.reply("❌ Invalid mood. Try `/mood funny` or `/mood romantic`")

# Auto-reply based on mood (in DMs)
@Client.on_message(filters.private & ~filters.command(["start", "help", "mood", "setmood"]))
async def auto_reply_mode_handler(client, message: Message):
    user_id = message.from_user.id
    mood = get_mood(user_id)
    prefix = mood_prefix(mood)

    input_text = message.text or ""
    lang = detect_language(input_text)

    if lang != "en":
        input_text = translate_text(input_text, lang, "en")

    prompt = f"{prefix} {input_text}"
    ai_reply = await get_ai_reply(user_id, prompt)

    if lang != "en":
        ai_reply = translate_text(ai_reply, "en", lang)

    await message.reply_text(ai_reply)