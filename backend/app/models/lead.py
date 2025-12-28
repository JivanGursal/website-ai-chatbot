from pydantic import BaseModel

class LeadCreate(BaseModel):
    bot_id: str
    name: str
    email: str
    message: str
