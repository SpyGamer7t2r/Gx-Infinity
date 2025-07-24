# modules/reminders.py

import asyncio
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX

reminder_store = {}

def parse_time_input(text):
    units = {"s": "seconds", "m": "minutes", "h": "hours"}
    for unit in units:
        if text.endswith(unit):
            try:
                amount = int(text[:-1])
                return timedelta(**{units[unit]: amount})
            except:
                return None
    return None

@Client.on_message(filters.command("remind", prefixes=PREFIX))
async def set_reminder(client, message: Message):
    if len(message.command) < 3:
        return await message.reply("⏰ Use format: `/remind 10m Take your meds`")

    time_input = message.command[1]
    reminder_text = " ".join(message.command[2:])

    delta = parse_time_input(time_input)
    if not delta:
        return await message.reply("⚠️ Invalid time. Use `10s`, `5m`, or `2h`")

    remind_at = datetime.utcnow() + delta
    user_id = message.from_user.id

    await message.reply(f"✅ Reminder set for {time_input} from now.")

    await asyncio.sleep(delta.total_seconds())
    try:
        await client.send_message(user_id, f"🔔 Reminder: {reminder_text}")
    except:
        pass  # user blocked bot or DMs disabled

@Client.on_message(filters.command("remindme", prefixes=PREFIX))
async def reminder_help(client, message: Message):
    await message.reply("ℹ️ Use `/remind <time> <message>`\nExample: `/remind 1h Walk the dog`")