from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str = "en") -> str:
    try:
        translated = GoogleTranslator(target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {str(e)}"

def detect_and_translate(text: str, to_language: str = "en") -> str:
    try:
        detected_lang = GoogleTranslator().detect(text)
        if detected_lang == to_language:
            return text
        translated = GoogleTranslator(source=detected_lang, target=to_language).translate(text)
        return translated
    except Exception as e:
        return f"Auto-translation error: {str(e)}"
