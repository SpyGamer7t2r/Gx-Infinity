import random
import aiohttp
from config import AI_MODE, OPENAI_API_KEY, OPENROUTER_API_KEY, DEEPAI_API_KEY, DEFAULT_MOOD, ALLOW_NSFW


# Predefined mood modifiers
MOOD_MODIFIERS = {
    "romantic": "Speak lovingly, like a caring lover 💖",
    "angry": "Reply in a bit irritated tone with sarcasm 😠",
    "funny": "Be humorous and entertaining 😂",
    "serious": "Answer strictly and seriously 🤨",
    "neutral": "Respond normally without any emotion.",
    "friendly": "Talk warmly and like a best friend 😊",
    "sad": "Sound a bit low, emotional 😢",
    "crazy": "Reply like a total wild funny psycho 🤪",
}

# NSFW keywords
NSFW_KEYWORDS = ["nude", "sex", "fuck", "xxx", "porn", "naked", "boobs", "dick", "vagina"]

def is_nsfw(text: str) -> bool:
    return any(word in text.lower() for word in NSFW_KEYWORDS)


async def generate_ai_response(user_id: int, user_message: str, mood: str = None) -> str:
    if not user_message.strip():
        return "Please send a message to respond to."

    # NSFW blocker
    if not ALLOW_NSFW and is_nsfw(user_message):
        return "🚫 NSFW content is not allowed."

    # Choose mood
    mood = mood or DEFAULT_MOOD or "neutral"
    mood_instruction = MOOD_MODIFIERS.get(mood.lower(), MOOD_MODIFIERS["neutral"])

    # Construct final prompt
    prompt = f"{mood_instruction}\nUser: {user_message.strip()}\nAI:"
    
    try:
        if AI_MODE == "openai":
            return await ask_openai(prompt)
        elif AI_MODE == "openrouter":
            return await ask_openrouter(prompt)
        elif AI_MODE == "deepai":
            return await ask_deepai(user_message)
        else:
            return "⚠️ Invalid AI mode set. Please check config."
    except Exception as e:
        return f"❌ AI Error: {str(e)}"


# --- OpenAI GPT-3.5/4 API ---
async def ask_openai(prompt: str) -> str:
    import openai
    openai.api_key = OPENAI_API_KEY

    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful and creative assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


# --- OpenRouter GPT (Claude, Mixtral, LLaMA, etc.) ---
async def ask_openrouter(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://t.me/InfinityAIBot",
        "X-Title": "Infinity AI",
    }
    json_data = {
        "model": "openrouter/openchat",
        "messages": [
            {"role": "system", "content": "You are an AI Assistant for Telegram."},
            {"role": "user", "content": prompt},
        ],
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data) as resp:
            data = await resp.json()
            return data["choices"][0]["message"]["content"].strip()


# --- DeepAI Text Generator (less powerful) ---
async def ask_deepai(prompt: str) -> str:
    url = "https://api.deepai.org/api/text-generator"
    headers = {"Api-Key": DEEPAI_API_KEY}
    data = {"text": prompt}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as resp:
            res = await resp.json()
            return res.get("output", "🤖 Couldn't think of anything...")