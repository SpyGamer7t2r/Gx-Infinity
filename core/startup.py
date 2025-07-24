# core/startup.py

from pyrogram import Client
from config import BOT_NAME, OWNER_USERNAME
from core.logger import LOGGER

LOG = LOGGER(__name__)

async def on_startup(client: Client):
    bot_info = await client.get_me()
    LOG.info(f"🤖 {bot_info.first_name} (@{bot_info.username}) Started Successfully.")
    LOG.info(f"👑 Owner: @{OWNER_USERNAME}")
    LOG.info("💡 All systems initialized. Infinity AI is now online and ready.")
