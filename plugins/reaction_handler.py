from pyrogram import Client, filters
from pyrogram.types import Message
import random

# Keywords and their corresponding emoji reactions
REACTIONS = {
    "hello": ["👋", "😊"],
    "hi": ["👋"],
    "thanks": ["🙏", "😊"],
    "love": ["❤️", "😍", "😘"],
    "bye": ["👋", "😢"],
    "good night": ["🌙", "😴"],
    "good morning": ["☀️", "🌅"],
    "lol": ["😂", "🤣"],
    "congrats": ["🎉", "👏"],
    "omg": ["😲", "😮"],
    "wow": ["😮", "🤩"],
}

@Client.on_message(filters.text & ~filters.edited)
async def auto_react(_, message: Message):
    text = message.text.lower()

    for keyword, emojis in REACTIONS.items():
        if keyword in text:
            emoji = random.choice(emojis)
            try:
                await message.react(emoji)
            except Exception:
                pass  # Some messages can't be reacted to (like service messages)
            break  # React only once per message