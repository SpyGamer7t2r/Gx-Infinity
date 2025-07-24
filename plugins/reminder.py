from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import re

REMINDERS = {}

@Client.on_message(filters.command(["remind", "alarm"]) & filters.private)
async def set_reminder(client, message: Message):
    text = message.text
    match = re.search(r"(\d+)\s*(sec|second|seconds|min|minute|minutes|hour|hours)", text, re.IGNORECASE)
    if not match:
        await message.reply("Please specify time like: `/remind 10 minutes Take a break`")
        return

    amount = int(match.group(1))
    unit = match.group(2).lower()

    if "sec" in unit:
        delay = amount
    elif "min" in unit:
        delay = amount * 60
    elif "hour" in unit:
        delay = amount * 3600
    else:
        delay = amount

    reminder_text = text[match.end():].strip()
    if not reminder_text:
        await message.reply("Please specify what to remind.")
        return

    await message.reply(f"⏰ Reminder set for {amount} {unit}(s). I will remind you.")

    async def reminder_task():
        await asyncio.sleep(delay)
        await client.send_message(message.chat.id, f"⏰ Reminder: {reminder_text}")

    asyncio.create_task(reminder_task())