# handlers/admin_handler.py

from pyrogram import Client, filters
from pyrogram.types import Message
from core.client import app
from config import OWNER_ID

@app.on_message(filters.command("gbanall") & filters.user(OWNER_ID))
async def gban_all_handler(client: Client, message: Message):
    await message.reply_text("🚫 Global Ban-All is under development.")

@app.on_message(filters.command("banall") & filters.user(OWNER_ID))
async def ban_all_handler(client: Client, message: Message):
    await message.reply_text("🚫 Ban-All in current group is under development.")

@app.on_message(filters.command("muteall") & filters.user(OWNER_ID))
async def mute_all_handler(client: Client, message: Message):
    await message.reply_text("🔇 Mute-All coming soon!")

@app.on_message(filters.command("kickall") & filters.user(OWNER_ID))
async def kick_all_handler(client: Client, message: Message):
    await message.reply_text("👢 Kick-All feature is coming soon!")
