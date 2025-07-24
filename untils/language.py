from deep_translator import GoogleTranslator
from langdetect import detect

def detect_language(text: str) -> str:
    """
    Detects the language of the input text using langdetect.
    Returns the language code (e.g., 'en', 'hi', 'fr').
    """
    try:
        return detect(text)
    except:
        return "en"  # Default to English if detection fails

def translate_text(text: str, target_lang: str = "en") -> str:
    """
    Translates the given text to the target language using GoogleTranslator.
    If translation fails, returns the original text.
    """
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except:
        return text