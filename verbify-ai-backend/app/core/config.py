from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    WHISPER_API_KEY: str
    GEMINI_API_KEY: str
    ELEVENLABS_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
