# modules/translator.py

from pyrogram import Client, filters
from pyrogram.types import Message
from googletrans import Translator
from config import PREFIX

translator = Translator()

@Client.on_message(filters.command(["tr", "translate"], prefixes=PREFIX))
async def translate_text(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.text:
        await message.reply("Reply to a message to translate it.")
        return

    text = message.reply_to_message.text
    try:
        translated = translator.translate(text, dest='en')  # default to English
        await message.reply(f"🌐 Translated:\n\n<b>{translated.text}</b>\n\n🔤 Language: {translated.src.upper()} ➜ {translated.dest.upper()}")
    except Exception as e:
        await message.reply(f"❌ Error during translation:\n{e}")