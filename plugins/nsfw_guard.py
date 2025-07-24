from pyrogram import Client, filters
from pyrogram.types import Message
from utils.nsfw_scan import is_nsfw_content

NSFW_MODE = {}

@Client.on_message(filters.command("nsfwmode"))
async def toggle_nsfw_mode(_, message: Message):
    chat_id = message.chat.id
    args = message.text.split()
    if len(args) < 2:
        await message.reply("Usage: `/nsfwmode on` or `/nsfwmode off`", quote=True)
        return

    mode = args[1].lower()
    if mode == "on":
        NSFW_MODE[chat_id] = True
        await message.reply("🔞 NSFW Guard Enabled.")
    elif mode == "off":
        NSFW_MODE[chat_id] = False
        await message.reply("✅ NSFW Guard Disabled.")
    else:
        await message.reply("Invalid option. Use `on` or `off`.")

@Client.on_message(filters.photo | filters.video | filters.document)
async def nsfw_detector_handler(_, message: Message):
    chat_id = message.chat.id
    if not NSFW_MODE.get(chat_id, False):
        return

    try:
        is_nsfw = await is_nsfw_content(message)
        if is_nsfw:
            await message.delete()
            await message.reply("⚠️ NSFW content detected and deleted.")
    except Exception as e:
        print(f"NSFW check failed: {e}")