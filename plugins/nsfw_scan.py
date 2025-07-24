import aiohttp
import os

NSFW_SCAN_API = os.getenv("NSFW_SCAN_API", "https://api.neural.love/v1/nsfw")  # Example, replace with actual API if needed

async def is_nsfw_content(message):
    file = await message.download()
    async with aiohttp.ClientSession() as session:
        with open(file, "rb") as f:
            data = aiohttp.FormData()
            data.add_field("file", f, filename=os.path.basename(file), content_type="application/octet-stream")
            async with session.post(NSFW_SCAN_API, data=data) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result.get("nsfw", False)
                else:
                    raise Exception(f"API returned {resp.status}")