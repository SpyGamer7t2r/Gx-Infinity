# modules/admin_tools.py

from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID
from utils.helpers import send_message_with_buttons

async def handle_admin_commands(client, message: Message):
    if message.text.startswith("/banall"):
        if message.from_user.id != OWNER_ID:
            await message.reply_text("🚫 Sirf owner hi ye command chala sakta hai.")
            return

        chat = message.chat
        banned = 0
        async for member in client.get_chat_members(chat.id):
            try:
                if member.user.id != OWNER_ID:
                    await client.ban_chat_member(chat.id, member.user.id)
                    banned += 1
            except:
                continue

        await message.reply_text(f"✅ {banned} members banned successfully!")

    elif message.text.startswith("/gbanall"):
        if message.from_user.id != OWNER_ID:
            await message.reply_text("🚫 Sirf owner hi ye command chala sakta hai.")
            return

        banned = 0
        for dialog in await client.get_dialogs():
            try:
                await client.ban_chat_member(dialog.chat.id, message.reply_to_message.from_user.id)
                banned += 1
            except:
                continue
        await message.reply_text(f"✅ Global ban complete: {banned} chats.")

    elif message.text.startswith("/muteall"):
        if message.from_user.id != OWNER_ID:
            await message.reply_text("🚫 Permission denied.")
            return
        chat = message.chat
        muted = 0
        async for member in client.get_chat_members(chat.id):
            try:
                if member.user.id != OWNER_ID:
                    await client.restrict_chat_member(chat.id, member.user.id, permissions={})
                    muted += 1
            except:
                continue
        await message.reply_text(f"🔇 {muted} members muted.")

    elif message.text.startswith("/kickall"):
        if message.from_user.id != OWNER_ID:
            await message.reply_text("🚫 Permission denied.")
            return
        chat = message.chat
        kicked = 0
        async for member in client.get_chat_members(chat.id):
            try:
                if member.user.id != OWNER_ID:
                    await client.kick_chat_member(chat.id, member.user.id)
                    kicked += 1
            except:
                continue
        await message.reply_text(f"👢 {kicked} members kicked from group.")