from fastapi import APIRouter
from app.models.lead import LeadCreate
from app.db.database import cursor, conn

router = APIRouter()

@router.post("/")
def save_lead(lead: LeadCreate):
    cursor.execute(
        """
        INSERT INTO leads (bot_id, name, email, message)
        VALUES (?, ?, ?, ?)
        """,
        (lead.bot_id, lead.name, lead.email, lead.message)
    )
    conn.commit()
    return {"status": "Lead saved"}
