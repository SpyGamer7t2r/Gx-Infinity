from pyrogram import Client, filters
from pyrogram.types import Message
from utils.music import play_video

@Client.on_message(filters.command("vplay") & filters.private)
async def video_play_handler(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("❌ Please provide a video/song name or link.")
        return

    query = " ".join(message.command[1:])
    await message.reply_text("🎬 Searching and downloading video...")

    try:
        video_path = await play_video(query)
        await message.reply_video(
            video=video_path,
            caption=f"🎥 Now Playing: `{query}`"
        )
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")