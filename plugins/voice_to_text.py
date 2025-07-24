from pyrogram import Client, filters
from pyrogram.types import Message
import os
import speech_recognition as sr
from pydub import AudioSegment

@Client.on_message(filters.voice & filters.private)
async def voice_to_text_handler(_, message: Message):
    voice = message.voice
    file_path = await message.download()
    ogg_path = file_path
    wav_path = file_path.replace(".ogg", ".wav")

    try:
        # Convert OGG to WAV using pydub
        AudioSegment.from_ogg(ogg_path).export(wav_path, format="wav")

        # Use speech recognition
        r = sr.Recognizer()
        with sr.AudioFile(wav_path) as source:
            audio = r.record(source)

        text = r.recognize_google(audio)
        await message.reply(f"🗣️ Voice to Text:\n\n{text}")

    except sr.UnknownValueError:
        await message.reply("⚠️ Could not understand the audio.")
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")

    finally:
        if os.path.exists(ogg_path):
            os.remove(ogg_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)