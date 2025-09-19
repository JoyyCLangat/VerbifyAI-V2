# app/services/stt_service.py
import requests
from app.core.config import settings

WHISPER_API_URL = "https://api.openai.com/v1/audio/transcriptions"

def transcribe_audio(file_path: str) -> str:
    """
    Uploads an audio file to Whisper API and returns transcribed text.
    """
    headers = {"Authorization": f"Bearer {settings.WHISPER_API_KEY}"}
    files = {"file": open(file_path, "rb")}
    data = {"model": "whisper-1"}

    response = requests.post(WHISPER_API_URL, headers=headers, files=files, data=data)
    response.raise_for_status()

    return response.json()["text"]
