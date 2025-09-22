# app/main.py
from fastapi import FastAPI
from app.api.v1 import audio, analysis, tts

app = FastAPI(title="VerbifyAI API")

# Register routes
app.include_router(audio.router, prefix="/api/v1/audio", tags=["Audio"])
app.include_router(analysis.router, prefix="/api/v1/analysis", tags=["Analysis"])
app.include_router(tts.router, prefix="/api/v1/tts", tags=["TTS"])

# Root route
@app.get("/")
async def root():
    return {"message": "VerbifyAI API is running 🚀"}
