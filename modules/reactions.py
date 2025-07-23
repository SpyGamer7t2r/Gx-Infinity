import random

REACTION_SETS = {
    "happy": ["😊", "😄", "😎", "😁", "✨", "🥰"],
    "sad": ["😢", "😞", "🥺", "😭"],
    "angry": ["😡", "😠", "😤", "💢"],
    "romantic": ["😍", "😘", "💖", "💕", "❤️"],
    "savage": ["😈", "💀", "🔥", "🤭", "👀"],
    "default": ["🤖", "🙃", "👌", "🤔"]
}

def get_reaction(mood="default"):
    mood = mood.lower()
    return random.choice(REACTION_SETS.get(mood, REACTION_SETS["default"]))
