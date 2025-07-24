# modules/notes_tasks.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import PREFIX

notes = {}

@Client.on_message(filters.command("note", prefixes=PREFIX))
async def save_note(_, message: Message):
    if len(message.command) < 2:
        await message.reply("✍️ Usage: /note <your note>")
        return
    text = message.text.split(None, 1)[1]
    notes[message.from_user.id] = text
    await message.reply("📝 Note saved!")

@Client.on_message(filters.command("getnote", prefixes=PREFIX))
async def get_note(_, message: Message):
    note = notes.get(message.from_user.id)
    if note:
        await message.reply(f"📒 Your note:\n\n{note}")
    else:
        await message.reply("❌ You haven't saved any note yet.")

@Client.on_message(filters.command("clearnote", prefixes=PREFIX))
async def clear_note(_, message: Message):
    if message.from_user.id in notes:
        del notes[message.from_user.id]
        await message.reply("🗑️ Note cleared!")
    else:
        await message.reply("❌ No note to clear.")