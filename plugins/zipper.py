# InfinityAI_bot/plugins/zipper.py

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.zipper import zip_file, zip_with_password, zip_multiple_files
from utils.password_gen import generate_password
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

user_file_cache = {}

@Client.on_message(filters.command("zip") & filters.reply)
async def zip_single_file(client, message: Message):
    replied = message.reply_to_message
    if not replied.document:
        return await message.reply("❌ Please reply to a file to zip it.")
    
    file = await client.download_media(replied)
    zipped = zip_file(file)

    await message.reply_document(zipped, caption="✅ Zipped file created.")
    os.remove(file)
    os.remove(zipped)


@Client.on_message(filters.command("zip_pwd") & filters.reply)
async def zip_with_pwd(client, message: Message):
    replied = message.reply_to_message
    if not replied.document:
        return await message.reply("❌ Please reply to a file to zip with password.")

    file = await client.download_media(replied)
    password = generate_password()
    zipped = zip_with_password(file, password)

    await message.reply_document(zipped, caption="🔐 Password-protected zip created.")

    # Send password in DM
    try:
        await client.send_message(message.from_user.id, f"🔑 Your zip password: `{password}`")
    except:
        await message.reply("❗ Couldn't send password in DM. Please start me in private.")
    
    os.remove(file)
    os.remove(zipped)


@Client.on_message(filters.command("zip_multi"))
async def collect_multi_files(client, message: Message):
    user_id = message.from_user.id
    args = message.text.split()

    if len(args) < 2 or args[1].lower() not in ["start", "done"]:
        return await message.reply("❗ Usage: `/zip_multi start` to begin, `/zip_multi done` to zip all.")

    action = args[1].lower()

    if action == "start":
        user_file_cache[user_id] = []
        await message.reply("📥 Now send me all the files one by one. When done, send `/zip_multi done`.")

    elif action == "done":
        if user_id not in user_file_cache or not user_file_cache[user_id]:
            return await message.reply("❌ No files collected yet.")
        
        zip_path = zip_multiple_files(user_file_cache[user_id])

        await message.reply_document(zip_path, caption="📦 Multi-file zip created.")
        for f in user_file_cache[user_id]:
            os.remove(f)
        os.remove(zip_path)
        user_file_cache[user_id] = []


@Client.on_message(filters.document)
async def store_files_for_multi_zip(client, message: Message):
    user_id = message.from_user.id
    if user_id in user_file_cache:
        file = await client.download_media(message)
        user_file_cache[user_id].append(file)
        await message.reply("✅ File received for multi-zip.")