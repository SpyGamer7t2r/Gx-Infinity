import random

happy_reactions = ["😄", "😁", "🎉", "🤩", "🥳", "😊"]
sad_reactions = ["😢", "😞", "😔", "😭", "🥺"]
angry_reactions = ["😠", "😡", "🤬"]
love_reactions = ["😍", "😘", "❤️", "💖", "💕"]
funny_reactions = ["😂", "🤣", "😹", "😆"]

keyword_reactions = {
    "love": love_reactions,
    "happy": happy_reactions,
    "birthday": ["🎂", "🎉", "🥳"],
    "sad": sad_reactions,
    "angry": angry_reactions,
    "funny": funny_reactions,
    "lol": funny_reactions,
    "cry": sad_reactions,
    "congrats": ["🎊", "👏", "🙌", "🏆"],
    "thanks": ["🙏", "😊", "❤️"],
    "bye": ["👋", "😢", "❤️"],
}

def get_reaction(text: str) -> str:
    text_lower = text.lower()
    for keyword, reaction_list in keyword_reactions.items():
        if keyword in text_lower:
            return random.choice(reaction_list)
    return random.choice(["👍", "🙂", "✨", "👌"])
