from pyrogram import Client, filters
from pyrogram.types import Message
import random

REACTIONS = [
    "😲", "😂", "🔥", "😍", "😭", "🤯", "😡", "👍", "👎", "💀",
    "💯", "🤔", "🤡", "🥶", "😎", "👀", "🫡", "😴", "😈", "🎉"
]

@Client.on_message(filters.command(["react", "reaction"]))
async def send_reaction(_, message: Message):
    if not message.reply_to_message:
        await message.reply("Reply to a message to react!")
        return

    reaction = random.choice(REACTIONS)
    await message.reply_to_message.reply(reaction)