import os
import random
import requests
from config import AI_MODE, OPENAI_API_KEY, OPENROUTER_API_KEY, DEEPAI_API_KEY

# Mood-based reply starters
romantic_lines = ["Jaanu ❤️", "Baby 😘", "Meri Jindagi 💕", "Suno na 😍"]
angry_lines = ["Kya bakwaas hai 😡", "Shaant ho ja 😠", "Faltu mat bol!"]
funny_lines = ["Tu toh chomu nikla 😂", "Bhai kya logic hai 😂", "Mazaak chal raha hai kya?"]

def apply_mood(text, mood="neutral"):
    if mood == "romantic":
        return f"{random.choice(romantic_lines)} {text}"
    elif mood == "angry":
        return f"{random.choice(angry_lines)} {text}"
    elif mood == "funny":
        return f"{random.choice(funny_lines)} {text}"
    return text

async def generate_ai_response(message):
    user_text = message.text
    mood = os.getenv("DEFAULT_MOOD", "neutral")

    # If you add per-user mood in future:
    # mood = get_user_mood(message.from_user.id)

    if AI_MODE == "openai":
        response = await openai_response(user_text)
    elif AI_MODE == "openrouter":
        response = await openrouter_response(user_text)
    elif AI_MODE == "deepai":
        response = await deepai_response(user_text)
    else:
        return "AI mode not configured properly."

    return apply_mood(response, mood)

async def openai_response(text):
    try:
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        json_data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": text}]
        }
        res = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[OpenAI Error: {e}]"

async def openrouter_response(text):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        json_data = {
            "model": "openrouter/auto",
            "messages": [{"role": "user", "content": text}]
        }
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[OpenRouter Error: {e}]"

async def deepai_response(text):
    try:
        headers = {"api-key": DEEPAI_API_KEY}
        data = {"text": text}
        res = requests.post("https://api.deepai.org/api/text-generator", data=data, headers=headers)
        res.raise_for_status()
        return res.json().get("output", "No output.")
    except Exception as e:
        return f"[DeepAI Error: {e}]"
