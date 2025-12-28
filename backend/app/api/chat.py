from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import ask_llm
from app.services.bot_service import get_bot

router = APIRouter()

class ChatRequest(BaseModel):
    bot_id: str
    message: str

@router.post("/")
def chat(req: ChatRequest):
    system_prompt = get_bot(req.bot_id)

    if not system_prompt:
        return {"reply": "Bot configuration not found."}

    reply = ask_llm(system_prompt, req.message)
    return {"reply": reply}
