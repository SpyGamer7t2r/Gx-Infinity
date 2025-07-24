from pyrogram import Client, filters
from pyrogram.types import Message
from PIL import Image
import io

@Client.on_message(filters.command("makesticker") & filters.reply)
async def make_sticker(client: Client, message: Message):
    if not message.reply_to_message.photo:
        await message.reply("❌ Reply to an image to convert it into a sticker.")
        return

    photo = await message.reply_to_message.download()
    img = Image.open(photo)

    img = img.convert("RGBA")
    img = img.resize((512, 512))

    sticker_io = io.BytesIO()
    sticker_io.name = "sticker.webp"
    img.save(sticker_io, format="WEBP")
    sticker_io.seek(0)

    await message.reply_sticker(sticker_io)