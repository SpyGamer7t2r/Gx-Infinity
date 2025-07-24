# modules/meme_sticker.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX
import random

memes = [
    "https://i.imgflip.com/30b1gx.jpg",
    "https://i.imgflip.com/26am.jpg",
    "https://i.imgflip.com/1bij.jpg",
    "https://i.imgflip.com/2fm6x.jpg",
    "https://i.imgflip.com/3tx08g.jpg",
    "https://i.imgflip.com/5t4guq.jpg",
    "https://i.imgflip.com/5kdwuh.jpg"
]

stickers = [
    "CAACAgUAAxkBAAEFRA9mZ4bZmxdv-sb3p3uZpiBTqANcDQACuQMAAiRn2VcXBiOPPYbl3jQE",
    "CAACAgUAAxkBAAEFRA5mZ4bJYHhgwA2AGoR5TZRlmDNLuwACtwMAAiRn2VfY8uycAZf7JjQE",
    "CAACAgUAAxkBAAEFRBFmZ4bn96fY_6Y2f9f6dj4TwUo9AwACuAMAAiRn2VctIXSVP6wM9jQE",
    "CAACAgUAAxkBAAEFRBNmZ4cJux7IyzbEC9rEafSCGfGnbgACugMAAiRn2VdWaMX0ewziKjQE"
]

@Client.on_message(filters.command("meme", prefixes=PREFIX))
async def send_meme(client, message: Message):
    meme_url = random.choice(memes)
    await message.reply_photo(
        photo=meme_url,
        caption="😂 Here’s a meme to brighten your day!"
    )

@Client.on_message(filters.command("sticker", prefixes=PREFIX))
async def send_sticker(client, message):