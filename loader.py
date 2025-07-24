# loader.py

from pyrogram import Client
import config
from pyrogram.enums import ParseMode

app = Client(
    "InfinityAI_Bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    parse_mode=ParseMode.HTML
)