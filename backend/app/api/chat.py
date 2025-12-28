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
    bot_id = req.bot_id                      # ✅ FIX 1
    system_prompt = get_bot(bot_id)          # ✅ FIX 2

    print("BOT FETCH:", bot_id, system_prompt is not None)

    if not system_prompt:
        return {"reply": "Bot configuration not found."}

    reply = ask_llm(system_prompt, req.message)  # ✅ FIX 3
    return {"reply": reply}
