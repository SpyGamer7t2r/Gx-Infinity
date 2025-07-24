# modules/fun_stats.py

from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime
from config import PREFIX

# In-memory storage (replace with DB for persistence)
user_stats = {}

@Client.on_message(filters.private | filters.group)
async def track_message_stats(client, message: Message):
    if not message.from_user:
        return

    user_id = message.from_user.id
    chat_type = message.chat.type
    user_stats.setdefault(user_id, {"dm": 0, "group": 0, "first_seen": datetime.utcnow()})

    if chat_type == "private":
        user_stats[user_id]["dm"] += 1
    else:
        user_stats[user_id]["group"] += 1

@Client.on_message(filters.command("mystats", prefixes=PREFIX))
async def show_stats(client, message: Message):
    user_id = message.from_user.id
    stats = user_stats.get(user_id)

    if not stats:
        return await message.reply("❌ No stats found for you yet.")

    reply = (
        f"📊 **Your FunStats**\n"
        f"👤 User ID: `{user_id}`\n"
        f"💬 DMs Sent: `{stats['dm']}`\n"
        f"👥 Group Messages: `{stats['group']}`\n"
        f"📆 First Seen: `{stats['first_seen'].strftime('%Y-%m-%d %H:%M:%S')}`"
    )
    await message.reply(reply)

# Add this at the end
def update_stats():
    return user_stats