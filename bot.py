import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# ➕ Modules
from modules.fun_stats import update_user_stats
from modules.auto_reply_modes import auto_reply
import modules.reaction_handler
from modules.nsfw_guard import scan_nsfw
from modules.brain import generate_ai_response
from modules.voice_to_text import voice_to_text_handler
from modules.cmds import show_cmds, cmds_callback  # ✅ ADDED

load_dotenv()

# 🌐 𝙴𝙽𝚅 𝙲𝙾𝙽𝙵𝙸𝙶
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "InfinityAIBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

# 🔧 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝙳𝙰𝚃𝙰
FEATURES = {
    "🧠 AI Chat": {
        "description": "🤖 ᴛᴀʟᴋ ᴡɪᴛʜ ᴀɪ, ᴍᴏᴏᴅ-ʙᴀsᴇᴅ ʀᴇᴘʟɪᴇs, ᴛʀᴀɴsʟᴀᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ.",
        "commands": ["/chat", "/mood", "/setmood"]
    },
    "📦 Zip Tools": {
        "description": "🔐 ᴢɪᴘ/ᴜɴᴢɪᴘ ғɪʟᴇs, ᴘᴀssᴡᴏʀᴅ ᴘʀᴏᴛᴇᴄᴛ, ᴍᴜʟᴛɪғɪʟᴇ.",
        "commands": ["/zip", "/zip_pwd", "/unzip"]
    },
    "🎵 Music Player": {
        "description": "🎧 /play, /pause, /resume, /skip, ʀᴇᴀʟ-ᴛɪᴍᴇ.",
        "commands": ["/play", "/pause", "/resume", "/skip"]
    },
    "⚙️ Mood/Settings": {
        "description": "💫 sᴇᴛ ᴍᴏᴏᴅs (ғᴜɴɴʏ, ʀᴏᴍᴀɴᴛɪᴄ), ᴀɪ ᴄᴜsᴛᴏᴍ.",
        "commands": ["/mood", "/setmood", "/settings"]
    },
    "🚫 NSFW Filter": {
        "description": "🛡️ sᴄᴀɴ/ʙʟᴏᴄᴋ ɴsғᴡ ᴍᴇᴅɪᴀ.",
        "commands": ["/nsfw_on", "/nsfw_off"]
    },
    "⏰ Reminders": {
        "description": "📌 ʀᴇᴍɪɴᴅᴇʀs, ᴀʟᴀʀᴍs, sᴄʜᴇᴅᴜʟᴇs.",
        "commands": ["/remind", "/alarm"]
    },
    "🎮 Fun Games": {
        "description": "🎲 ᴛʀɪᴠɪᴀ, ᴡᴏʀᴅɢᴀᴍᴇ, ʜᴀɴɢᴍᴀɴ.",
        "commands": ["/trivia", "/wordgame", "/hangman"]
    },
    "🔍 OSINT Tools": {
        "description": "🧾 ᴛɢ/ɪɴsᴛᴀ/ʟɪɴᴋᴇᴅɪɴ sᴛᴀʟᴋɪɴɢ.",
        "commands": ["/osint", "/osint_user"]
    },
    "🌐 Translator": {
        "description": "🗣️ ᴀᴜᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ᴍsɢs.",
        "commands": ["/translate", "/autotranslate"]
    },
    "🖼️ Sticker Tools": {
        "description": "🎨 ᴄʀᴇᴀᴛᴇ/ᴍᴀɴᴀɢᴇ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋs.",
        "commands": ["/sticker", "/stickerpack"]
    }
}

# 🔘 𝙼𝙰𝙸𝙽 𝙱𝚄𝚃𝚃𝙾𝙽𝚂
def main_buttons():
    rows = []
    keys = list(FEATURES.keys())
    for i in range(0, len(keys), 2):
        row = []
        for j in range(2):
            if i + j < len(keys):
                key = keys[i + j]
                row.append(InlineKeyboardButton(key, callback_data=f"feat_{key.replace(' ', '_')}"))
        rows.append(row)
    rows.append([InlineKeyboardButton("📜 All Commands", callback_data="cmds_0")])
    return InlineKeyboardMarkup(rows)

def feature_back_button():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="menu")]])

# ▶️ 𝚂𝚃𝙰𝚁𝚃
@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        "✨ ʜᴇʟʟᴏ, ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɪɴғɪɴɪᴛʏ ᴀɪ ʙᴏᴛ ✨\n\n"
        "💡 ᴀ sᴍᴀʀᴛ, ᴀᴜᴛᴏ-ʀᴇsᴘᴏɴsɪᴠᴇ, sᴛʏʟɪsʜ ᴍᴜʟᴛɪғᴇᴀᴛᴜʀᴇ ʙᴏᴛ.\n\n"
        "🔍 ᴇxᴘʟᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ʙᴇʟᴏᴡ:",
        reply_markup=main_buttons()
    )

@app.on_message(filters.command("menu") & filters.private)
async def menu_handler(client, message: Message):
    await start_handler(client, message)

# 🔁 𝙲𝙰𝙻𝙻𝙱𝙰𝙲𝙺𝚂
@app.on_callback_query()
async def callback_handler(client, cq):
    data = cq.data

    if data.startswith("cmds_"):
        await cmds_callback(client, cq)
        return

    if data.startswith("feat_"):
        feat_name = data[5:].replace("_", " ")
        feat = FEATURES.get(feat_name)
        if feat:
            cmds = "\n".join(feat["commands"])
            msg = f"**{feat_name}**\n\n{feat['description']}\n\n**Commands:**\n{cmds}"
            await cq.message.edit_text(msg, reply_markup=feature_back_button())
        else:
            await cq.answer("Unknown Feature")

    elif data == "menu":
        await cq.message.edit_text(
            "✨ **ɪɴғɪɴɪᴛʏ ᴀɪ ғᴇᴀᴛᴜʀᴇs** ✨\n\n💡 ᴛᴀᴘ ᴀɴʏ ғᴇᴀᴛᴜʀᴇ ᴛᴏ sᴇᴇ ᴄᴍᴅs:",
            reply_markup=main_buttons()
        )
    else:
        await cq.answer()

# 🧾 𝙲𝙼𝙳𝚂
@app.on_message(filters.command("cmds") & (filters.private | filters.group))
async def cmds_panel(client, message: Message):
    await show_cmds(client, message)

# 🧠 𝙼𝙰𝙸𝙽 𝙰𝙸 𝙷𝙰𝙽𝙳𝙻𝙴𝚁
@app.on_message(filters.text & (filters.private | filters.group) & ~filters.command(["start", "menu", "cmds"]))
async def main_message_handler(client, message: Message):
    await update_user_stats(user_id=message.from_user.id)
    await modules.reaction_handler.auto_react(client, message)
    await auto_reply(message)

    if message.voice:
        await voice_to_text_handler(message)
        return

    if await scan_nsfw(message):
        return

    reply = await generate_ai_response(message)
    if reply:
        await message.reply_text(reply)

# 🚀 𝚁𝚄𝙽
if __name__ == "__main__":
    print("🚀 Infinity AI Bot is running...")
    app.run()