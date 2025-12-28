from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import chat, lead, bot
from app.db.database import init_db
from fastapi.staticfiles import StaticFiles
from app.api.dashboard import router as dashboard_router
app = FastAPI(
    title="Website AI Chatbot",
    version="1.0.0"
)
@app.on_event("startup")
def start():
    init_db()

# CORS (allow widget from any website)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(lead.router, prefix="/api/lead", tags=["Leads"])
app.include_router(bot.router, prefix="/api/bot", tags=["Bots"])
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(dashboard_router)
@app.get("/")
def root():
    return {"status": "Website AI Chatbot Backend Running 🚀"}

@app.on_event("startup")
def startup():
    init_db()