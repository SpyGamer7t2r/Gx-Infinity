from googletrans import Translator

translator = Translator()

def detect_language(text: str) -> str:
    try:
        detected = translator.detect(text)
        return detected.lang
    except Exception as e:
        return "unknown"

def translate_to_english(text: str) -> str:
    try:
        translated = translator.translate(text, dest='en')
        return translated.text
    except Exception as e:
        return text

def translate_text(text: str, dest_lang: str = 'en') -> str:
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return text
