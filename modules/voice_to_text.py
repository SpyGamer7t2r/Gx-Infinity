from pyrogram import Client, filters
from pyrogram.types import Message
import os
import asyncio
import subprocess

@Client.on_message(filters.voice | filters.audio)
async def voice_to_text_handler(client, message: Message):
    download_path = f"downloads/{message.chat.id}_{message.message_id}.ogg"

    try:
        await message.download(file_name=download_path)
        await message.reply("🎙️ Converting voice to text...")

        # Use whisper or ffmpeg + whisper.cpp/OpenAI
        result = subprocess.run(
            ["whisper", download_path, "--model", "base", "--language", "hi", "--output_format", "txt"],
            capture_output=True,
            text=True
        )

        txt_path = download_path.replace(".ogg", ".txt")
        if os.path.exists(txt_path):
            with open(txt_path, "r") as f:
                text = f.read()
            await message.reply(f"📝 **Transcription:**\n\n{text}")
        else:
            await message.reply("❌ Failed to transcribe the audio.")
    except Exception as e:
        await message.reply(f"⚠️ Error: {str(e)}")
    finally:
        if os.path.exists(download_path):
            os.remove(download_path)
