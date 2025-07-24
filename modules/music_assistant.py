from pyrogram import Client, filters
from pyrogram.types import Message
import yt_dlp
import os

DOWNLOAD_FOLDER = "downloads"

@Client.on_message(filters.command(["play", "baby", "gana", "bhai"]) & filters.private)
async def play_music(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("🎵 Bata gaana ka naam ya YouTube link. Example:\n`/play tu hi ho`")

    query = " ".join(message.command[1:])
    msg = await message.reply(f"🔍 Dhund raha hoon: `{query}`...")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{DOWNLOAD_FOLDER}/%(id)s.%(ext)s',
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
            file_path = ydl.prepare_filename(info)

        await msg.edit("📤 Upload kar raha hoon...")
        await message.reply_audio(audio=file_path, title=info.get("title"), performer=info.get("uploader"))
        os.remove(file_path)
    except Exception as e:
        await msg.edit(f"❌ Khatam ho gaya: {e}")