# handlers/ai_handler.py

from pyrogram import Client, filters
from pyrogram.types import Message
from brain import generate_ai_reply
from core.client import app

@app.on_message(filters.text & ~filters.command(["start", "help"]))
async def handle_ai_reply(client: Client, message: Message):
    if not message.text:
        return
    try:
        user_id = message.from_user.id
        user_message = message.text
        ai_response = await generate_ai_reply(user_id, user_message)
        await message.reply_text(ai_response)
    except Exception as e:
        await message.reply_text("⚠️ AI error occurred.")
        print(f"[AI Handler Error]: {e}")
