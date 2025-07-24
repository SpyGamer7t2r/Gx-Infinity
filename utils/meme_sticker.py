import os
import random
import string
from PIL import Image, ImageDraw, ImageFont
from pyrogram.types import Message

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def random_filename(ext="png", length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + f".{ext}"

def generate_meme(image_path, top_text, bottom_text, output_dir="generated_memes"):
    os.makedirs(output_dir, exist_ok=True)

    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    width, height = img.size
    font_size = int(height / 10)
    font = ImageFont.truetype(FONT_PATH, font_size)

    # Outline text drawing
    def draw_text(text, y):
        text = text.upper()
        text_width, text_height = draw.textsize(text, font=font)
        x = (width - text_width) / 2
        outline_range = 2

        for ox in range(-outline_range, outline_range + 1):
            for oy in range(-outline_range, outline_range + 1):
                draw.text((x + ox, y + oy), text, font=font, fill="black")
        draw.text((x, y), text, font=font, fill="white")

    if top_text:
        draw_text(top_text, 10)
    if bottom_text:
        draw_text(bottom_text, height - font_size - 20)

    output_path = os.path.join(output_dir, random_filename())
    img.save(output_path)
    return output_path

def make_sticker_from_text(text, output_dir="generated_stickers"):
    from PIL import ImageFont

    os.makedirs(output_dir, exist_ok=True)
    font = ImageFont.truetype(FONT_PATH, 40)
    text_width = font.getlength(text) + 40
    img = Image.new("RGBA", (int(text_width), 80), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    draw.text((20, 20), text, font=font, fill=(0, 0, 0))

    path = os.path.join(output_dir, random_filename("webp"))
    img.save(path, "WEBP")
    return path

# Optional handler to extract media
async def download_image_from_message(message: Message, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    media = message.photo or message.document
    if not media:
        return None
    path = os.path.join(output_dir, random_filename("jpg"))
    await message.download(file_name=path)
    return path