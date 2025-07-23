import os
import requests
import random
from config import AI_MODE, OPENAI_API_KEY, OPENROUTER_API_KEY, DEEPAI_API_KEY

# Mood-based reply starters
romantic_lines = ["Jaanu ❤️", "Baby 😘", "Meri Jindagi 💕", "Suno na 😍"]
angry_lines = ["Kya bakwaas hai 😡", "Shaant ho ja 😠", "Faltu mat bol!"]
funny_lines = ["Tu toh chomu nikla 😂", "Bhai kya logic hai 😂", "Mazaak chal raha hai kya?"]

def apply_mood(text, mood):
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

    if AI_MODE == "openai":
        return apply_mood(openai_response(user_text), mood)
    elif AI_MODE == "openrouter":
        return apply_mood(openrouter_response(user_text), mood)
    elif AI_MODE == "deepai":
        return apply_mood(deepai_response(user_text), mood)
    return "AI mode not configured."

def openai_response(text):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": text}]
    }
    res = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)
    return res.json().get("choices", [{}])[0].get("message", {}).get("content", "Error.")

def openrouter_response(text):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "openrouter/auto",
        "messages": [{"role": "user", "content": text}]
    }
    res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)
    return res.json().get("choices", [{}])[0].get("message", {}).get("content", "Error.")

def deepai_response(text):
    res = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={"text": text},
        headers={"api-key": DEEPAI_API_KEY}
    )
    return res.json().get("output", "DeepAI error.")
