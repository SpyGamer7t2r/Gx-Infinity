from pyrogram import Client, filters
from pyrogram.types import Message
import random

# Emojis for different reactions
REACTIONS = ["😂", "🔥", "😍", "💀", "👍", "😎", "💯", "😭", "😡", "🤯", "🤖", "🙈", "👀"]

@Client.on_message(filters.command("react") & filters.reply)
async def react_to_message(client, message: Message):
    reaction = random.choice(REACTIONS)
    try:
        await client.send_reaction(chat_id=message.chat.id, message_id=message.reply_to_message.id, emoji=reaction)
        await message.reply(f"Reacted with {reaction}")
    except Exception as e:
        await message.reply("Could not react to the message.")