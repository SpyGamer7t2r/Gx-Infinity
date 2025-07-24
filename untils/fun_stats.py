# modules/fun_stats.py

import json
import os
from datetime import datetime

STATS_FILE = "data/user_stats.json"

def load_stats():
    if not os.path.exists(STATS_FILE):
        return {}
    with open(STATS_FILE, "r") as f:
        return json.load(f)

def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)

async def update_user_stats(user_id, chat_id, is_private=True, partner_id=None):
    stats = load_stats()
    user_id = str(user_id)

    if user_id not in stats:
        stats[user_id] = {
            "messages": 0,
            "private_chats": 0,
            "group_chats": [],
            "partners": [],
            "last_seen": None
        }

    stats[user_id]["messages"] += 1
    stats[user_id]["last_seen"] = datetime.utcnow().isoformat()

    if is_private:
        stats[user_id]["private_chats"] += 1
    else:
        group_id = str(chat_id)
        if group_id not in stats[user_id]["group_chats"]:
            stats[user_id]["group_chats"].append(group_id)

    if partner_id:
        partner_id = str(partner_id)
        if partner_id != user_id and partner_id not in stats[user_id]["partners"]:
            stats[user_id]["partners"].append(partner_id)

    save_stats(stats)