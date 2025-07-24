from pyrogram import Client, filters
from pyrogram.types import Message
import re

# Simple abusive word list (expand as needed)
ABUSIVE_WORDS = ["chutiya", "madarchod", "bhosdike", "gandu", "randi", "loda", "lund", "chodu", "behenchod", "mc", "bc"]

# Per-chat NSFW gaali mode status
NSFW_STATUS = {}

def contains_abuse(text: str) -> bool:
    return any(re.search(rf"\b{word}\b", text.lower()) for word in ABUSIVE_WORDS)

@Client.on_message(filters.command("nsfw_mode"))
async def toggle_nsfw(client, message: Message):
    chat_id = message.chat.id
    current = NSFW_STATUS.get(chat_id, False)
    NSFW_STATUS[chat_id] = not current
    status = "🛡️ ON" if not current else "❌ OFF"
    await message.reply(f"NSFW Guard (Gaali Filter) is now: {status}")

@Client.on_message(filters.text & ~filters.private)
async def nsfw_monitor(client, message: Message):
    chat_id = message.chat.id
    if NSFW_STATUS.get(chat_id, False) and contains_abuse(message.text):
        try:
            await message.reply("🚫 Gaali detect hua! Sigma style activated 😎")
            await client.delete_messages(chat_id, message.id)
        except Exception:
            pass