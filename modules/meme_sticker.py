# modules/meme_sticker.py

from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import random
from config import PREFIX

MEME_APIS = [
    "https://meme-api.com/gimme",
    "https://meme-api.com/gimme/dankmemes",
    "https://meme-api.com/gimme/wholesomememes",
]

STICKER_PACKS = [
    "FunnyStickers",
    "MemesGang",
    "ToxicStickers",
]

@Client.on_message(filters.command(["meme", "memes"], prefixes=PREFIX))
async def send_random_meme(client, message: Message):
    url = random.choice(MEME_APIS)
    try:
        res = requests.get(url).json()
        meme_url = res["url"]
        title = res.get("title", "Meme")
        subreddit = res.get("subreddit", "")
        await message.reply_photo(
            meme_url,
            caption=f"😂 **{title}**\n🔗 Subreddit: `{subreddit}`",
        )
    except Exception as e:
        await message.reply("⚠️ Failed to fetch meme.")

@Client.on_message(filters.command(["sticker", "funny"], prefixes=PREFIX))
async def send_random_sticker(client, message: Message):
    pack = random.choice(STICKER_PACKS)
    sticker_query = f"https://api.telegram.org/bot{client.token}/getStickerSet?name={pack}"
    try:
        res = requests.get(sticker_query).json()
        stickers = res["result"]["stickers"]
        sticker = random.choice(stickers)
        file_id = sticker["file_id"]
        await message.reply_sticker(file_id)
    except Exception as e:
        await message.reply("⚠️ Could not load sticker. Try again.")