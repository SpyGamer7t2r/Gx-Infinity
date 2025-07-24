from pyrogram import Client, filters
from pyrogram.types import Message
from utils.osint import fetch_user_info

@Client.on_message(filters.command("osint") & filters.private)
async def osint_handler(_, message: Message):
    if len(message.command) < 2:
        await message.reply("🔍 Usage: `/osint username_or_link`")
        return

    target = message.command[1]
    await message.reply("🕵️ Gathering intelligence...")

    try:
        result = await fetch_user_info(target)
        await message.reply(result)
    except Exception as e:
        await message.reply(f"❌ Failed to fetch info:\n`{e}`")