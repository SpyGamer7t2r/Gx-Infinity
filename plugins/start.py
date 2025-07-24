# InfinityAI_bot/plugins/start.py

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_USERNAME

START_TEXT = """
👋 Hello! I'm <b>Infinity AI</b> — your ultimate all-in-one assistant!  
I can help with:
• 💬 AI Chatting  
• 🛠 Admin Tools  
• 🎵 Music + Video  
• 📂 Zip/Unzip Files  
• 🎮 Games & Trivia  
• 📥 Downloads  
• 💡 Coding Help  
• 🤖 OSINT & Info Tracing  
• 🎭 Meme/Sticker Creation  
• 🗂 Notes, Reminders & More!

Type <code>/help</code> to see all commands.
"""

HELP_TEXT = """
<b>📚 Infinity AI Commands:</b>

• <b>💬 AI:</b> Just message me or reply with text to start AI chat  
• <b>/zip, /unzip</b> - Compress or extract files  
• <b>/genpwd</b> - Generate secure password  
• <b>/play, /pause</b> - Music control  
• <b>/remind</b> - Set reminders  
• <b>/note, /get</b> - Save and get notes  
• <b>/osint, /userinfo</b> - User tracking tools  
• <b>/mode, /brain</b> - Switch AI brain/personality  
• <b>/ban, /kick</b> - Admin control  
• <b>/sticker</b> - Create stickers from photo/text  
• <b>/download</b> - Download from YouTube, IG, etc.  
• <b>/games</b> - Start word & brain games

More coming soon...

<b>👑 Owner:</b> @{OWNER}
""".replace("{OWNER}", OWNER_USERNAME)

@Client.on_message(filters.command(["start", "alive"]))
async def start_cmd(_, message: Message):
    await message.reply_text(
        START_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Help", callback_data="show_help")],
            [InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_USERNAME}")]
        ])
    )

@Client.on_callback_query(filters.regex("show_help"))
async def show_help_callback(client, callback_query):
    await callback_query.message.edit_text(
        HELP_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="back_start")]
        ])
    )

@Client.on_callback_query(filters.regex("back_start"))
async def back_start_callback(client, callback_query):
    await callback_query.message.edit_text(
        START_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Help", callback_data="show_help")],
            [InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_USERNAME}")]
        ])
                                 )
