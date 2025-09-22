# app/services/stt_service.py
import subprocess
import os
from faster_whisper import WhisperModel

# Path where audio will be temporarily saved
AUDIO_FILE = "temp_input.wav"

# Initialize Whisper model (can pick "base", "small", "medium", or "large")
model = WhisperModel("base", device="cpu")

def record_audio(device_name: str, duration: int = 5) -> str:
    """
    Records audio using ffmpeg from the given device name.
    """
    if os.path.exists(AUDIO_FILE):
        os.remove(AUDIO_FILE)

    cmd = [
        "ffmpeg",
        "-f", "dshow",
        "-t", str(duration),
        "-i", f"audio={device_name}",
        AUDIO_FILE,
        "-y"  # overwrite without asking
    ]

    subprocess.run(cmd, check=True)
    return AUDIO_FILE

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes audio file into text using Whisper.
    """
    segments, _ = model.transcribe(file_path)
    text = " ".join([seg.text for seg in segments])
    return text

def record_and_transcribe(device_name: str, duration: int = 5) -> str:
    """
    Record audio from mic and transcribe in one step.
    """
    audio_path = record_audio(device_name, duration)
    return transcribe_audio(audio_path)
