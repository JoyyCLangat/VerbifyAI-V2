# app/utils/audio_utils.py
import uuid, os
from pathlib import Path
from pydub import AudioSegment


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def save_audio(file, ext="wav"):
    filename = f"{uuid.uuid4()}.{ext}"
    filepath = UPLOAD_DIR / filename
    with open(filepath, "wb") as f:
        f.write(file)
    return filepath


def convert_to_wav(filepath):
    audio = AudioSegment.from_file(filepath)
    wav_path = filepath.with_suffix(".wav")
    audio.export(wav_path, format="wav")
    return wav_path























