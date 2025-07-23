from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
import asyncio

# Simulated members DB (you can replace with actual chat member fetching)
group_members = {}

@Client.on_message(filters.command("tagall") & filters.group)
async def tag_all(client, message: Message):
    if message.from_user.id not in SUDO_USERS:
        return await message.reply("🚫 You don't have permission.")

    chat_id = message.chat.id
    user_ids = group_members.get(chat_id)

    if not user_ids:
        # Simulate fetching members
        user_ids = [f"User{i}" for i in range(1, 51)]  # Replace with real users
        group_members[chat_id] = user_ids

    text = message.text.split(maxsplit=1)
    note = text[1] if len(text) > 1 else "Tagging everyone 👇"

    BATCH = 10
    for i in range(0, len(user_ids), BATCH):
        tags = " ".join([f"@{user}" for user in user_ids[i:i + BATCH]])
        await message.reply(f"{note}\n{tags}")
        await asyncio.sleep(2)  # Prevent flood

@Client.on_message(filters.command("stop") & filters.group)
async def stop_tagging(client, message: Message):
    await message.reply("⛔ Tagging stopped (manual command).")
