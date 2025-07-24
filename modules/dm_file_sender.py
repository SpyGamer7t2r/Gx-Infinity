# modules/dm_file_sender.py

from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid, UserIsBlocked
from pyrogram.types import Message
from utils.helpers import send_message_with_buttons

@Client.on_message(filters.command(["sendfile", "send_file"]) & filters.private)
async def send_file_to_dm(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.document:
        await message.reply_text("❗ Reply to a file/document you want me to send to someone’s DM.\n\nFormat:\n`/sendfile @username`")
        return

    if len(message.command) < 2:
        await message.reply_text("⚠️ Please provide a valid username.\n\nExample:\n`/sendfile @username`")
        return

    target_user = message.command[1].strip()
    doc = message.reply_to_message.document

    try:
        sent = await client.send_document(
            chat_id=target_user,
            document=doc.file_id,
            caption=f"📁 File shared by: [{message.from_user.first_name}](tg://user?id={message.from_user.id})"
        )
        await message.reply_text("✅ File successfully sent to their DM.")
    except PeerIdInvalid:
        await message.reply_text("❌ Unable to send. Invalid username or user not found.")
    except UserIsBlocked:
        await message.reply_text("🚫 I can't message this user. They may have blocked the bot.")
    except Exception as e:
        await message.reply_text(f"⚠️ Failed to send file: `{e}`")