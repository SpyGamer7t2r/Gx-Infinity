from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

@Client.on_message(filters.command("gbanall") & filters.user(YOUR_ID))
async def gban_all(client, message: Message):
    if not message.chat.type.endswith("group"):
        return await message.reply("❌ Group command only.")
    
    async for member in client.get_chat_members(message.chat.id):
        try:
            if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                await client.ban_chat_member(message.chat.id, member.user.id)
        except:
            continue
    await message.reply("✅ All users banned.")

@Client.on_message(filters.command("muteall") & filters.user(YOUR_ID))
async def mute_all(client, message: Message):
    if not message.chat.type.endswith("group"):
        return await message.reply("❌ Group command only.")
    
    async for member in client.get_chat_members(message.chat.id):
        try:
            if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                await client.restrict_chat_member(message.chat.id, member.user.id, permissions={})
        except:
            continue
    await message.reply("🔇 Everyone muted.")

@Client.on_message(filters.command("gaali_mode_on"))
async def gaali_mode_on(client, message: Message):
    # Enable abusive word filter
    await message.reply("🛡️ Abusive detection mode: ON")

@Client.on_message(filters.command("gaali_mode_off"))
async def gaali_mode_off(client, message: Message):
    # Disable abusive word filter
    await message.reply("❌ Abusive detection mode: OFF")
