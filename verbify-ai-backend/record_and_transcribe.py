import sounddevice as sd
import soundfile as sf
import whisper
import random
import difflib
import requests
import os
from io import BytesIO
from app.core.config import ELEVENLABS_API_KEY

# 🎤 Recording config
SAMPLE_RATE = 16000
DURATION = 5

# 🎯 Word pool
WORDS = ["Hello", "World", "Monkey", "Python", "AI"]

# 🔊 ElevenLabs TTS
def speak_with_elevenlabs(text, voice="Rachel"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.7, "similarity_boost": 0.8}
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        audio_bytes = BytesIO(response.content)
        data, samplerate = sf.read(audio_bytes, dtype='float32')
        sd.play(data, samplerate)
        sd.wait()
    else:
        print("⚠️ ElevenLabs Error:", response.text)


# 🎤 Record audio
def record_audio(filename="output.wav"):
    print("\n🎤 Please say the word now (recording 5s)...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    sf.write(filename, audio, SAMPLE_RATE)
    print(f"✅ Audio saved to {filename}")


# 🎧 Transcribe with Whisper
def transcribe_audio(filename="output.wav"):
    model = whisper.load_model("base")
    print("🔎 Transcribing audio...")
    result = model.transcribe(filename, language="en")
    return result["text"].strip()


# 📝 Practice loop
def main():
    word = random.choice(WORDS)
    print(f"\n📝 Your practice word is: {word}")
    speak_with_elevenlabs(f"Your practice word is {word}")

    record_audio()
    transcription = transcribe_audio()
    print("✅ Transcription:", transcription)

    # 🔍 Similarity check
    similarity = difflib.SequenceMatcher(None, word.lower(), transcription.lower()).ratio()

    if similarity > 0.7:  # allow slack
        feedback = f"✅ Great job! You said {transcription}, which is close enough to {word}."
    else:
        feedback = f"❌ Not quite. You said {transcription}. Try again: {word}."

    print("\n📊 Pronunciation Feedback:")
    print(feedback)
    speak_with_elevenlabs(feedback)


if __name__ == "__main__":
    main()
