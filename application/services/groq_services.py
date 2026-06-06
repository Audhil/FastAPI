from groq import AsyncGroq
from application.config import settings

client = AsyncGroq(api_key=settings.groq_api_key)


async def get_groq_reply(user_message: str) -> str:
    completion = await client.chat.completions.create(
        model=settings.model_name,
        messages=[{"role": "user", "content": user_message}]
    )
    return completion.choices[0].message.content
