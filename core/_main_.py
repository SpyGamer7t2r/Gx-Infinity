# core/__main__.py

import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from core.startup import on_startup
from core.logger import LOGGER

LOG = LOGGER("InfinityAI")

bot = Client(
    name="InfinityAI_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

if __name__ == "__main__":
    LOG.info("Booting up Infinity AI Bot...")
    asyncio.run(on_startup(bot))
    bot.run()
