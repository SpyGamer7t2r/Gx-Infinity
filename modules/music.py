from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import yt_dlp
import os

@Client.on_message(filters.command(["play", "baby", "gana", "vplay", "bhai"]) & filters.private)
async def play_music(client, message: Message):
    if len(message.command) < 2:
        await message.reply("🎵 Please enter song name. Example:\n`/play tum hi ho`")
        return
    
    query = " ".join(message.command[1:])
    msg = await message.reply(f"🔍 Searching: `{query}`...")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            file_path = ydl.prepare_filename(info)

        await msg.edit("📤 Uploading...")
        await message.reply_audio(audio=file_path, title=info.get("title"), performer=info.get("uploader"))
        os.remove(file_path)

    except Exception as e:
        await msg.edit(f"❌ Failed to play: {e}")
