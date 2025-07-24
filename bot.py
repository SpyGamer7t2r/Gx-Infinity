import os from pyrogram import Client, filters from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID from brain import generate_ai_response from modules import zipper, unzipper, password_gen, downloader, notes_tasks, translate, music_assistant from modules.auto_reply_modes import auto_reply from modules.restrictor import restrict_user from modules.reaction_handler import emoji_react from modules.nsfw_guard import scan_nsfw from modules.product_compare import compare_product_prices from modules.voice_to_text import voice_to_text_handler from modules.admin_tools import handle_admin_commands from modules.games import handle_game_command from modules.dm_file_sender import send_file_to_dm from modules.reminders import set_reminder from modules.fun_stats import update_stats from modules.document_writer import generate_report from modules.meme_sticker import send_funny_reply

app = Client("InfinityAIBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

Start command

@app.on_message(filters.command("start") & filters.private) async def start_handler(client, message: Message): await message.reply_text( "🧠 Welcome to Infinity AI Bot!\nHow can I help you today?", reply_markup=InlineKeyboardMarkup([ [InlineKeyboardButton("🤖 AI Help", callback_data="ai_help")], [InlineKeyboardButton("🎵 Music", callback_data="music")], [InlineKeyboardButton("🧹 Games", callback_data="games")], ]) )

AI response

@app.on_message(filters.text & filters.private & ~filters.command("start")) async def ai_reply(client, message: Message): await update_stats(message) await emoji_react(message) await auto_reply(message)

if message.voice:
    await voice_to_text_handler(message)
    return

if await scan_nsfw(message):
    return

reply = await generate_ai_response(message)
if reply:
    await message.reply_text(reply)

Main zip/unzip commands

@app.on_message(filters.command("zip")) async def zip_command(client, message): await zipper.zip_handler(message)

@app.on_message(filters.command("unzip")) async def unzip_command(client, message): await unzipper.unzip_handler(message)

@app.on_message(filters.command("genpwd")) async def pwd_generate(client, message): await password_gen.handle_password_command(message)

@app.on_message(filters.command(["remind", "alarm"])) async def reminder(client, message): await set_reminder(message)

@app.on_message(filters.command("download")) async def download_cmd(client, message): await downloader.handle_download(message)

@app.on_message(filters.command("note")) async def notes_cmd(client, message): await notes_tasks.handle_note(message)

@app.on_message(filters.command("translate")) async def translate_cmd(client, message): await translate.translate_text(message)

@app.on_message(filters.command("music")) async def music_cmd(client, message): await music_assistant.play_music(message)

@app.on_message(filters.command("compare")) async def compare_cmd(client, message): await compare_product_prices(message)

@app.on_message(filters.command("gban") & filters.user(OWNER_ID)) async def admin_cmd(client, message): await handle_admin_commands(message)

@app.on_message(filters.command("sendto")) async def dm_send(client, message): await send_file_to_dm(message)

@app.on_message(filters.command("report")) async def report_gen(client, message): await generate_report(message)

@app.on_message(filters.command("fun") | filters.regex(".joke.|.shayari.")) async def fun_content(client, message): await send_funny_reply(message)

@app.on_message(filters.command("game")) async def game_cmd(client, message): await handle_game_command(message)

print("🧠 Infinity AI Bot is running...") app.run()

