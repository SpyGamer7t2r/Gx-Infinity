from pyrogram import Client, filters
from pyrogram.types import Message

NOTES_DB = {}

@Client.on_message(filters.command("note") & filters.private)
async def handle_note(client, message: Message):
    user_id = message.from_user.id
    text = message.text

    if not text or len(text.split()) < 2:
        await message.reply("Usage:\n/note add <text>\n/note list\n/note del <index>")
        return

    args = text.split(maxsplit=2)
    command = args[1].lower()

    if user_id not in NOTES_DB:
        NOTES_DB[user_id] = []

    if command == "add" and len(args) > 2:
        NOTES_DB[user_id].append(args[2])
        await message.reply(f"✅ Note added. You now have {len(NOTES_DB[user_id])} notes.")
    elif command == "list":
        notes = NOTES_DB.get(user_id, [])
        if not notes:
            await message.reply("You have no notes saved.")
            return
        msg = "🗒️ Your Notes:\n"
        for i, note in enumerate(notes, start=1):
            msg += f"{i}. {note}\n"
        await message.reply(msg)
    elif command == "del" and len(args) > 2:
        try:
            index = int(args[2]) - 1
            if 0 <= index < len(NOTES_DB[user_id]):
                deleted = NOTES_DB[user_id].pop(index)
                await message.reply(f"✅ Deleted note: {deleted}")
            else:
                await message.reply("❌ Invalid note index.")
        except ValueError:
            await message.reply("❌ Please provide a valid note number to delete.")
    else:
        await message.reply("Invalid note command. Usage:\n/note add <text>\n/note list\n/note del <index>")