# modules/callback_handler.py

from pyrogram import filters from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton from pyrogram.enums import ParseMode

from main import app

@app.on_message(filters.command("cmds")) async def cmds_handler(_, message: Message): await message.reply( "<b>ᴄᴏᴍᴘʟᴇᴛᴇ ᴄᴍᴅs ᴍᴇɴᴜ ғᴏʀ ɪɴғɪɴɪᴛʏ ᴀɪ</b>", reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("🗜️ ᴢɪᴘ", callback_data="zip_menu"), InlineKeyboardButton("📂 ᴜɴᴢɪᴘ", callback_data="unzip_menu"), ], [ InlineKeyboardButton("🔐 ᴘᴀssᴡᴏʀᴅ", callback_data="password_menu"), InlineKeyboardButton("📥 ᴅᴏᴡɴʟᴏᴀᴅ", callback_data="download_menu"), ], [ InlineKeyboardButton("🧠 ᴀɪ ʙʀᴀɪɴs", callback_data="brain_menu"), InlineKeyboardButton("📊 sᴛᴀᴛs", callback_data="stats_menu"), ], [ InlineKeyboardButton("🎮 ɢᴀᴍᴇs", callback_data="games_menu"), InlineKeyboardButton("🧩 sᴛᴜᴅʏ ᴀssɪsᴛ", callback_data="study_menu"), ], [ InlineKeyboardButton("🛠️ ᴀᴅᴍɪɴ", callback_data="admin_menu"), InlineKeyboardButton("🚨 ʀᴇᴘᴏʀᴛs", callback_data="report_menu"), ], [ InlineKeyboardButton("🔎 sᴏᴄɪᴀʟ sᴄᴀɴ", callback_data="osint_menu"), InlineKeyboardButton("🌐 ᴛʀᴀɴsʟᴀᴛᴇ", callback_data="translate_menu"), ], [ InlineKeyboardButton("📻 ᴍᴜsɪᴄ", callback_data="music_menu"), InlineKeyboardButton("🖼️ sᴛɪᴄᴋᴇʀs", callback_data="sticker_menu"), ], [ InlineKeyboardButton("🔧 ᴏᴛʜᴇʀs", callback_data="others_menu"), InlineKeyboardButton("📜 ʀᴜʟᴇs", callback_data="rules_menu"), ], [ InlineKeyboardButton("🛡️ sᴜᴘᴘᴏʀᴛ / ᴏᴡɴᴇʀ", callback_data="support_menu") ] ] ), parse_mode=ParseMode.HTML )

