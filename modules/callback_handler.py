# modules/callback_handler.py

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

from main import app


@app.on_callback_query(filters.regex("zip_menu"))
async def zip_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🗜️ ᴢɪᴘ ᴄᴏᴍᴍᴀɴᴅs:\n\n"
        "/zip - 1 ғɪʟᴇ ᴢɪᴘ\n"
        "/zip_pwd - ᴢɪᴘ ᴡɪᴛʜ ᴘᴀssᴡᴏʀᴅ\n"
        "/zip_multi - ᴍᴜʟᴛɪ ᴢɪᴘ ғɪʟᴇs</b>"
    )


@app.on_callback_query(filters.regex("unzip_menu"))
async def unzip_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>📂 ᴜɴᴢɪᴘ ᴄᴏᴍᴍᴀɴᴅs:\n\n"
        "/unzip - ᴀᴜᴛᴏ ᴇxᴛʀᴀᴄᴛ\n"
        "/unzip + ᴘᴀssᴡᴏʀᴅ - ᴘᴡ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ᴢɪᴘ</b>"
    )


@app.on_callback_query(filters.regex("password_menu"))
async def password_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🔐 ᴘᴀssᴡᴏʀᴅ ᴄᴏᴍᴍᴀɴᴅs:\n\n"
        "/genpwd - ʀᴀɴᴅᴏᴍ ᴘᴀssᴡᴏʀᴅ\n"
        "/extend - sᴇssɪᴏɴ ᴛɪᴍᴇ ɪɴᴄʀᴇᴀsᴇ\n"
        "/reduce - ᴅᴇᴄʀᴇᴀsᴇ sᴇssɪᴏɴ ᴛɪᴍᴇ</b>"
    )


@app.on_callback_query(filters.regex("download_menu"))
async def download_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>📥 ᴅᴏᴡɴʟᴏᴀᴅ ᴄᴍᴅs:\n\n"
        "/yt [ʟɪɴᴋ] - ʏᴏᴜᴛᴜʙᴇ\n"
        "/insta [ʟɪɴᴋ] - ɪɴsᴛᴀ\n"
        "/fb [ʟɪɴᴋ] - ғᴀᴄᴇʙᴏᴏᴋ</b>"
    )


@app.on_callback_query(filters.regex("brain_menu"))
async def brain_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🧠 ᴀɪ ʙʀᴀɪɴs:\n\n"
        "/setbrain - ᴄʜᴀɴɢᴇ ᴀɪ\n"
        "/setmood - ᴄʜᴀɴɢᴇ ᴍᴏᴏᴅ\n"
        "/chat - sᴛᴀʀᴛ ᴀɪ ᴄʜᴀᴛ</b>"
    )


@app.on_callback_query(filters.regex("stats_menu"))
async def stats_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>📊 sᴛᴀᴛs & ɪɴғᴏ:\n\n"
        "/stats - ᴜsᴇʀ ᴅᴀᴛᴀ\n"
        "/top - ᴛᴏᴘ ᴜsᴇʀs\n"
        "/groupstats - ɢʀᴏᴜᴘ ʟᴇᴠᴇʟ</b>"
    )


@app.on_callback_query(filters.regex("games_menu"))
async def games_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🎮 ɢᴀᴍᴇs ᴍᴏᴅᴇ:\n\n"
        "/guess - ᴡᴏʀᴅ ɢᴀᴍᴇ\n"
        "/hangman - ʜᴀɴɢᴍᴀɴ\n"
        "/quiz - sᴘᴇᴇᴅ ǫᴜɪᴢ</b>"
    )


@app.on_callback_query(filters.regex("study_menu"))
async def study_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🧩 sᴛᴜᴅʏ ᴀssɪsᴛᴀɴᴛ:\n\n"
        "/notes - ᴀᴅᴅ / ɢᴇᴛ\n"
        "/reminder - ʀᴇᴍɪɴᴅ\n"
        "/pdfgen - ᴅᴏᴄ ᴄʀᴇᴀᴛᴇ</b>"
    )


@app.on_callback_query(filters.regex("admin_menu"))
async def admin_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🛠️ ᴀᴅᴍɪɴ ᴛᴏᴏʟs:\n\n"
        "/ban, /kick, /mute\n"
        "/gbanall, /banall - ᴄʀᴀᴢʏ ᴘᴏᴡᴇʀ\n"
        "/rules - ʀᴜʟᴇs ᴘᴏsᴛ</b>"
    )


@app.on_callback_query(filters.regex("report_menu"))
async def report_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🚨 ʀᴇᴘᴏʀᴛ ᴏᴘᴛɪᴏɴs:\n\n"
        "/report - ʀᴇᴘᴏʀᴛ ᴍᴇssᴀɢᴇ\n"
        "/feedback - sᴇɴᴅ ᴍᴇssᴀɢᴇ</b>"
    )


@app.on_callback_query(filters.regex("osint_menu"))
async def osint_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🔎 sᴏᴄɪᴀʟ sᴄᴀɴ:\n\n"
        "/scan @ᴜsᴇʀ\n"
        "/emailchk - ᴇᴍᴀɪʟ sᴄᴀɴ\n"
        "/usernamechk - ᴜsᴇʀɴᴀᴍᴇ ᴛʀᴀᴄᴋ</b>"
    )


@app.on_callback_query(filters.regex("translate_menu"))
async def translate_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🌐 ᴛʀᴀɴsʟᴀᴛᴇ ᴍᴏᴅᴇ:\n\n"
        "/tr hi/en/fr - ᴀᴜᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ\n"
        "/setlang - ᴅᴇғᴀᴜʟᴛ ʟᴀɴɢᴜᴀɢᴇ</b>"
    )


@app.on_callback_query(filters.regex("music_menu"))
async def music_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>📻 ᴍᴜsɪᴄ ᴍᴏᴅᴇ:\n\n"
        "/play - ᴘʟᴀʏ sᴏɴɢ\n"
        "/playlist - ʟɪsᴛ\n"
        "/stop - sᴛᴏᴘ</b>"
    )


@app.on_callback_query(filters.regex("sticker_menu"))
async def sticker_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🖼️ sᴛɪᴄᴋᴇʀ ᴍᴏᴅᴇ:\n\n"
        "/sticker - ɢᴇɴ\n"
        "/stpack - ᴄʀᴇᴀᴛᴇ\n"
        "/emojify - ᴛᴇxᴛ ➜ sᴛɪᴄᴋᴇʀ</b>"
    )


@app.on_callback_query(filters.regex("others_menu"))
async def others_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🔧 ᴏᴛʜᴇʀs:\n\n"
        "/ghostping - sᴘᴀᴍ ᴘɪɴɢ\n"
        "/tagall - ᴀʟʟ ᴛᴀɢ\n"
        "/scanfile - ғɪʟᴇ sᴄᴀɴ</b>"
    )


@app.on_callback_query(filters.regex("rules_menu"))
async def rules_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>📜 ʀᴜʟᴇs:\n\n"
        "1. ᴅᴏɴᴛ sᴘᴀᴍ\n"
        "2. ᴅᴏɴᴛ ᴀʙᴜsᴇ ʙᴏᴛ\n"
        "3. ᴇɴᴊᴏʏ ᴘᴇᴀᴄᴇғᴜʟʟʏ</b>"
    )


@app.on_callback_query(filters.regex("support_menu"))
async def support_menu_cb(_, query: CallbackQuery):
    await query.message.edit_text(
        "<b>🛡️ sᴜᴘᴘᴏʀᴛ / ᴏᴡɴᴇʀ:\n\n"
        "👤 Owner: @DarkGamer7t2rI\n"
        "💬 Group: @Ufff_Ye_Aadaye\n"
        "🌐 GitHub: github.com/hehe</b>"
    )