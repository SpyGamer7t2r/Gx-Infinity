from pyrogram import Client, filters
from pyrogram.types import Message
from utils.zipper import zip_file, zip_with_password, zip_multiple_files
from utils.password_gen import generate_password
import os

@Client.on_message(filters.command("zip") & filters.reply)
async def zip_handler(_, message: Message):
    replied = message.reply_to_message
    if not replied.document:
        await message.reply_text("❌ Please reply to a document or file to zip.")
        return

    file = await replied.download()
    zip_path = zip_file(file)

    await message.reply_document(
        zip_path,
        caption="✅ File zipped successfully."
    )
    os.remove(file)
    os.remove(zip_path)

@Client.on_message(filters.command("zip_pwd") & filters.reply)
async def zip_with_pwd_handler(_, message: Message):
    replied = message.reply_to_message
    if not replied.document:
        await message.reply_text("❌ Please reply to a document or file to zip with password.")
        return

    file = await replied.download()
    password = generate_password()
    zip_path = zip_with_password(file, password)

    await message.reply_document(
        zip_path,
        caption=f"🔐 File zipped with password. Password sent in DM."
    )
    try:
        await message.from_user.send_message(f"🔐 Password for your zipped file: `{password}`")
    except:
        await message.reply_text("❗ Couldn't send password in DM. Please start the bot.")

    os.remove(file)
    os.remove(zip_path)

@Client.on_message(filters.command("zip_multi"))
async def zip_multi_handler(_, message: Message):
    if not message.reply_to_message or not message.reply_to_message.media_group_id:
        await message.reply_text("❌ Please reply to a media group (album) to zip multiple files.")
        return

    files = []
    async for msg in message.chat.get_media_group(message.reply_to_message.id):
        if msg.document:
            f = await msg.download()
            files.append(f)

    if not files:
        await message.reply_text("❌ No files found to zip.")
        return

    zip_path = zip_multiple_files(files)

    await message.reply_document(
        zip_path,
        caption="✅ Multiple files zipped successfully."
    )

    for f in files:
        os.remove(f)
    os.remove(zip_path)