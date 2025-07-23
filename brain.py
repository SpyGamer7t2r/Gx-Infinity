import os
import random
import requests
from config import OPENAI_API_KEY, OPENROUTER_API_KEY, DEEPAI_API_KEY

from deep_translator import GoogleTranslator
from langdetect import detect

# User-based storage (can move to Redis/DB later)
USER_BRAINS = {}
USER_MOODS = {}

# Mood Starters
romantic_lines = ["Jaanu ❤️", "Baby 😘", "Meri Jindagi 💕", "Suno na 😍"]
angry_lines = ["Kya bakwaas hai 😡", "Shaant ho ja 😠", "Faltu mat bol!"]
funny_lines = ["Tu toh chomu nikla 😂", "Bhai kya logic hai 😂", "Mazaak chal raha hai kya?"]

# === NSFW Detector ===
def is_nsfw(text: str) -> bool:
    text = text.lower()
    nsfw_keywords = ["sex", "nude", "horny", "boobs", "penis", "vagina", "xxx", "porn", "bhabhi", "nangi"]
    return any(word in text for word in nsfw_keywords)

# === Translator ===
def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "en"

def translate_text(text: str, target_lang="en") -> str:
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        return f"[❌ Translation failed: {e}]"

# === Mood handler ===
def apply_mood(text, mood):
    if mood == "romantic":
        return f"{random.choice(romantic_lines)} {text}"
    elif mood == "angry":
        return f"{random.choice(angry_lines)} {text}"
    elif mood == "funny":
        return f"{random.choice(funny_lines)} {text}"
    return text

# === Main Response Handler ===
async def generate_ai_response(message):
    user_id = message.from_user.id
    user_text = message.text

    if is_nsfw(user_text):
        return "❌ NSFW content detected. Can't process that."

    lang = detect_language(user_text)
    translated_input = translate_text(user_text, "en") if lang != "en" else user_text

    brain = USER_BRAINS.get(user_id, "openai")
    mood = USER_MOODS.get(user_id, "default")

    if brain == "openai":
        raw_reply = openai_response(translated_input)
    elif brain == "openrouter":
        raw_reply = openrouter_response(translated_input)
    elif brain == "deepai":
        raw_reply = deepai_response(translated_input)
    else:
        return "❌ Unknown brain mode."

    final = apply_mood(raw_reply, mood)
    return translate_text(final, lang) if lang != "en" else final

# === AI Brain Functions ===
def openai_response(text):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": text}]
    }
    try:
        res = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=json_data)
        return res.json().get("choices", [{}])[0].get("message", {}).get("content", "OpenAI Error.")
    except Exception as e:
        return f"[OpenAI Failed: {e}]"

def openrouter_response(text):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "openrouter/auto",  # You can use `nous/hermes-2`, `meta-llama`, `mistralai`, `claude-3-opus`, etc.
        "messages": [{"role": "user", "content": text}]
    }
    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)
        return res.json().get("choices", [{}])[0].get("message", {}).get("content", "OpenRouter Error.")
    except Exception as e:
        return f"[OpenRouter Failed: {e}]"

def deepai_response(text):
    try:
        res = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={"text": text},
            headers={"api-key": DEEPAI_API_KEY}
        )
        return res.json().get("output", "DeepAI Error.")
    except Exception as e:
        return f"[DeepAI Failed: {e}]"
