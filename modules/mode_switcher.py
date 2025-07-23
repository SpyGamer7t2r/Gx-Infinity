from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from utils.database import set_user_mode, get_user_mode

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

@Client.on_message(filters.command("setmode"))
async def set_mode(client: Client, message: Message):
    keyboard = [
        [InlineKeyboardButton(text=name, callback_data=f"mode_{key}")]
        for key, name in MODES.items()
    ]
    await message.reply_text(
        "🎛️ **Choose a mode for your Infinity AI**:",
        reply_markup=InlineKeyboardMarkup(keyboard),
        quote=True
    )

@Client.on_callback_query(filters.regex(r"^mode_"))
async def mode_selected(client: Client, callback_query: CallbackQuery):
    mode = callback_query.data.replace("mode_", "")
    user_id = callback_query.from_user.id

    if mode not in MODES:
        await callback_query.answer("❌ Invalid mode selected.", show_alert=True)
        return

    set_user_mode(user_id, mode)
    await callback_query.answer(f"✅ Mode set to {MODES[mode]}!", show_alert=True)
    await callback_query.message.edit_text(f"🧠 Your bot mode is now: **{MODES[mode]}**")

@Client.on_message(filters.command("mymode"))
async def get_mode(client: Client, message: Message):
    user_id = message.from_user.id
    mode = get_user_mode(user_id) or "default"
    await message.reply_text(f"👤 Your current mode: **{MODES.get(mode, '🤖 Default')}**")
