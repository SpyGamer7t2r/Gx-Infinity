# InfinityAI_bot/plugins/chat_ai.py

from pyrogram import Client, filters
from pyrogram.types import Message
from modules.user_mode import get_user_mode
from brain import ai_response
from modules.translate import translate_if_needed
from modules.nsfw_guard import is_nsfw_safe
from modules.reaction_handler import react_to_text
from config import BOT_USERNAME

TRIGGER_KEYWORDS = ["ai", BOT_USERNAME.lower(), "infinity", "chat", "🤖", "baby", "assistant", "infinity ai"]

@Client.on_message(filters.text & ~filters.edited)
async def handle_ai_message(client, message: Message):
    user_id = message.from_user.id if message.from_user else None
    text = message.text

    # Trigger check (DM or mentions/keywords in group)
    if message.chat.type != "private":
        if not any(word.lower() in text.lower() for word in TRIGGER_KEYWORDS):
            return

    # Translate input if needed
    translated_text, user_lang = await translate_if_needed(text)

    # NSFW check (if enabled)
    if not await is_nsfw_safe(message, translated_text):
        return

    # Get user mode (brain/personality)
    mode = await get_user_mode(user_id)

    # Typing simulation
    await message.chat.send_chat_action("typing")

    # Get AI reply
    reply = await ai_response(translated_text, user_id, mode)

    # Reaction system
    await react_to_text(client, message, reply)

    # Send reply
    await message.reply_text(reply)