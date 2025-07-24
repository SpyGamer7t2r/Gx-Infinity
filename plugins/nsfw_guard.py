from pyrogram import Client, filters
from pyrogram.types import Message
import re

# Add more keywords or use an external NSFW detection API for images
NSFW_KEYWORDS = [
    "nude", "porn", "sex", "boobs", "pussy", "dick", "xxx", "nsfw", "horny", "fuck", "bitch", "asshole"
]

# Example config for per group NSFW mode (you can link to a DB or config file)
NSFW_MODE_ENABLED = {}

def is_nsfw_text(text: str):
    return any(re.search(rf"\b{re.escape(word)}\b", text.lower()) for word in NSFW_KEYWORDS)

@Client.on_message(filters.command("nsfw_mode"))
async def toggle_nsfw_mode(_, message: Message):
    if message.chat.type not in ["supergroup", "group"]:
        await message.reply("This command only works in groups.")
        return

    status = message.command[1] if len(message.command) > 1 else None
    chat_id = message.chat.id

    if status == "on":
        NSFW_MODE_ENABLED[chat_id] = True
        await message.reply("🔞 NSFW Guard is now **enabled** in this group.")
    elif status == "off":
        NSFW_MODE_ENABLED[chat_id] = False
        await message.reply("🔕 NSFW Guard has been **disabled**.")
    else:
        await message.reply("Usage: `/nsfw_mode on` or `/nsfw_mode off`")

@Client.on_message(filters.text & filters.group & ~filters.edited)
async def nsfw_detector(_, message: Message):
    chat_id = message.chat.id
    if not NSFW_MODE_ENABLED.get(chat_id):
        return

    if is_nsfw_text(message.text):
        try:
            await message.delete()
            await message.reply(f"🚫 Message deleted due to NSFW content!\nUser: {message.from_user.mention}")
        except Exception:
            pass