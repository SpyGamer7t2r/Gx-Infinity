import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

MEME_API = "https://meme-api.com/gimme"

@Client.on_message(filters.command("meme"))
async def fetch_meme(client, message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(MEME_API) as resp:
            if resp.status != 200:
                return await message.reply("😓 Meme API unavailable.")
            data = await resp.json()
    
    meme_url = data["url"]
    title = data["title"]
    postlink = data["postLink"]
    subreddit = data["subreddit"]

    await message.reply_photo(
        photo=meme_url,
        caption=f"🤣 <b>{title}</b>\n🔗 <a href='{postlink}'>r/{subreddit}</a>",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔁 Next Meme", callback_data="next_meme")]]
        )
    )

@Client.on_callback_query(filters.regex("next_meme"))
async def next_meme(client, callback_query):
    async with aiohttp.ClientSession() as session:
        async with session.get(MEME_API) as resp:
            data = await resp.json()
    
    meme_url = data["url"]
    title = data["title"]
    postlink = data["postLink"]
    subreddit = data["subreddit"]

    await callback_query.message.edit_media(
        media=meme_url,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔁 Next Meme", callback_data="next_meme")]]
        ),
        caption=f"🤣 <b>{title}</b>\n🔗 <a href='{postlink}'>r/{subreddit}</a>"
  )
