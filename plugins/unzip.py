from pyrogram import Client, filters
from pyrogram.types import Message
from utils.unzipper import unzip_file
import os

@Client.on_message(filters.command("unzip") & filters.reply)
async def unzip_handler(_, message: Message):
    replied = message.reply_to_message
    if not replied.document:
        await message.reply_text("❌ Please reply to a zip file to unzip.")
        return

    file_path = await replied.download()
    password = None

    # Check if user added password
    if len(message.command) > 1:
        password = message.command[1]

    try:
        extracted_files = unzip_file(file_path, password)
    except RuntimeError:
        await message.reply_text("❌ Incorrect password or failed to unzip file.")
        os.remove(file_path)
        return
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")
        os.remove(file_path)
        return

    for f in extracted_files:
        await message.reply_document(f)
        os.remove(f)

    os.remove(file_path)