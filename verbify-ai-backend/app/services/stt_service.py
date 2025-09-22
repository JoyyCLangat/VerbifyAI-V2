# app/services/stt_service.py
import whisper

model = whisper.load_model("base")  # or "small", "medium", "large"

def transcribe_audio(filepath: str):
    result = model.transcribe(filepath)
    return result["text"]
