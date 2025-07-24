from langdetect import detect
from deep_translator import GoogleTranslator

# Detects the language of a given text
def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "unknown"

# Translate text to target language using GoogleTranslator
def translate_text(text: str, target_language: str = "en") -> str:
    try:
        translated = GoogleTranslator(source="auto", target=target_language).translate(text)
        return translated
    except:
        return "[Translation Failed]"
