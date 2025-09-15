# Verbify AI

Verbify AI is an **AI-powered speech therapy platform** designed for children with autism and related conditions. It helps kids practice speech by generating words, converting them into natural speech, recording the child’s attempt, analyzing correctness with AI, and giving encouraging real-time feedback — both as text and speech.  

---

## 🌟 Vision
Speech therapy should be **accessible, engaging, and fun** for every child. Verbify AI combines **AI + gamification + therapist support** to create a platform that empowers kids, supports parents, and augments therapists.  

---

## 🚀 Features
- 🎤 **Speech-to-Text**: Transcribes a child’s spoken word using Whisper/Google STT.  
- 🤖 **Smart Analysis**: Gemini API checks pronunciation correctness and gives tailored feedback.  
- 🗣️ **Natural Feedback**: ElevenLabs converts feedback into kid-friendly speech.  
- 📊 **Progress Tracking**: Tracks accuracy and improvements over time.  
- 🧩 **Adaptive Learning Path**: Words scale in difficulty (simple → complex).  
- 🎮 **Gamification**: Rewards, stars, and animations to keep kids motivated.  
- 👩‍⚕️ **Therapist Mode** (future): Custom word lists and session reports for therapists.  

---

## 🏗️ Architecture
Child speaks → Audio recorded → STT (Whisper)
→ Analysis (Gemini) → Feedback generated
→ TTS (ElevenLabs) → Response to child

## ⚙️ Tech Stack
### Backend
- **FastAPI** (Python) – Core API  
- **OpenAI Whisper / Google Speech-to-Text** – Voice transcription  
- **Gemini API** – Word correctness + feedback  
- **ElevenLabs API** – Text-to-speech feedback  
- **Postgres/Supabase** (future) – User + session tracking  

### Frontend
- **React / React Native** – Kid-friendly gamified interface  
- **TailwindCSS** – Styling  
- **Web Audio APIs** – Recording/playback 
