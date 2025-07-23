import requests
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("osint"))
async def osint_fetch(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❗Usage: `/osint username_or_link`", quote=True)

    query = message.command[1]

    await message.reply("🔍 Fetching OSINT data...")

    results = []

    # Telegram username check
    if query.startswith("@") or query.isalnum():
        results.append(f"🟣 Telegram User: `{query}`")
        results.append("• Possible TG Link: https://t.me/" + query.strip("@"))

    # Instagram check
    results.append(f"\n📸 Instagram Profile: https://instagram.com/{query}")

    # Facebook check
    results.append(f"📘 Facebook Profile: https://facebook.com/{query}")

    # LinkedIn check
    results.append(f"💼 LinkedIn Profile: https://linkedin.com/in/{query}")

    await message.reply_text("\n".join(results), disable_web_page_preview=True)
