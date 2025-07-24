from pyrogram import Client, filters
from pyrogram.types import Message
from utils.password_gen import generate_password

@Client.on_message(filters.command("genpwd"))
async def generate_pwd_handler(_, message: Message):
    args = message.text.split()
    length = 12  # default password length

    if len(args) == 2 and args[1].isdigit():
        length = int(args[1])
        if length < 6 or length > 128:
            return await message.reply("❌ Length must be between 6 and 128 characters.")

    password = generate_password(length)
    await message.reply(f"🔐 Generated Password:\n`{password}`", quote=True)