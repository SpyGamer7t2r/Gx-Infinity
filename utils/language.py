# utils/language.py

from langdetect import detect
from deep_translator import GoogleTranslator


def detect_language(text: str) -> str:
    """
    Detects the language of the given text.
    Returns ISO 639-1 language code (e.g., 'en', 'hi', 'fr').
    """
    try:
        return detect(text)
    except Exception:
        return "en"  # fallback to English


def translate_text(text: str, target_language: str = "en") -> str:
    """
    Translates text to the target language using Google Translator.
    """
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated
    except Exception:
        return text  # fallback to original text
