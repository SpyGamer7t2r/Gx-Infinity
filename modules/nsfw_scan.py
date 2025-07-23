import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Dummy key if you want to plug in deep detection API
NSFW_API = "https://api.deepai.org/api/nsfw-detector"
API_KEY = os.getenv("NSFW_API_KEY")  # You can set this in .env

@Client.on_message(filters.photo | filters.video)
async def scan_nsfw(client: Client, message: Message):
    if not message.chat.type in ["group", "supergroup"]:
        return

    if message.photo:
        file = await message.download()
    elif message.video:
        file = await message.download()
    else:
        return

    # Simulated local scan (you can replace with actual API detection)
    # e.g., DeepAI, NudeNet, etc.
    result = fake_nsfw_scan(file)

    if result["nsfw_score"] > 0.7:
        await message.delete()
        await message.reply("🚫 NSFW content detected and removed!")
    os.remove(file)


def fake_nsfw_scan(file_path):
    # Simulate score: you can plug real model here
    import random
    return {"nsfw_score": random.uniform(0.0, 1.0)}
