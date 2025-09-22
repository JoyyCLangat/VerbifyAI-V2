import pathlib
import soundfile as sf
from app.services import stt_service, nlp_service, tts_service

# Paths
BASE_DIR = pathlib.Path(__file__).resolve().parent
INPUT_AUDIO = BASE_DIR / "sample_input.wav"   # Put a small test recording here
OUTPUT_SPEECH = BASE_DIR / "output_speech.mp3"

def test_full_pipeline():
    print("🎙️ 1. Running Speech-to-Text with Whisper (offline)...")
    text = stt_service.transcribe_audio(str(INPUT_AUDIO))
    print("➡️ Transcribed text:", text)

    print("\n🧠 2. Running analysis with Gemini...")
    analysis = nlp_service.analyze_text_with_gemini(
        f"Analyze the correctness of this sentence: {text}"
    )
    print("➡️ Gemini analysis:", analysis)

    print("\n🔊 3. Converting analysis to speech with ElevenLabs...")
    speech = tts_service.text_to_speech(analysis, voice="Rachel")

    with open(OUTPUT_SPEECH, "wb") as f:
        f.write(speech)

    print(f"✅ Pipeline complete! MP3 saved at: {OUTPUT_SPEECH}")
