from fastapi import APIRouter
from uuid import uuid4

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.post("/create-bot")
def create_bot(name: str, prompt: str):
    bot_id = str(uuid4())[:8]

    script = f"""
<script
  src="YOUR_DOMAIN/static/widget.js"
  data-bot-id="{bot_id}">
</script>
"""

    return {
        "bot_id": bot_id,
        "embed_code": script
    }
