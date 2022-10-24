# project/app/main.py
from fastapi import FastAPI, Depends

from app.config import get_settings, Settings


app = FastAPI()

@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "enviroment": settings.environment,
        "testing": settings.testing,
    }