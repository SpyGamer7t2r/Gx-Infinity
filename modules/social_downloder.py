from pyrogram import Client, filters
from pyrogram.types import Message
import yt_dlp

@Client.on_message(filters.command("download") & filters.private)
async def download_media(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("📥 Use: `/download <link>`")

    url = message.text.split(" ", 1)[1]

    opts = {
        "format": "best[ext=mp4]/best",
        "outtmpl": "downloads/%(title).50s.%(ext)s",
        "quiet": True,
    }

    await message.reply("⏳ Downloading... Please wait.")

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        await message.reply_video(
            video=file_path,
            caption=f"🎉 Downloaded: `{info.get('title', 'Unknown')}`",
        )
    except Exception as e:
        await message.reply(f"❌ Error:\n`{str(e)}`")
