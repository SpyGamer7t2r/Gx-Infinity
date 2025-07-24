from pyrogram import Client, filters
from pyrogram.types import Message
import random

MEMES = [
    "https://i.imgflip.com/4t0m5.jpg",
    "https://i.imgflip.com/30b1gx.jpg",
    "https://i.imgflip.com/1otk96.jpg",
    "https://i.imgflip.com/26am.jpg",
    "https://i.imgflip.com/2fm6x.jpg",
    "https://i.imgflip.com/1ur9b0.jpg",
]

STICKERS = [
    "CAACAgUAAxkBAAEGPh5kZgIjeHqD7FbGOjG6p4mvOUEjlAACZQIAAsbd2VQdcHUSdQGdBi8E",
    "CAACAgUAAxkBAAEGPh9kZgJbTzUuF5_SyXNZlQGXe_Z1ugACYgIAAsbd2VSBrOCjAfIkAy8E",
    "CAACAgUAAxkBAAEGPiBkZgKdAnll8m6wh1CFpR7th53m_AACZgIAAsbd2VQrAZ2-pnAO2y8E",
]

@Client.on_message(filters.command(["meme", "funny"]) & filters.private)
async def send_meme(client, message: Message):
    await message.reply_photo(random.choice(MEMES), caption="🤣 Here’s a random meme!")

@Client.on_message(filters.command(["sticker", "funsticker"]) & filters.private)
async def send_sticker(client, message: Message):
    await message.reply_sticker(random.choice(STICKERS))