import random
import httpx
import json
from config import (
    AI_MODE,
    OPENAI_API_KEY,
    OPENROUTER_API_KEY,
    DEEPAI_API_KEY,
    DEFAULT_MOOD,
    ALLOW_NSFW,
)

# --- Moods and Modifiers ---
MOOD_MAP = {
    "romantic": "❤️ Darling,",
    "angry": "😡 Listen here,",
    "funny": "😂 Haha! Okay,",
    "neutral": "",
    "serious": "🧠 Logically speaking,"
}

# --- Get mood prefix ---
def apply_mood(text, mood):
    mood = mood.lower() if mood else DEFAULT_MOOD
    prefix = MOOD_MAP.get(mood, "")
    return f"{prefix} {text}" if prefix else text

# --- NSFW Guard ---
def contains_nsfw(text: str):
    nsfw_keywords = ["sex", "porn", "nude", "xxx", "boobs", "dick", "fuck"]
    return any(word in text.lower() for word in nsfw_keywords)

# --- Main Brain Engine ---
async def ask_ai(user_id: int, message: str, mood: str = None, brain: str = None):
    # Optional NSFW blocker
    if not ALLOW_NSFW and contains_nsfw(message):
        return "🚫 NSFW content is not allowed."

    mood = mood or DEFAULT_MOOD
    brain = (brain or AI_MODE).lower()

    try:
        if brain == "openai":
            return await openai_brain(message, mood)
        elif brain == "openrouter":
            return await openrouter_brain(message, mood)
        elif brain == "deepai":
            return await deepai_brain(message, mood)
        else:
            return apply_mood("❌ Unknown AI engine selected.", mood)
    except Exception as e:
        return f"⚠️ AI engine error: {e}"

# --- OpenAI GPT-3.5 / GPT-4 ---
async def openai_brain(prompt, mood):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, json=data)
        r.raise_for_status()
        result = r.json()
        reply = result["choices"][0]["message"]["content"]
        return apply_mood(reply.strip(), mood)

# --- OpenRouter GPT / Claude / Mixtral ---
async def openrouter_brain(prompt, mood):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mixtral-8x7b",
        "messages": [
            {"role": "system", "content": "You are a smart assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    async with httpx.AsyncClient() as client:
        r = await client.post(url, headers=headers, json=data)
        r.raise_for_status()
        result = r.json()
        reply = result["choices"][0]["message"]["content"]
        return apply_mood(reply.strip(), mood)

# --- DeepAI (fallback) ---
async def deepai_brain(prompt, mood):
    url = "https://api.deepai.org/api/chat-response"
    headers = {"api-key": DEEPAI_API_KEY}
    data = {"message": prompt}

    async with httpx.AsyncClient() as client:
        r = await client.post(url, data=data, headers=headers)
        r.raise_for_status()
        result = r.json()
        reply = result.get("output", "🤖 No response from DeepAI.")
        return apply_mood(reply.strip(), mood)