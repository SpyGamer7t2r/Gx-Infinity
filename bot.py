import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

from modules.fun_stats import update_user_stats
from modules.auto_reply_modes import auto_reply  
import modules.reaction_handler
from modules.nsfw_guard import scan_nsfw
from modules.brain import generate_ai_response
from modules.voice_to_text import voice_to_text_handler

load_dotenv()

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


FEATURES = {
    "AI Chat": {
        "description": "🤖 Talk with AI, mood-based replies, multi-language support.",
        "commands": ["/chat", "/mood", "/setmood"]
    },
    "Zip & Unzip": {
        "description": "🔐 Zip/unzip files, password protect, multi-file support.",
        "commands": ["/zip", "/zip_pwd", "/unzip", "/zip_multi"]
    },
    "Music Player": {
        "description": "🎵 Play, pause, resume, manage playlists.",
        "commands": ["/play", "/pause", "/resume", "/skip"]
    },
    "Settings & Mood": {
        "description": "⚙️ Set moods (funny, romantic), customize replies.",
        "commands": ["/mood", "/setmood", "/settings"]
    },
    "NSFW Filter": {
        "description": "🚫 Auto-scan NSFW content in groups and private chats.",
        "commands": ["/nsfw_on", "/nsfw_off"]
    },
    "Reminders": {
        "description": "⏰ Set reminders and alarms.",
        "commands": ["/remind", "/alarm", "/reminders"]
    },
    "Fun Games": {
        "description": "🎮 Trivia, word games, quizzes, and puzzles.",
        "commands": ["/trivia", "/wordgame", "/hangman"]
    },
    "OSINT Tools": {
        "description": "🔍 Extract social info from Telegram, Instagram, LinkedIn, etc.",
        "commands": ["/osint", "/osint_user"]
    },
    "Auto Translator": {
        "description": "🌐 Auto-translate foreign messages to your language.",
        "commands": ["/translate", "/autotranslate"]
    },
    "Sticker Creator": {
        "description": "🖼️ Create and manage stickers and sticker packs.",
        "commands": ["/sticker", "/stickerpack", "/stickercreate"]
    },
    # Add more features here for 100+ total
}


def build_main_menu():
    buttons = []
    for feat_name in list(FEATURES.keys())[:8]:  # First 8 features on first page
        buttons.append([InlineKeyboardButton(feat_name, callback_data=f"feat_{feat_name.replace(' ', '_')}")])
    buttons.append([InlineKeyboardButton("➡️ More", callback_data="menu_page_2")])
    return InlineKeyboardMarkup(buttons)


def build_page_2_menu():
    buttons = []
    for feat_name in list(FEATURES.keys())[8:16]:  # Next 8 features on second page
        buttons.append([InlineKeyboardButton(feat_name, callback_data=f"feat_{feat_name.replace(' ', '_')}")])
    buttons.append([
        InlineKeyboardButton("⬅️ Back", callback_data="menu_page_1"),
        InlineKeyboardButton("➡️ More", callback_data="menu_page_3")
    ])
    return InlineKeyboardMarkup(buttons)


def build_page_3_menu():
    buttons = []
    for feat_name in list(FEATURES.keys())[16:]:
        buttons.append([InlineKeyboardButton(feat_name, callback_data=f"feat_{feat_name.replace(' ', '_')}")])
    buttons.append([InlineKeyboardButton("⬅️ Back", callback_data="menu_page_2")])
    return InlineKeyboardMarkup(buttons)


def build_feature_detail_menu(feature_name):
    buttons = [[InlineKeyboardButton("⬅️ Back to menu", callback_data="menu_page_1")]]
    return InlineKeyboardMarkup(buttons)


@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    await message.reply_text(
        "🌟 Welcome to Infinity AI Bot!\n\n"
        "Use the buttons below to explore features:",
        reply_markup=build_main_menu()
    )


@app.on_message(filters.command("menu") & filters.private)
async def menu_handler(client, message: Message):
    await start_handler(client, message)


@app.on_callback_query()
async def callback_handler(client, callback_query):
    data = callback_query.data

    if data == "menu_page_1":
        await callback_query.message.edit_text(
            "🌟 Features — Page 1/3\nSelect a feature to know more:",
            reply_markup=build_main_menu()
        )
    elif data == "menu_page_2":
        await callback_query.message.edit_text(
            "🌟 Features — Page 2/3\nSelect a feature to know more:",
            reply_markup=build_page_2_menu()
        )
    elif data == "menu_page_3":
        await callback_query.message.edit_text(
            "🌟 Features — Page 3/3\nSelect a feature to know more:",
            reply_markup=build_page_3_menu()
        )
    elif data.startswith("feat_"):
        feat_name = data[5:].replace("_", " ")
        feature = FEATURES.get(feat_name)
        if feature:
            cmds = "\n".join(feature["commands"])
            text = f"**{feat_name}**\n\n{feature['description']}\n\n*Commands:*\n{cmds}"
            await callback_query.message.edit_text(text, reply_markup=build_feature_detail_menu(feat_name))
        else:
            await callback_query.answer("Feature not found.", show_alert=True)
    else:
        await callback_query.answer()


@app.on_message(filters.text & (filters.private | filters.group) & ~filters.command(["start", "menu"]))
async def main_message_handler(client, message: Message):
    # Update stats
    await update_user_stats(user_id=message.from_user.id)
    
    # React to message keywords
    await modules.reaction_handler.auto_react(client, message)
    
    # AI auto reply with mood, translation, etc
    await auto_reply(message)
    
    # Handle voice to text messages
    if message.voice:
        await voice_to_text_handler(message)
        return
    
    # NSFW scan
    if await scan_nsfw(message):
        return
    
    # AI generate final reply if needed
    reply = await generate_ai_response(message)
    if reply:
        await message.reply_text(reply)


if __name__ == "__main__":
    print("🧠 Infinity AI Bot is running...")
    app.run()