import re

# Basic list of explicit words. You can expand it as needed.
NSFW_KEYWORDS = [
    "nude", "sex", "boobs", "porn", "naked", "babe", "pussy", "cock", "dick",
    "suck", "hentai", "fuck", "slut", "milf", "xxx", "blowjob", "anal", "threesome",
]

def is_nsfw(text: str) -> bool:
    text = text.lower()
    for word in NSFW_KEYWORDS:
        if re.search(rf"\b{re.escape(word)}\b", text):
            return True
    return False

def censor_nsfw(text: str) -> str:
    censored_text = text
    for word in NSFW_KEYWORDS:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        censored_text = pattern.sub("****", censored_text)
    return censored_text
