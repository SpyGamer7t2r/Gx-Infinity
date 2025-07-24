from pyrogram import Client, filters
from pyrogram.types import Message
import json
import os

NOTES_FILE = "data/notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

@Client.on_message(filters.command("note"))
async def save_note(_, message: Message):
    if len(message.command) < 3:
        await message.reply("Use: `/note title content`")
        return
    title = message.command[1]
    content = " ".join(message.command[2:])
    notes = load_notes()
    notes[title] = content
    save_notes(notes)
    await message.reply(f"✅ Note saved under **{title}**")

@Client.on_message(filters.command("getnote"))
async def get_note(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Use: `/getnote title`")
        return
    title = message.command[1]
    notes = load_notes()
    content = notes.get(title)
    if content:
        await message.reply(f"📝 **{title}**:\n{content}")
    else:
        await message.reply("❌ Note not found.")

@Client.on_message(filters.command("delnote"))
async def delete_note(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Use: `/delnote title`")
        return
    title = message.command[1]
    notes = load_notes()
    if title in notes:
        del notes[title]
        save_notes(notes)
        await message.reply("🗑️ Note deleted.")
    else:
        await message.reply("❌ Note not found.")