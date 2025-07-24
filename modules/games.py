# modules/games.py

from pyrogram import filters, Client
from pyrogram.types import Message
import random

# Word list for basic games (can be replaced with advanced game engine later)
WORD_LIST = ["python", "telegram", "bot", "music", "chat", "game", "infinity", "code", "ai", "crypto"]

# Store game state per chat
game_state = {}

def handle_game_command(bot: Client):
    
    @bot.on_message(filters.command("startwordgame"))
    async def start_word_game(_, message: Message):
        chat_id = message.chat.id
        word = random.choice(WORD_LIST)
        scrambled = ''.join(random.sample(word, len(word)))
        game_state[chat_id] = word

        await message.reply_text(
            f"🧠 **Word Scramble Game Started!**\n\nUnscramble this word: **`{scrambled}`**\n\nReply with your guess!"
        )

    @bot.on_message(filters.text & ~filters.command(["startwordgame", "endwordgame"]))
    async def handle_guess(_, message: Message):
        chat_id = message.chat.id
        if chat_id not in game_state:
            return

        original = game_state[chat_id]
        if message.text.lower().strip() == original:
            del game_state[chat_id]
            await message.reply_text(f"🎉 Correct! The word was **{original}**.\nUse /startwordgame to play again.")
        else:
            await message.reply_text("❌ Incorrect! Try again.")

    @bot.on_message(filters.command("endwordgame"))
    async def end_game(_, message: Message):
        chat_id = message.chat.id
        if chat_id in game_state:
            word = game_state.pop(chat_id)
            await message.reply_text(f"🛑 Game ended. The correct word was **{word}**.")
        else:
            await message.reply_text("⚠️ No game is currently running in this chat.")