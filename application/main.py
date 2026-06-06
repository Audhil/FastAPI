from fastapi import FastAPI

from application.config import settings
from application.routers import chat

app = FastAPI(title=settings.app_name, version="1.0.0")
app.include_router(chat.router)
