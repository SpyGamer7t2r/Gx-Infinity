# modules/reaction_handler.py

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import MessageEntityType
from config import OWNER_ID
from loader import app

REACTIONS = ["🔥", "😂", "💀", "😍", "😎", "🥺", "🤯", "👍", "👎", "❤️"]

@app.on_message(filters.command("react") & filters.reply)
async def react_to_message(client, message: Message):
    if len(message.command) < 2:
        await message.reply("Please provide a reaction emoji. Example: `/react 😂`", quote=True)
        return

    emoji = message.text.split(None, 1)[1].strip()

    if emoji not in REACTIONS:
        await message.reply(f"Only these emojis are allowed:\n{', '.join(REACTIONS)}", quote=True)
        return

    try:
        await message.reply_to_message.react(emoji)
        await message.reply(f"Reacted with {emoji} ✅", quote=True)
    except Exception as e:
        await message.reply(f"Failed to react: {e}", quote=True)

@app.on_message(filters.command("reactions"))
async def list_reactions(client, message: Message):
    text = "**Available Reactions:**\n"
    text += "\n".join(f"- {emoji}" for emoji in REACTIONS)
    await message.reply(text, quote=True)