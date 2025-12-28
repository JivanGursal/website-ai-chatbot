from pydantic import BaseModel

class BotCreate(BaseModel):
    id: str
    name: str
    system_prompt: str
    website_url: str
