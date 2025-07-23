from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

abusive_words = ["chutiya", "bhosdike", "madarchod", "gandu", "randi", "lodu", "lavde"]  # Add more as needed

@Client.on_message(filters.text & filters.group)
async def abuse_filter(client: Client, message: Message):
    text = message.text.lower()
    if any(word in text for word in abusive_words):
        try:
            await message.delete()
            await message.reply("🛑 Abuse Detected! You're muted automatically. 😎")
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                permissions={}
            )
        except Exception as e:
            print(f"BanHammer error: {e}")


@Client.on_message(filters.command(["banall"]) & filters.user(OWNER_ID))
async def ban_all_users(client: Client, message: Message):
    chat_id = message.chat.id
    async for user in client.get_chat_members(chat_id):
        try:
            await client.ban_chat_member(chat_id, user.user.id)
        except:
            continue
    await message.reply("🚷 All users banned (admin only).")


@Client.on_message(filters.command(["muteall"]) & filters.user(OWNER_ID))
async def mute_all_users(client: Client, message: Message):
    chat_id = message.chat.id
    async for user in client.get_chat_members(chat_id):
        try:
            await client.restrict_chat_member(chat_id, user.user.id, permissions={})
        except:
            continue
    await message.reply("🔇 All users muted (admin only).")


@Client.on_message(filters.command(["gbanall"]) & filters.user(OWNER_ID))
async def gban_all(client: Client, message: Message):
    # This is only symbolic unless connected to global ban system
    await message.reply("🌐 Global Ban system activated (not implemented fully)")
