import json
import os
from collections import defaultdict, Counter

STATS_FILE = "data/fun_stats.json"

# Ensure file exists
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.isfile(STATS_FILE):
    with open(STATS_FILE, "w") as f:
        json.dump({}, f)


def load_stats():
    with open(STATS_FILE, "r") as f:
        return json.load(f)


def save_stats(data):
    with open(STATS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def update_user_stats(user_id: int, chat_id: int, is_private: bool = False, partner_id: int = None):
    stats = load_stats()

    user_id = str(user_id)
    chat_id = str(chat_id)

    if user_id not in stats:
        stats[user_id] = {
            "message_count": 0,
            "chats": [],
            "dm_partners": [],
        }

    stats[user_id]["message_count"] += 1

    if chat_id not in stats[user_id]["chats"]:
        stats[user_id]["chats"].append(chat_id)

    if is_private and partner_id:
        stats[user_id]["dm_partners"].append(str(partner_id))

    save_stats(stats)


def get_user_stats(user_id: int):
    stats = load_stats()
    user_id = str(user_id)

    if user_id not in stats:
        return None

    data = stats[user_id]
    total_msgs = data.get("message_count", 0)
    total_chats = len(data.get("chats", []))
    common_dms = Counter(data.get("dm_partners", []))
    top_3_dms = common_dms.most_common(3)

    return {
        "messages": total_msgs,
        "chats": total_chats,
        "top_dm_users": top_3_dms,
  }
