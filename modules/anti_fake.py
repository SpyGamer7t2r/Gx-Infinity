from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message
import time

FAKE_ACCOUNTS_DAYS = 3  # Minimum account age in days

@Client.on_message(filters.new_chat_members)
async def detect_fake_users(client, message: Message):
    for member in message.new_chat_members:
        user_id = member.id
        user = await client.get_users(user_id)

        if user.is_bot:
            continue

        account_created = int(user.id) >> 32  # Estimate time from Telegram ID
        current_time = int(time.time())
        account_age_days = (current_time - account_created) / 86400

        if account_age_days < FAKE_ACCOUNTS_DAYS:
            try:
                await message.chat.ban_member(user_id)
                await message.reply_text(f"🚫 Banned possible fake account: {user.mention}")
            except Exception as e:
                await message.reply_text(f"⚠️ Couldn't ban: {user.mention} - {e}")
