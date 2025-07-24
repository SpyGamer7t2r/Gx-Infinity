import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message

NSFW_SCAN_API = "https://api.deepai.org/api/nsfw-detector"  # or any image NSFW API
DEEPAI_API_KEY = "your_deepai_api_key_here"  # You can use a free key from DeepAI

@Client.on_message(filters.command("nsfw_scan") & filters.reply)
async def scan_nsfw(_, message: Message):
    if not message.reply_to_message.photo:
        await message.reply("📸 Please reply to an image to scan it for NSFW content.")
        return

    photo = await message.reply_to_message.download()
    await message.reply("🔍 Scanning image for NSFW content...")

    try:
        async with aiohttp.ClientSession() as session:
            with open(photo, "rb") as f:
                form = aiohttp.FormData()
                form.add_field('image', f, filename="image.jpg")

                headers = {"api-key": DEEPAI_API_KEY}
                async with session.post(NSFW_SCAN_API, data=form, headers=headers) as resp:
                    result = await resp.json()

        nsfw_score = result.get("output", {}).get("nsfw_score", 0)
        nsfw_score_percent = round(nsfw_score * 100, 2)

        if nsfw_score > 0.5:
            await message.reply(f"🚫 NSFW Detected!\nNSFW Score: **{nsfw_score_percent}%**")
        else:
            await message.reply(f"✅ Safe Image\nNSFW Score: **{nsfw_score_percent}%**")

    except Exception as e:
        await message.reply(f"❌ Failed to scan image.\nError: `{str(e)}`")