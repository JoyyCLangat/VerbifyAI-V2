# app/services/tts_service.py
import requests
from app.core.config import ELEVENLABS_API_KEY

ELEVENLABS_URL = "https://api.elevenlabs.io/v1/text-to-speech"

def text_to_speech(text: str, voice: str = "Rachel") -> bytes:
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(f"{ELEVENLABS_URL}/{voice}", headers=headers, json=payload)
    response.raise_for_status()
    return response.content  # MP3 bytes
