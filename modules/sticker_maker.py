import os
import aiofiles
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("sticker") & filters.reply)
async def make_sticker(client, message: Message):
    replied = message.reply_to_message

    if replied.photo or replied.video:
        media = await replied.download()
        sticker_path = f"{media}.webp"

        os.system(f"ffmpeg -i '{media}' -vf scale=512:512 '{sticker_path}' -y")
        await client.send_sticker(message.chat.id, sticker_path)
        os.remove(media)
        os.remove(sticker_path)

    elif replied.text:
        text = replied.text
        sticker_file = f"{message.from_user.id}_text.webp"

        from PIL import Image, ImageDraw, ImageFont

        img = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((50, 250), text, font=font, fill="black")

        img.save(sticker_file)
        await client.send_sticker(message.chat.id, sticker_file)
        os.remove(sticker_file)
    
    else:
        await message.reply("⚠️ Please reply to a photo, video or text.")
