import random
from pyrogram import Client, filters
from pyrogram.types import Message

# Word database (simplified)
nouns = ["apple", "banana", "car", "dog", "elephant"]
verbs = ["run", "jump", "eat", "sleep", "write"]
adjectives = ["big", "fast", "smart", "blue", "angry"]

@Client.on_message(filters.command("wordgen"))
async def word_gen(client, message: Message):
    word_type = message.text.split(" ", 1)[-1].lower()
    if "noun" in word_type:
        word = random.choice(nouns)
    elif "verb" in word_type:
        word = random.choice(verbs)
    elif "adj" in word_type or "adjective" in word_type:
        word = random.choice(adjectives)
    else:
        word = random.choice(nouns + verbs + adjectives)
    await message.reply(f"🔤 Generated word: **{word}**")

@Client.on_message(filters.command("scramble"))
async def scramble_word(client, message: Message):
    word = random.choice(nouns + verbs + adjectives)
    scrambled = ''.join(random.sample(word, len(word)))
    await message.reply(f"🧩 Unscramble this: **{scrambled}**\nReply with the correct word!")

@Client.on_message(filters.command("hangman"))
async def hangman_game(client, message: Message):
    word = random.choice(nouns + verbs)
    hidden = "_" * len(word)
    await message.reply(f"🎯 Hangman: `{hidden}`\n(Guess the word in replies!)")
