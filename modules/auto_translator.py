from pyrogram import Client, filters
from pyrogram.types import Message
from deep_translator import GoogleTranslator
from langdetect import detect

# 🔍 Language detection
def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "en"

# 🌐 Translation using GoogleTranslator
def translate_text(text: str, target_lang="en") -> str:
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        return f"[❌ Translation failed: {e}]"

# 🔄 Auto-translate foreign messages to English
@Client.on_message(filters.text & ~filters.edited & ~filters.command(["translate", "tl"]))
async def auto_translate_handler(_, message: Message):
    text = message.text
    detected_lang = detect_language(text)

    if detected_lang != "en":
        translated = translate_text(text, target_lang="en")
        reply_text = f"🌐 **Translated from `{detected_lang}` to `en`:**\n`{translated}`"
        await message.reply(reply_text, quote=True)
