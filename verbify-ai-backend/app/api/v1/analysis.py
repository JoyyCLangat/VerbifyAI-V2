# app/api/v1/analysis.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.nlp_service import analyze_text

router = APIRouter()

class AnalysisRequest(BaseModel):
    user_text: str
    target_text: str

@router.post("/compare")
async def analyze_text_route(req: AnalysisRequest):
    feedback = analyze_text(req.user_text, req.target_text)
    return {"feedback": feedback}
