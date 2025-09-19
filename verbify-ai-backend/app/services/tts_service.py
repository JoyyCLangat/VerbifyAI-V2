# app/services/tts_service.py
import requests
from app.core.config import settings

ELEVEN_API_URL = "https://api.elevenlabs.io/v1/text-to-speech"
VOICE_ID = "Rachel"  # can be dynamic later

def synthesize_speech(text: str, output_path: str = "output.wav") -> str:
    """
    Converts text into speech using ElevenLabs API.
    """
    url = f"{ELEVEN_API_URL}/{VOICE_ID}"
    headers = {
        "xi-api-key": settings.ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg"
    }
    body = {"text": text, "voice_settings": {"stability": 0.4, "similarity_boost": 0.8}}

    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    return output_path
