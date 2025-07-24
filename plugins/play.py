from pyrogram import Client, filters
from pyrogram.types import Message
from utils.music import play_audio

@Client.on_message(filters.command("play") & filters.private)
async def play_music_handler(client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("❌ Please provide a song name or link.")
        return

    query = " ".join(message.command[1:])
    await message.reply_text("🎵 Searching and playing...")

    try:
        file_path = await play_audio(query)
        await message.reply_audio(
            audio=file_path,
            caption=f"🎶 Now Playing: `{query}`"
        )
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")