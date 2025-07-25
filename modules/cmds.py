from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType

# Command categories and their UI buttons
def get_cmds_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🤖 ʙʀᴀɪɴ", callback_data="cmd_ai")],
        [InlineKeyboardButton("🎵 ᴍᴜꜱɪᴄ", callback_data="cmd_music"),
         InlineKeyboardButton("🗂️ ᴢɪᴘ", callback_data="cmd_zip")],
        [InlineKeyboardButton("🧠 ᴍᴏᴏᴅ", callback_data="cmd_mood"),
         InlineKeyboardButton("🛡️ ꜱᴇᴄᴜʀɪᴛʏ", callback_data="cmd_nsfw")],
        [InlineKeyboardButton("🛍️ ᴄᴏᴍᴘᴀʀᴇ", callback_data="cmd_prod"),
         InlineKeyboardButton("🔎 ᴅᴏᴡɴʟᴏᴀᴅ", callback_data="cmd_down")],
        [InlineKeyboardButton("🎮 ɢᴀᴍᴇꜱ", callback_data="cmd_game"),
         InlineKeyboardButton("📊 ꜱᴛᴀᴛꜱ", callback_data="cmd_stats")],
        [InlineKeyboardButton("🎓 ꜱᴛᴜᴅʏ", callback_data="cmd_study"),
         InlineKeyboardButton("🗣️ ᴠᴏɪᴄᴇ", callback_data="cmd_voice")],
        [InlineKeyboardButton("👨‍💻 ᴄᴏᴅɪɴɢ", callback_data="cmd_code"),
         InlineKeyboardButton("🎭 ꜰᴜɴ", callback_data="cmd_fun")],
        [InlineKeyboardButton("👮 ᴀᴅᴍɪɴ", callback_data="cmd_admin")],
    ])

# Category titles
title_fonts = {
    "ai": "🤖 <b><u>ʙʀᴀɪɴꜱ + ᴀɪ ᴄʜᴀᴛ</u></b>",
    "music": "🎵 <b><u>ᴍᴜꜱɪᴄ & ᴘʟᴀʏʟɪꜱᴛ</u></b>",
    "zip": "🗂️ <b><u>ᴢɪᴘ / ᴜɴᴢɪᴘ ᴛᴏᴏʟꜱ</u></b>",
    "mood": "🧠 <b><u>ᴍᴏᴏᴅ + ᴘᴇʀꜱᴏɴᴀʟɪᴛʏ</u></b>",
    "nsfw": "🛡️ <b><u>ꜱᴇᴄᴜʀɪᴛʏ / ꜰɪʟᴛᴇʀꜱ</u></b>",
    "prod": "🛍️ <b><u>ᴘʀᴏᴅᴜᴄᴛ ᴄᴏᴍᴘᴀʀᴇ</u></b>",
    "down": "🔎 <b><u>ᴍᴇᴅɪᴀ ᴅᴏᴡɴʟᴏᴀᴅᴇʀꜱ</u></b>",
    "game": "🎮 <b><u>ɢᴀᴍᴇꜱ & ʙᴀᴛᴛʟᴇꜱ</u></b>",
    "stats": "📊 <b><u>ᴜꜱᴇʀ ꜱᴛᴀᴛꜱ + ᴅᴀᴛᴀ</u></b>",
    "study": "🎓 <b><u>ꜱᴛᴜᴅʏ / ɴᴏᴛᴇꜱ</u></b>",
    "voice": "🗣️ <b><u>ᴠᴏɪᴄᴇ ᴛᴏᴏʟꜱ</u></b>",
    "code": "👨‍💻 <b><u>ᴄᴏᴅɪɴɢ + ᴅᴏᴄꜱ</u></b>",
    "fun": "🎭 <b><u>ꜰᴜɴ + ʀᴇᴀᴄᴛɪᴏɴꜱ</u></b>",
    "admin": "👮 <b><u>ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ</u></b>"
}

# Command sets
cmd_descriptions = {
    "cmd_ai": """
/ʜᴇʟʟᴏ - ᴡᴀᴋᴇ ᴜᴘ ᴀɪ  
/ʙʀᴀɪɴ - ꜱᴡɪᴛᴄʜ ᴀɪ ʙʀᴀɪɴ  
/ʟᴀɴɢ - ᴀᴜᴛᴏ ʀᴇᴘʟʏ ʟᴀɴɢ  
/ᴄʜᴀᴛ - ꜱᴍᴀʀᴛ ᴄᴏɴᴠᴏ
    """,
    "cmd_music": """
/ᴘʟᴀʏ - ꜱᴏɴɢ ꜱᴇᴀʀᴄʜ  
/ᴘʟᴀʏʟɪꜱᴛ - ᴘʀɪᴠᴀᴛᴇ ʟɪꜱᴛ  
/ᴠᴘʟᴀʏ - ᴠɪᴅᴇᴏ ꜱᴛʀᴇᴀᴍ  
/ꜱᴛᴏᴘ - ꜱᴛᴏᴘ ᴘʟᴀʏ
    """,
    "cmd_zip": """
/ᴢɪᴘ - ꜰɪʟᴇ ᴢɪᴘ  
/ᴢɪᴘ_ᴘᴡᴅ - ᴘᴀꜱꜱᴡᴏʀᴅ ᴢɪᴘ  
/ᴜɴᴢɪᴘ - ᴇxᴛʀᴀᴄᴛ  
/ɢᴇɴᴘᴡᴅ - ꜱᴛʀᴏɴɢ ᴘᴀꜱꜱ
    """,
    "cmd_mood": """
/ᴍᴏᴏᴅ - ꜱᴇᴛ ᴍᴏᴏᴅ  
/ᴍᴏᴅᴇ - ꜱᴇʟᴇᴄᴛ ᴘᴇʀꜱᴏɴᴀ  
/ʀᴇꜱᴇᴛ - ʀᴇꜱᴇᴛ ᴍᴏᴏᴅ
    """,
    "cmd_nsfw": """
/ꜱᴄᴀɴ - ɴꜱꜰᴡ ꜱᴄᴀɴ  
/ɴꜱꜰᴡᴏɴ - ᴀᴜᴛᴏ ꜱᴄᴀɴ  
/ɴꜱꜰᴡᴏꜰꜰ - ᴛᴜʀɴ ᴏꜰꜰ ꜱᴄᴀɴ
    """,
    "cmd_prod": """
/ᴄᴏᴍᴘᴀʀᴇ - ꜱʜᴏᴘ ᴄᴏᴍᴘᴀʀᴇ  
/ᴘʀɪᴄᴇ - ꜰɪɴᴅ ᴘʀɪᴄᴇ  
/ʀᴇᴠɪᴇᴡ - ɢᴇᴛ ᴜꜱᴇʀ ᴠɪᴇᴡꜱ
    """,
    "cmd_down": """
/ʏᴛ - ʏᴛ ᴅʟ  
/ɪɴꜱᴛᴀ - ʀᴇᴇʟ ᴅʟ  
/ꜱᴏɴɢ - ꜰᴀꜱᴛ ᴀᴜᴅɪᴏ ᴅʟ
    """,
    "cmd_game": """
/ᴡᴏʀᴅɢᴀᴍᴇ - ʙᴀᴛᴛʟᴇ  
/ꜱᴄʀᴀᴍʙʟᴇ - ᴡᴏʀᴅ ꜱᴄʀᴀᴍʙʟᴇ  
/ʜᴀɴɢᴍᴀɴ - ᴄʟᴜᴇ ɢᴀᴍᴇ  
/ɢᴜᴇꜱꜱ - ɢᴜᴇꜱꜱ ᴛʜᴇ ᴡᴏʀᴅ
    """,
    "cmd_stats": """
/ꜱᴛᴀᴛꜱ - ᴜꜱᴇʀ ꜱᴛᴀᴛ  
/ᴛᴏᴘ - ᴛᴏᴘ ᴜꜱᴇʀꜱ  
/ᴅᴍꜱ - ʏᴏᴜʀ ᴅᴍꜱ  
/ɢʀᴏᴜᴘ - ᴀᴄᴛɪᴠᴇ ɢʀᴘꜱ
    """,
    "cmd_study": """
/ɴᴏᴛᴇ - ꜱᴀᴠᴇ ɴᴏᴛᴇ  
/ɴᴏᴛᴇꜱ - ᴀʟʟ ꜱᴀᴠᴇᴅ  
/ᴅᴇʟᴇᴛᴇ_ɴᴏᴛᴇ - ʀᴇᴍᴏᴠᴇ  
/ʀᴇᴍɪɴᴅ - ᴛɪᴍᴇ ʀᴇᴍɪɴᴅ
    """,
    "cmd_voice": """
/ᴠᴏɪᴄᴇ - ᴠᴏɪᴄᴇ ᴛᴏ ᴛᴇxᴛ  
/ꜱᴘᴇᴀᴋ - ᴛᴇxᴛ ᴛᴏ ꜱᴘᴇᴇᴄʜ
    """,
    "cmd_code": """
/ᴄᴏᴅᴇ - ɢᴇɴᴇʀᴀᴛᴇ  
/ᴘʏ - ᴘʏᴛʜᴏɴ ᴇxᴇᴄ  
/ʜᴛᴍʟ - ᴡᴇʙ ᴄᴏᴅᴇ  
/ᴅᴏᴄ - ᴄʀᴇᴀᴛᴇ ᴘᴅꜰ
    """,
    "cmd_fun": """
/ꜱʜᴀʏᴀʀɪ - ʟᴏᴠᴇ ꜱʜᴀʏᴀʀɪ  
/ᴊᴏᴋᴇ - ꜰᴜɴɴʏ ʟɪɴᴇꜱ  
/ʀᴇᴀᴄᴛ - ʙᴏᴛ ʀᴇᴀᴄᴛꜱ  
/ᴀᴜᴛᴏ - ᴀᴜᴛᴏ ʀᴇᴘʟʏ
    """,
    "cmd_admin": """
/ʙᴀɴ, /ᴍᴜᴛᴇ, /ᴋɪᴄᴋ - ᴜꜱᴇʀ ᴍᴀɴᴀɢᴇ  
/ᴄʟᴇᴀɴ - ᴘᴜʀɢᴇ ᴄʜᴀᴛ  
/ᴛᴀɢᴀʟʟ - ᴀʟʟ ᴛᴀɢ  
/ɢʙᴀɴᴀʟʟ - ɢʟᴏʙᴀʟ ʙᴀɴ
    """
}

# /cmds handler
@Client.on_message(filters.command("cmds") & (filters.private | filters.group))
async def show_cmds(client, message: Message):
    await message.reply_text(
        "📜 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɪɴꜰɪɴɪᴛʏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ ᴘᴀɴᴇʟ</b>\nᴄʟɪᴄᴋ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ʙᴇʟᴏᴡ ⬇️",
        reply_markup=get_cmds_buttons(),
        parse_mode="HTML"
    )

# Callback handler
@Client.on_callback_query(filters.regex("cmd_"))
async def cmds_callback(client, callback_query):
    data = callback_query.data
    key = data.replace("cmd_", "")
    title = title_fonts.get(key, "📚 ᴄᴏᴍᴍᴀɴᴅꜱ")
    desc = cmd_descriptions.get(data, "No commands found.")

    formatted_text = f"""
<b>{title}</b>

{desc}

<b>ʜᴇʟʟᴏ, ɪ'ᴍ ɪɴꜰɪɴɪᴛʏ ᴀɪ</b> 🤖

🧠 <b>ᴍᴀɪ ᴍᴜʟᴛɪ-ʙʀᴀɪɴ, ᴍᴏᴏᴅ + ᴘᴇʀꜱᴏɴᴀʟɪᴛʏ ʙᴀꜱᴇᴅ ᴀɪ ʜᴜ</b> 💡

🧩 ᴜꜱᴇ /menu ᴛᴏ ᴇxᴘʟᴏʀᴇ ғᴇᴀᴛᴜʀᴇꜱ 🎮
💬 ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ, ᴀꜱᴋ ᴄᴏᴅᴇꜱ, ꜱᴇɴᴅ ғɪʟᴇꜱ, ɢᴇɴᴇʀᴀᴛᴇ ᴅᴏᴄꜱ, ᴘʀɪᴄᴇ ᴄʜᴇᴄᴋ, ᴀɴᴅ ᴍᴏʀᴇ!
"""

    await callback_query.message.edit_text(
        formatted_text,
        parse_mode="html",
        reply_markup=get_cmds_buttons()
    )