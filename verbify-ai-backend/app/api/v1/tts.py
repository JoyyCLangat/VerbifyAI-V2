# app/api/v1/tts.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.tts_service import synthesize_speech

router = APIRouter()

class TTSRequest(BaseModel):
    text: str

@router.post("/speak")
async def synthesize_speech_route(req: TTSRequest):
    output_path = synthesize_speech(req.text)
    return {"audio_file": output_path}
