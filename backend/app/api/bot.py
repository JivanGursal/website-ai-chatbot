from fastapi import APIRouter
from app.models.bot import BotCreate
from app.services.bot_service import create_bot

router = APIRouter()

@router.post("/create")
def create(bot: BotCreate):
    create_bot(
        bot.id,
        bot.name,
        bot.system_prompt,
        bot.website_url
    )
    return {"status": "Bot created & trained from website 🚀"}
