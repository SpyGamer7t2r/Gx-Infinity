from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str = "en") -> str:
    try:
        translated = GoogleTranslator(target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {e}"

def detect_and_translate(text: str, to_language: str = "en") -> str:
    try:
        translator = GoogleTranslator()
        detected_lang = translator.detect(text)
        if detected_lang == to_language:
            return text  # No need to translate
        return translator.translate(text, target=to_language)
    except Exception as e:
        return f"Error: {e}"
