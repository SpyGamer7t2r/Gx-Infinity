import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message

# Bing Image API (or DuckDuckGo fallback)
async def fetch_image_url(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data.get("Image") or None

@Client.on_message(filters.command(["img", "image", "photo"]) | filters.regex(r"(image|photo|pic|picture) de") & filters.private)
async def image_fetch(client, message: Message):
    query = message.text.split(maxsplit=1)[-1] if " " in message.text else "cute cat"
    msg = await message.reply("🔍 Fetching image...")
    image_url = await fetch_image_url(query)
    if image_url:
        await message.reply_photo(photo=image_url, caption=f"🖼️ Here's your image for: **{query}**")
        await msg.delete()
    else:
        await msg.edit("❌ Couldn't fetch image.")

@Client.on_message(filters.command(["meme", "memes"]) | filters.regex("meme de") & filters.private)
async def meme_fetch(client, message: Message):
    meme_api = "https://meme-api.com/gimme"
    msg = await message.reply("🎭 Fetching meme...")
    async with aiohttp.ClientSession() as session:
        async with session.get(meme_api) as resp:
            data = await resp.json()
            await message.reply_photo(data["url"], caption=f"{data['title']}\nFrom: r/{data['subreddit']}")
            await msg.delete()

@Client.on_message(filters.command(["video", "vid"]) | filters.regex(r"(video|clip) de") & filters.private)
async def video_fetch(client, message: Message):
    query = message.text.split(maxsplit=1)[-1] if " " in message.text else "funny dog"
    msg = await message.reply("🎬 Fetching video link...")
    yt = f"https://yt.lemnoslife.com/search?query={query}"
    async with aiohttp.ClientSession() as session:
        async with session.get(yt) as resp:
            data = await resp.json()
            try:
                video_id = data["items"][0]["id"]["videoId"]
                url = f"https://www.youtube.com/watch?v={video_id}"
                await msg.edit(f"🎥 Video for **{query}**:\n{url}")
            except:
                await msg.edit("❌ Video not found.")
