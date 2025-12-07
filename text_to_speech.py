from gtts import gTTS
import uuid
import os

def text_to_speech(text: str, lang: str) -> str:
    os.makedirs("static/voice", exist_ok=True)

    filename = f"static/voice/{uuid.uuid4().hex}.mp3"
    lang_code = "hi" if lang.lower() in ["hindi", "hinglish", "odia"] else "en"

    tts = gTTS(text=text, lang=lang_code)
    tts.save(filename)

    return filename
