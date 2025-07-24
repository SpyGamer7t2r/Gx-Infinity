import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get MongoDB URL from .env
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Connect to MongoDB
client = MongoClient(MONGO_URL)
db = client["infinity_ai_db"]

# Define collections
users_col = db["users"]
sessions_col = db["sessions"]
group_settings_col = db["group_settings"]
zip_logs_col = db["zip_logs"]
stats_col = db["fun_stats"]

# Example function to add/update a user
def save_user(user_id: int, username: str = None):
    users_col.update_one(
        {"user_id": user_id},
        {"$set": {"username": username}},
        upsert=True
    )

# Example function to get user data
def get_user(user_id: int):
    return users_col.find_one({"user_id": user_id})

# Example to store password zip history
def log_zip(user_id: int, filename: str, password: str):
    zip_logs_col.insert_one({
        "user_id": user_id,
        "filename": filename,
        "password": password
    })

# Example to fetch all zipped files for a user
def get_user_zip_logs(user_id: int):
    return list(zip_logs_col.find({"user_id": user_id}))