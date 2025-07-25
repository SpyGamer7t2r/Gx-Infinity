# modules/callback_handler.py

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_callback_query()
async def callback_handler(client: Client, callback_query: CallbackQuery):
    data = callback_query.data

    if data == "zip_help":
        await callback_query.message.edit_text(
            "🗜 <b>ᴢɪᴘ ᴍᴏᴅᴜʟᴇ ʜᴇʟᴘ</b>\n"
            "➤ /zip - ᴄᴏᴍᴘʀᴇss ғɪʟᴇ\n"
            "➤ /zip_pwd - ᴘᴀssᴡᴏʀᴅ ᴢɪᴘ\n"
            "➤ /zip_multi - ᴍᴜʟᴛɪ ғɪʟᴇ ᴢɪᴘ\n"
            "➤ /unzip - ᴇxᴛʀᴀᴄᴛ ғɪʟᴇ",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="home")]
            ])
        )

    elif data == "music_help":
        await callback_query.message.edit_text(
            "🎵 <b>ᴍᴜsɪᴄ ᴄᴏᴍᴍᴀɴᴅs</b>\n"
            "➤ /play [ɴᴀᴍᴇ/ʟɪɴᴋ]\n"
            "➤ /pause /resume /skip /stop\n"
            "➤ /playlist - sᴀᴠᴇᴅ sᴏɴɢs",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="home")]
            ])
        )

    elif data == "games_help":
        await callback_query.message.edit_text(
            "🎮 <b>ɢᴀᴍᴇ ᴄᴏᴍᴍᴀɴᴅs</b>\n"
            "➤ /hangman /scramble /guess /ladder\n"
            "➤ /wordbattle /synonym /typing\n"
            "➤ /chain /generate /quiz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="home")]
            ])
        )

    elif data == "tools_help":
        await callback_query.message.edit_text(
            "🧰 <b>ᴛᴏᴏʟs + sᴜᴘᴘᴏʀᴛᴇᴅ ғᴇᴀᴛᴜʀᴇs</b>\n"
            "➤ /genpwd /translate /reminder\n"
            "➤ /voice /compare /sticker /report\n"
            "➤ /docgen /notes /osint",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="home")]
            ])
        )

    elif data == "admin_help":
        await callback_query.message.edit_text(
            "🛠 <b>ᴀᴅᴍɪɴ + sᴀғᴇᴛʏ</b>\n"
            "➤ /ban /mute /kick /gbanall\n"
            "➤ /gaalimode /clean /tagall /stats",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="home")]
            ])
        )

    elif data == "home":
        await callback_query.message.edit_text(
            "🏠 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɪɴғɪɴɪᴛʏ ᴀɪ ᴍᴇɴᴜ</b>\n"
            "ᴄʜᴏᴏsᴇ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ʙᴇʟᴏᴡ ↓",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("🗜 ᴢɪᴘ", callback_data="zip_help"),
                    InlineKeyboardButton("🎵 ᴍᴜsɪᴄ", callback_data="music_help")
                ],
                [
                    InlineKeyboardButton("🎮 ɢᴀᴍᴇs", callback_data="games_help"),
                    InlineKeyboardButton("🧰 ᴛᴏᴏʟs", callback_data="tools_help")
                ],
                [
                    InlineKeyboardButton("🛠 ᴀᴅᴍɪɴ", callback_data="admin_help"),
                    InlineKeyboardButton("❓ sᴜᴘᴘᴏʀᴛ", url="https://t.me/your_support")
                ]
            ]),
            disable_web_page_preview=True
        )

    else:
        await callback_query.answer("❌ ᴜɴᴋɴᴏᴡɴ ʙᴜᴛᴛᴏɴ ᴄʟɪᴄᴋᴇᴅ!", show_alert=True)