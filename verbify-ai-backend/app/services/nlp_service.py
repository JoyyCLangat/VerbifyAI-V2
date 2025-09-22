# app/services/nlp_service.py
import google.generativeai as genai
from app.core.config import GEMINI_API_KEY

# Configure Gemini with API key
genai.configure(api_key=GEMINI_API_KEY)

def analyze_text_with_gemini(text: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(text)
    return response.text
