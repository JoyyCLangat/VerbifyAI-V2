# app/api/v1/audio.py
from fastapi import APIRouter
from app.services import stt_service

router = APIRouter()

# Replace this with your mic device name
MIC_DEVICE = "Headset Microphone (Samsung USB C Earphones)"

@router.get("/record")
def record_and_transcribe(duration: int = 5):
    """
    Record audio from the Samsung mic and transcribe it.
    """
    text = stt_service.record_and_transcribe(MIC_DEVICE, duration)
    return {"transcription": text}
