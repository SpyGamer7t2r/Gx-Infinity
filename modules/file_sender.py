from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import PeerIdInvalid, UserIsBlocked, UserPrivacyRestricted

@Client.on_message(filters.command(["sendfile", "sendto"]) & filters.reply)
async def send_file_to_user(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("❗ Example: `/sendfile @username` (reply to a media message)", quote=True)

    target_user = message.command[1]
    if not message.reply_to_message:
        return await message.reply("❗ Please reply to a file/photo/video to send.", quote=True)

    try:
        sent_msg = await client.copy_message(
            chat_id=target_user,
            from_chat_id=message.chat.id,
            message_id=message.reply_to_message.id
        )
        await message.reply(f"✅ Sent to {target_user} successfully.")
    except PeerIdInvalid:
        await message.reply("❌ Invalid user ID or username.")
    except UserIsBlocked:
        await message.reply("🚫 User has blocked the bot.")
    except UserPrivacyRestricted:
        await message.reply("🔒 Bot can't DM this user due to their privacy settings.")
    except Exception as e:
        await message.reply(f"⚠️ Failed to send: `{e}`")
