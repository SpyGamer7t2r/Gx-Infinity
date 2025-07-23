from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
import re

GBAN_LIST = set()
ABUSIVE_WORDS = {"madarchod", "bhosdike", "lodu", "chutiya", "gaand", "bkl", "mc", "bc", "randi", "haraami"}

def is_admin(member):
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

@Client.on_message(filters.command("banall") & filters.group)
async def ban_all(client, message: Message):
    if not is_admin(await client.get_chat_member(message.chat.id, message.from_user.id)):
        return await message.reply("🚫 Only admins can use this.")

    await message.reply("⛔ Banning all users (excluding admins)...")
    async for member in client.get_chat_members(message.chat.id):
        if member.user.is_bot or is_admin(member): continue
        try:
            await client.ban_chat_member(message.chat.id, member.user.id)
        except:
            continue
    await message.reply("✅ All members banned.")

@Client.on_message(filters.command("gbanall") & filters.user(OWNER_ID))  # Replace with your ID
async def gban_all(client, message: Message):
    await message.reply("🌐 GBAN initiated...")
    async for dialog in client.get_dialogs():
        try:
            async for member in client.get_chat_members(dialog.chat.id):
                if member.user.is_bot or is_admin(member): continue
                GBAN_LIST.add(member.user.id)
                await client.ban_chat_member(dialog.chat.id, member.user.id)
        except:
            continue
    await message.reply("✅ GBAN done globally.")

@Client.on_message(filters.command("muteall") & filters.group)
async def mute_all(client, message: Message):
    if not is_admin(await client.get_chat_member(message.chat.id, message.from_user.id)):
        return await message.reply("🔇 Only admins can use this.")
    await client.set_chat_permissions(message.chat.id, permissions={})
    await message.reply("🔇 Group muted for everyone!")

@Client.on_message(filters.command("kickall") & filters.group)
async def kick_all(client, message: Message):
    if not is_admin(await client.get_chat_member(message.chat.id, message.from_user.id)):
        return await message.reply("🥾 Only admins can kick.")
    async for member in client.get_chat_members(message.chat.id):
        if member.user.is_bot or is_admin(member): continue
        try:
            await client.kick_chat_member(message.chat.id, member.user.id)
        except:
            continue
    await message.reply("✅ All users kicked (non-admins).")

@Client.on_message(filters.text & filters.group)
async def abusive_detector(client, message: Message):
    text = message.text.lower()
    if any(word in text for word in ABUSIVE_WORDS):
        await message.reply("😈 Sigma says: Apni aukat me reh 🚫")
        try:
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                permissions={}
            )
        except:
            pass
