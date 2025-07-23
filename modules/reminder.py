import asyncio
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import Message

reminders = {}

@Client.on_message(filters.command("remind"))
async def set_reminder(client, message: Message):
    try:
        parts = message.text.split(" ", 2)
        time_in_minutes = int(parts[1])
        reminder_text = parts[2]

        remind_time = datetime.now() + timedelta(minutes=time_in_minutes)
        user_id = message.from_user.id

        if user_id not in reminders:
            reminders[user_id] = []

        reminders[user_id].append((remind_time, reminder_text))
        await message.reply(f"⏰ Reminder set for **{time_in_minutes} minutes**: `{reminder_text}`")
        
        await asyncio.sleep(time_in_minutes * 60)
        await client.send_message(user_id, f"🔔 Reminder: {reminder_text}")

    except Exception as e:
        await message.reply("❗Usage: `/remind <minutes> <reminder_text>`\nExample: `/remind 10 Take a break!`")
