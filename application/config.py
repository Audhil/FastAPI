from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    groq_api_key: str
    app_name: str = "Groq Chatbot API"
    model_name: str = "llama-3.3-70b-versatile"

    class Config:
        env_file = ".env"


settings = Settings()
