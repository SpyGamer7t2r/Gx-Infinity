from pyrogram import Client, filters
from pyrogram.types import Message
from utils.zipper import zip_file, zip_with_password, zip_multiple_files
from utils.password_gen import generate_password
import os

@Client.on_message(filters.command("zip") & filters.reply)
async def zip_single_file(client, message: Message):
    replied = message.reply_to_message

    if not replied or not replied.document:
        return await message.reply("❌ Please reply to a file to zip it.")

    file_path = await replied.download()
    zip_path = zip_file(file_path)
    await message.reply_document(zip_path)

    os.remove(file_path)
    os.remove(zip_path)

@Client.on_message(filters.command("zip_pwd") & filters.reply)
async def zip_file_with_password(client, message: Message):
    replied = message.reply_to_message

    if not replied or not replied.document:
        return await message.reply("❌ Please reply to a file to zip it with password.")

    password = message.command[1] if len(message.command) > 1 else generate_password()

    file_path = await replied.download()
    zip_path = zip_with_password(file_path, password)

    await message.reply_document(zip_path)
    await message.reply(f"🔐 Password: `{password}`", quote=True)

    os.remove(file_path)
    os.remove(zip_path)

@Client.on_message(filters.command("zip_multi") & filters.reply)
async def zip_multiple(client, message: Message):
    if not message.reply_to_message.media_group_id:
        return await message.reply("❌ Please reply to a media group (album) containing multiple files.")

    media_group = await client.get_media_group(message.chat.id, message.reply_to_message.message_id)

    file_paths = []
    for media in media_group:
        if media.document:
            file_paths.append(await media.download())

    if not file_paths:
        return await message.reply("❌ No valid files found in the media group.")

    zip_path = zip_multiple_files(file_paths)
    await message.reply_document(zip_path)

    for path in file_paths:
        os.remove(path)
    os.remove(zip_path)