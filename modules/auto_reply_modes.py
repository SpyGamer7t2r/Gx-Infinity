# modules/auto_reply_modes.py

from pyrogram import Client, filters  # ✅ Added Client import
from pyrogram.types import Message
from config import OWNER_ID
from brain import get_ai_reply
from utils.language import detect_language, translate_text

# In-memory mood states
user_moods = {}

MOODS = {
    "default": "💬 Normal",
    "romantic": "❤️ Romantic",
    "serious": "🧠 Serious",
    "angry": "😡 Angry",
    "funny": "🤣 Funny",
    "friendly": "😊 Friendly"
}

def set_mood(user_id, mood):
    user_moods[user_id] = mood

def get_mood(user_id):
    return user_moods.get(user_id, "default")

def mood_prefix(mood):
    return {
        "romantic": "Talk like a sweet lover. Reply romantically:",
        "serious": "Reply seriously and logically:",
        "angry": "Reply like you're slightly angry and savage:",
        "funny": "Reply with sarcasm and fun tone:",
        "friendly": "Reply like a close friend:",
        "default": "",
    }.get(mood, "")


# Command to change mood
@Client.on_message(filters.command(["mood", "setmood"]) & filters.user(OWNER_ID))
async def change_mood(_, message: Message):
    if len(message.command) < 2:
        moods_text = "\n".join([f"`{k}` → {v}" for k, v in MOODS.items()])
        await message.reply(f"😄 **Available Moods:**\n\n{moods_text}\n\nUse `/mood romantic`")
        return

    mood = message.command[1].lower()
    if mood in MOODS:
        set_mood(message.from_user.id, mood)
        await message.reply(f"✅ Mood set to **{MOODS[mood]}**")
    else:
        await message.reply("❌ Unknown mood. Try `/mood romantic` or `/mood serious`")


# Auto Reply Handler
@Client.on_message(filters.private & ~filters.command(["start", "help", "mood"]))
async def auto_reply_mode_handler(client, message: Message):
    user_id = message.from_user.id
    mood = get_mood(user_id)
    prefix = mood_prefix(mood)

    original_text = message.text
    lang = detect_language(original_text)

    if lang != "en":
        original_text = translate_text(original_text, lang, "en")

    prompt = f"{prefix} {original_text}"
    reply = await get_ai_reply(user_id, prompt)

    if lang != "en":
        reply = translate_text(reply, "en", lang)

    await message.reply(reply)