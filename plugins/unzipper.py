from pyrogram import Client, filters
from pyrogram.types import Message
from utils.unzipper import unzip_file
import os

@Client.on_message(filters.command("unzip") & filters.reply)
async def unzip_handler(client, message: Message):
    replied = message.reply_to_message

    if not replied or not replied.document or not replied.document.file_name.endswith(".zip"):
        return await message.reply("❌ Please reply to a `.zip` file to extract.")

    password = None
    if len(message.command) > 1:
        password = message.command[1]

    file_path = await replied.download()
    try:
        extracted_path = unzip_file(file_path, password=password)
    except RuntimeError:
        return await message.reply("❌ Incorrect password or unable to extract.")

    file_count = 0
    for root, _, files in os.walk(extracted_path):
        for f in files:
            abs_path = os.path.join(root, f)
            await message.reply_document(abs_path)
            os.remove(abs_path)
            file_count += 1

    os.remove(file_path)
    os.rmdir(extracted_path)

    if file_count == 0:
        await message.reply("⚠️ Unzipped but no files found inside.")
    else:
        await message.reply(f"✅ Extracted and sent `{file_count}` file(s).")