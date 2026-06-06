from fastapi import FastAPI
from config import settings

app = FastAPI()


@app.get("/check-env-file")
def check_env_file():
    return {
        "groq_api_key": settings.groq_api_key,
    }
