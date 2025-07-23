from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

MODES = {
    "romantic": "💖 Romantic",
    "serious": "🧠 Serious",
    "funny": "😂 Funny",
    "jugaadu": "🧠 Jugaadu",
    "sigma": "😎 Sigma",
    "default": "🤖 Default",
    "girl": "👧 Female Mode",
    "boy": "👦 Male Mode",
    "openai": "🌐 OpenAI Brain",
    "deepai": "🧬 DeepAI Brain",
    "openrouter": "🛰️ OpenRouter Brain"
}

USER_MODES = {}

@Client.on_message(filters.command("setmode") & filters.private)
async def set_mode(client, message: Message):
    keyboard = [
        [InlineKeyboardButton(text=v, callback_data=f"mode_{k}")]
        for k, v in MODES.items()
    ]
    await message.reply("Select a mode:", reply_markup=InlineKeyboardMarkup(keyboard))

@Client.on_callback_query(filters.regex("mode_"))
async def mode_selected(client, callback_query):
    user_id = callback_query.from_user.id
    mode_key = callback_query.data.replace("mode_", "")
    USER_MODES[user_id] = mode_key
    await callback_query.answer(f"Mode set to {MODES[mode_key]}!", show_alert=True)
