# core/decorators.py

from functools import wraps
from pyrogram.types import Message
from pyrogram.enums import ChatType

from config import OWNER_ID


def only_owner(func):
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        if message.from_user and message.from_user.id == OWNER_ID:
            return await func(client, message, *args, **kwargs)
        await message.reply_text("❌ You are not allowed to use this command.")
    return wrapper


def group_only(func):
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            return await func(client, message, *args, **kwargs)
        await message.reply_text("❌ This command can only be used in groups.")
    return wrapper


def private_only(func):
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        if message.chat.type == ChatType.PRIVATE:
            return await func(client, message, *args, **kwargs)
        await message.reply_text("❌ This command can only be used in private chat.")
    return wrapper
