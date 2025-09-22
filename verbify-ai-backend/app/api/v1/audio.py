# app/api/v1/audio.py
from fastapi import APIRouter, UploadFile, File
from app.utils.audio_utils import save_audio, convert_to_wav
from app.services.stt_service import transcribe_audio

router = APIRouter()

@router.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    filepath = save_audio(await file.read(), ext=file.filename.split(".")[-1])
    wav_path = convert_to_wav(filepath)
    text = transcribe_audio(str(wav_path))
    return {"transcript": text}
