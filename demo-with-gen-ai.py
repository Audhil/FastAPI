# integration with LLM
import os
import requests

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("groq_api_key")
app = FastAPI()


class PromptRequest(BaseModel):
    prompt: str
    tone: str = "neutral"


@app.post("/genai")
def generate_text(request: PromptRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    tone_prefix = {
        "friendly": "Respond in a casual and warm tone.",
        "formal": "Respond in professional and concise tone.",
        "neutral": "Respond Neutrally",
    }.get(request.tone.lower(), "Respond Neutrally")
    final_prompt = f"{tone_prefix}\n User request: {request.prompt}"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    payload = {"model":
               # "llama3-8b-8192", - this model is decommisioned
                   "llama-3.3-70b-versatile",
               "messages": [
                   {"role": "system", "content": "You are helpful AI assistant!"},
                   {"role": "user", "content": final_prompt},
               ], "temperature": 0.7}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    data = response.json()
    print(data)
    generated_text = data["choices"][0]["message"]["content"]
    return {
        "tone_used": request.tone,
        "original prompt": request.prompt,
        "final prompt": final_prompt,
        "response": generated_text,
    }


"""
change model if faced this error:

{
  "detail": {
    "error": {
      "message": "The model `llama3-8b-8192` has been decommissioned and is no longer supported. Please refer to https://console.groq.com/docs/deprecations for a recommendation on which model to use instead.",
      "type": "invalid_request_error",
      "code": "model_decommissioned"
    }
  }
}
"""

"""
response is:
{
  "tone_used": "neutral",
  "original prompt": "jack and jill went up the hill to fetch a pail of water",
  "final prompt": "Respond Neutrally\n\n User request: jack and jill went up the hill to fetch a pail of water",
  "response": "That's a well-known nursery rhyme. The traditional rhyme goes like this: \"Jack and Jill went up the hill to fetch a pail of water. Jack fell down and broke his crown, and Jill came tumbling after.\""
}

{
  "tone_used": "professional",
  "original prompt": "Where there is a will, there is a way!",
  "final prompt": "Respond Neutrally\n User request: Where there is a will, there is a way!",
  "response": "That's a common phrase often used to convey determination and perseverance. It suggests that if someone is motivated enough, they can find a way to achieve their goals."
}
"""