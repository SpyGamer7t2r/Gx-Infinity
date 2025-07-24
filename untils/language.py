from langdetect import detect
from deep_translator import GoogleTranslator


def detect_language(text: str) -> str:
    """
    Detect the language of a given text.
    Returns ISO 639-1 language code (e.g., 'en', 'hi', 'fr').
    """
    try:
        return detect(text)
    except Exception:
        return "en"


def translate_text(text: str, target_lang: str = "en") -> str:
    """
    Translate given text to target language (default English).
    """
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception:
        return text