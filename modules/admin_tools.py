# modules/admin_tools.py

from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
from config import PREFIX

async def is_admin(client, message):
    member = await client.get_chat_member(message.chat.id, message.from_user.id)
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

@Client.on_message(filters.command(["ban", "kick", "mute"], prefixes=PREFIX) & filters.group)
async def admin_commands(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("❌ You must be an admin to use this command.")

    if not message.reply_to_message:
        return await message.reply("⚠️ Please reply to a user to perform this action.")

    target_user = message.reply_to_message.from_user.id
    command = message.command[0]

    try:
        if command == "ban":
            await client.ban_chat_member(message.chat.id, target_user)
            await message.reply("🔨 User has been banned.")
        elif command == "kick":
            await client.ban_chat_member(message.chat.id, target_user)
            await client.unban_chat_member(message.chat.id, target_user)
            await message.reply("👢 User has been kicked.")
        elif command == "mute":
            await client.restrict_chat_member(
                message.chat.id,
                target_user,
                permissions=None
            )
            await message.reply("🔇 User has been muted.")
    except Exception as e:
        await message.reply(f"⚠️ Failed: {e}")

@Client.on_message(filters.command("unban", prefixes=PREFIX) & filters.group)
async def unban_user(client, message: Message):
    if not await is_admin(client, message):
        return await message.reply("❌ You must be an admin to unban.")

    if not message.reply_to_message:
        return await message.reply("⚠️ Reply to a banned user.")

    try:
        await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await message.reply("✅ User unbanned.")
    except Exception as e:
        await message.reply(f"⚠️ Error: {e}")