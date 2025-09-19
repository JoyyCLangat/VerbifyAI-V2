# app/services/nlp_service.py
import requests
from app.core.config import settings

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def analyze_text(user_text: str, target_text: str) -> str:
    """
    Compares user's spoken text with the target phrase and provides feedback.
    """
    headers = {"Content-Type": "application/json"}
    params = {"key": settings.GEMINI_API_KEY}
    body = {
        "contents": [
            {"parts": [{"text": f"Compare: '{user_text}' vs '{target_text}'. "
                                "Give short feedback on correctness of words."}]}
        ]
    }

    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=body)
    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
