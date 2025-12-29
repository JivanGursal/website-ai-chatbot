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
    bot = get_bot(req.bot_id)
    print("BOT FETCH:", req.bot_id, bot is not None)

    if not bot:
        return {"reply": "Bot configuration not found."}

    system_prompt = bot["system_prompt"]

    reply = ask_llm(system_prompt, req.message)
    return {"reply": reply}
