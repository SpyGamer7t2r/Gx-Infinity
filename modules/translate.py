from deep_translator import GoogleTranslator
from langdetect import detect

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "en"

def translate_text(text: str, target_lang="en") -> str:
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"[❌ Translation failed: {e}]"
