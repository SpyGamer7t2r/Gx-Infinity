import os
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

from modules.fun_stats import update_user_stats
from modules.auto_reply_modes import auto_reply
from modules.auto_reply_modes import auto_reply_mode_handler as auto_reply
from modules.reaction_handler import emoji_react
from modules.nsfw_guard import scan_nsfw
from modules.brain import generate_ai_response
from modules.voice_to_text import voice_to_text_handler

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "InfinityAIBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)


@app.on_message(filters.command("start") & filters.private)
async def start(_, message: Message):
    await message.reply_text(
        "🌟 Welcome to Infinity AI Bot!\n\n"
        "🤖 Talk to me directly, or use commands in group!\n"
        "Try: `/zip`, `/unzip`, `hi`, `generate code`, `gana baja`, etc."
    )


@app.on_message(filters.text & (filters.private | filters.group) & ~filters.command(["start"]))
async def ai_reply(client, message: Message):
    await update_user_stats(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        is_private=message.chat.type == "private",
        partner_id=message.reply_to_message.from_user.id if message.reply_to_message else None
    )

    await emoji_react(message)
    await auto_reply(message)

    if message.voice:
        await voice_to_text_handler(message)
        return

    if await scan_nsfw(message):
        return

    reply = await generate_ai_response(message)
    if reply:
        await message.reply_text(reply)


if __name__ == "__main__":
    print("🧠 Infinity AI Bot is running...")
    app.run()