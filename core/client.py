# core/client.py

from pyrogram import Client
from pyrogram.enums import ParseMode
import config
from core.logger import LOGGER

class InfinityAI(Client):
    def __init__(self):
        LOGGER("client").info("Starting Infinity AI Bot...")
        super().__init__(
            name="InfinityAI",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            plugins=dict(root="modules"),
            workers=50,
        )
