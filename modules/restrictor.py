# modules/restrictor.py

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio

# ✅ Restrict specific user from using bot temporarily
restricted_users = set()

def restrict_user(user_id: int):
    restricted_users.add(user_id)

def allow_user(user_id: int):
    restricted_users.discard(user_id)

def is_restricted(user_id: int) -> bool:
    return user_id in restricted_users

@Client.on_message(filters.private & filters.text)
async def block_restricted_users(client, message: Message):
    if is_restricted(message.from_user.id):
        try:
            await message.reply_text("🚫 You are temporarily restricted from using this bot.")
        except FloodWait as e:
            await asyncio.sleep(e.value)
        return