import requests
from pyrogram import Client, filters
from pyrogram.types import Message
import re

@Client.on_message(filters.command("osint") & filters.private)
async def osint_scan(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("🔍 Use: `/osint username_or_url`")

    target = message.text.split(" ", 1)[1].strip()
    result = ""

    if target.startswith("http") or "instagram.com" in target:
        result = await get_instagram_data(target)
    elif "facebook.com" in target:
        result = await get_facebook_data(target)
    elif re.match(r"^[A-Za-z0-9_]{5,32}$", target):
        result = await get_telegram_data(target)
    else:
        result = "❌ Unsupported format. Use Telegram username, Instagram/Facebook link."

    await message.reply(result)


async def get_telegram_data(username):
    return f"🧾 Telegram Scan for `{username}`\n\n📌 Username: @{username}\n⚠️ Deep scan not supported via bot."

async def get_instagram_data(link):
    return f"📸 Instagram OSINT for:\n{link}\n\n⚠️ Public profile info requires external scraping."

async def get_facebook_data(link):
    return f"📘 Facebook OSINT for:\n{link}\n\n⚠️ FB data is limited due to privacy policies."
