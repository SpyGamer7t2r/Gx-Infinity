from pyrogram import Client, filters
from pyrogram.types import Message
import requests

AMAZON_API = "https://api.example.com/amazon"
FLIPKART_API = "https://api.example.com/flipkart"

def get_amazon_price(product_name):
    # Placeholder simulation
    return f"₹{str(len(product_name) * 100)} (Amazon)"

def get_flipkart_price(product_name):
    # Placeholder simulation
    return f"₹{str(len(product_name) * 110)} (Flipkart)"

@Client.on_message(filters.command(["compare", "compare_price"]))
async def compare_product_prices(_, message: Message):
    if len(message.command) < 2:
        await message.reply("Use: `/compare product name`")
        return

    product_name = " ".join(message.command[1:])
    amazon_price = get_amazon_price(product_name)
    flipkart_price = get_flipkart_price(product_name)

    result = (
        f"🔍 **Price Comparison for** `{product_name}`\n\n"
        f"🛒 Amazon: {amazon_price}\n"
        f"🏬 Flipkart: {flipkart_price}\n\n"
        f"💡 *Prices may vary or be approximate.*"
    )

    await message.reply(result)