import random
import re
import httpx
from config import OPENROUTER_API, DEEPAI_API_KEY

BRAIN_TYPES = ["default", "romantic", "serious", "deep_ai", "openrouter"]
USER_BRAIN = {}
USER_MOOD = {}

# NSFW word filtering
NSFW_WORDS = ["nude", "sex", "boobs", "porn", "naked", "horny", "xxx", "bikini"]

def is_nsfw(text):
    return any(re.search(rf"\b{word}\b", text, re.IGNORECASE) for word in NSFW_WORDS)

def set_user_brain(user_id, brain_type):
    if brain_type in BRAIN_TYPES:
        USER_BRAIN[user_id] = brain_type
        return True
    return False

def set_user_mood(user_id, mood):
    USER_MOOD[user_id] = mood
    return True

async def generate_ai_response(user_id, prompt):
    brain = USER_BRAIN.get(user_id, "default")
    mood = USER_MOOD.get(user_id, "normal")

    # NSFW guard
    if is_nsfw(prompt):
        return "⚠️ Sorry, NSFW content is not allowed in this mode."

    if brain == "romantic":
        return f"❤️ {prompt}? Tum keh do toh saari duniya chhod doon baby... 😘"
    
    elif brain == "serious":
        return f"🔎 Analyzing: '{prompt}'\n🧠 Logical response: It seems valid and deeply insightful."
    
    elif brain == "deep_ai":
        return await get_deepai_response(prompt)

    elif brain == "openrouter":
        return await get_openrouter_response(prompt)

    else:  # Default brain
        replies = [
            f"You said: {prompt}",
            f"I got it: {prompt}",
            f"Understood: {prompt}",
            f"Hmm... interesting point.",
            f"Let me think about it: {prompt}"
        ]
        return random.choice(replies)

# ===== OpenRouter AI Response =====
async def get_openrouter_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API}",
        "Content-Type": "application/json",
    }
    json_data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are Infinity AI, a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            res = await client.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data)
            data = res.json()
            return data['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"🚫 OpenRouter Error: {str(e)}"

# ===== DeepAI Response =====
async def get_deepai_response(prompt):
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            res = await client.post(
                "https://api.deepai.org/api/text-generator",
                data={"text": prompt},
                headers={"api-key": DEEPAI_API_KEY},
            )
            data = res.json()
            return data.get("output", "🤖 DeepAI gave an empty response.")
    except Exception as e:
        return f"🚫 DeepAI Error: {str(e)}"