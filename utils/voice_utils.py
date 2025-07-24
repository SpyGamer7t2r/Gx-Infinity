import os
import tempfile
import speech_recognition as sr
from pydub import AudioSegment

def convert_voice_to_text(audio_path: str) -> str:
    try:
        # Convert audio to wav (if needed)
        if not audio_path.endswith(".wav"):
            audio = AudioSegment.from_file(audio_path)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
                audio.export(temp_wav.name, format="wav")
                audio_path = temp_wav.name

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text

    except sr.UnknownValueError:
        return "Sorry, couldn't understand the audio."
    except sr.RequestError as e:
        return f"Speech recognition service error: {e}"
    except Exception as e:
        return f"Error processing audio: {e}"
    finally:
        if "temp_wav" in locals():
            os.remove(temp_wav.name)
