# app/api/v1/analysis.py
from fastapi import APIRouter, UploadFile, File
from app.utils.audio_utils import save_audio, convert_to_wav
from app.services.stt_service import transcribe_audio
from app.services.nlp_service import analyze_text
from app.services.tts_service import synthesize_speech

router = APIRouter()

@router.post("/pipeline")
async def full_pipeline(file: UploadFile = File(...)):
    filepath = save_audio(await file.read(), ext=file.filename.split(".")[-1])
    wav_path = convert_to_wav(filepath)
    
    transcript = transcribe_audio(str(wav_path))
    analysis = analyze_text(transcript)
    tts_output = synthesize_speech(analysis)
    
    return {
        "transcript": transcript,
        "analysis": analysis,
        "tts_file": tts_output
    }
