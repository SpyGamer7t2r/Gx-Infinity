import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message

STATS_FILE = "user_stats.json"


def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=4)


def update_user_stats(user_id: int, username: str, chat_type: str):
    stats = load_stats()
    uid = str(user_id)

    if uid not in stats:
        stats[uid] = {
            "username": username or "Unknown",
            "dms": 0,
            "groups": 0,
            "total": 0,
        }

    # Update username if changed
    if username and stats[uid]["username"] != username:
        stats[uid]["username"] = username

    # Increment stats
    if chat_type == "private":
        stats[uid]["dms"] += 1
    elif chat_type in ["group", "supergroup"]:
        stats[uid]["groups"] += 1

    stats[uid]["total"] += 1
    save_stats(stats)


@Client.on_message(filters.command("mystats"))
async def show_stats(client, message: Message):
    user_id = str(message.from_user.id)
    stats = load_stats()

    if user_id not in stats:
        await message.reply_text("📉 Koi stats nahi mile abhi tak.")
        return

    s = stats[user_id]
    await message.reply_text(
        f"📊 **Aapke Stats**\n\n"
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

    # Sort by total interactions
    sorted_stats = sorted(
        stats.items(), key=lambda x: x[1]["total"], reverse=True
    )

    msg = "🏆 **Top 10 Active Users**\n\n"
    for i, (uid, data) in enumerate(sorted_stats[:10], 1):
        msg += f"{i}. `{data['username']}` - {data['total']} msgs\n"

    await message.reply_text(msg)
