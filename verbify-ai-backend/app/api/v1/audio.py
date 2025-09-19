# app/api/v1/audio.py
from fastapi import APIRouter, UploadFile
import tempfile
from app.services.stt_service import transcribe_audio

router = APIRouter()

@router.post("/transcribe")
async def transcribe_audio_route(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    text = transcribe_audio(tmp_path)
    return {"transcription": text}
