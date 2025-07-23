import os
import tempfile
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.types import Message

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

@Client.on_message(filters.command("sticker") & filters.reply)
async def create_sticker(client, message: Message):
    reply = message.reply_to_message

    if reply.photo:
        photo_path = await reply.download()
        await message.reply_sticker(photo_path)
        os.remove(photo_path)
    elif reply.text:
        text = reply.text.strip()
        img = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH, 40)

        # Center the text
        w, h = draw.textsize(text, font=font)
        draw.text(((512-w)/2, (512-h)/2), text, font=font, fill="black")

        with tempfile.NamedTemporaryFile(suffix=".webp", delete=False) as tmp:
            img.save(tmp.name, format="WEBP")
            await message.reply_sticker(tmp.name)
            os.remove(tmp.name)
    else:
        await message.reply("⚠️ Reply to a photo or text to create a sticker.")
