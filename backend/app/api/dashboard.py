from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


class CreateBotRequest(BaseModel):
    name: str
    prompt: str


@router.post("/create-bot")
def create_bot(data: CreateBotRequest):
    bot_id = str(uuid4())[:8]

    script = f"""
<script
  src="https://website-ai-chatbot-production.up.railway.app/static/widget.js"
  data-bot-id="{bot_id}">
</script>
"""

    return {
        "bot_id": bot_id,
        "embed_code": script
    }
