import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

STATS_FILE = "user_stats.json"


def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


async def update_user_stats(user_id: int, username: str, chat_type: str):
    stats = load_stats()
    uid = str(user_id)

    if uid not in stats:
        stats[uid] = {
            "username": username or "Unknown",
            "dms": 0,
            "groups": 0,
            "total": 0,
        }

    if username and stats[uid]["username"] != username:
        stats[uid]["username"] = username

    if chat_type == "private":
        stats[uid]["dms"] += 1
    elif chat_type in ["group", "supergroup"]:
        stats[uid]["groups"] += 1

    stats[uid]["total"] += 1
    save_stats(stats)


@Client.on_message(filters.command("mystats"))
async def show_stats(client, message: Message):
    target: User = None

    if message.reply_to_message:
        target = message.reply_to_message.from_user
    elif len(message.command) > 1:
        username = message.text.split(None, 1)[1].lstrip("@")
        try:
            target = await client.get_users(username)
        except Exception:
            await message.reply_text("❌ User nahi mila. Username sahi bhejo.")
            return
    else:
        target = message.from_user

    user_id = str(target.id)
    stats = load_stats()

    if user_id not in stats:
        await message.reply_text(f"📉 Koi stats nahi mile `{target.first_name}` ke liye.")
        return

    s = stats[user_id]
    await message.reply_text(
        f"📊 **{target.first_name} ke Stats**\n\n"
        f"👤 Username: `{s['username']}`\n"
        f"📬 DMs Used: `{s['dms']}`\n"
        f"👥 Groups Used: `{s['groups']}`\n"
        f"📈 Total Interactions: `{s['total']}`"
    )


@Client.on_message(filters.command("topstats"))
async def top_stats(client, message: Message):
    stats = load_stats()
    if not stats:
        await message.reply_text("Koi bhi data available nahi hai abhi.")
        return

    sorted_stats = sorted(stats.items(), key=lambda x: x[1]["total"], reverse=True)

    msg = "🏆 **Top 10 Active Users**\n\n"
    for i, (uid, data) in enumerate(sorted_stats[:10], 1):
        msg += f"{i}. `{data['username']}` - {data['total']} msgs\n"

    await message.reply_text(msg)