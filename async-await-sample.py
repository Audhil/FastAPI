import asyncio
from http.client import responses

import httpx
import time
from fastapi import FastAPI

app = FastAPI()

JOKE_URL = "http://www.official-joke-api.appspot.com/random_joke"


@app.get("/jokes")
def receive_jokes():
    start = time.time()
    jokes = []
    with httpx.Client() as client:
        for _ in range(10):
            response = client.get(JOKE_URL)
            data = response.json()
            jokes.append(f"{data['setup']} - {data['punchline']}")
    end = time.time() - start
    return {"mode": "sync", "elasped time": round(end, 3), "jokes": jokes}


"""
sample response:
{
  "mode": "sync",
  "elasped time": 4.789,
  "jokes": [
    "Why did the house go to the doctor? - It was having window panes.",
    "Did you hear about the hungry clock? - It went back four seconds.",
    "What do you get when you cross a React developer with a mathematician? - A function component.",
    "How does a train eat? - It goes chew, chew",
    "What do you call a cow with two legs? - Lean beef.",
    "Where do rabbits go after they get married? - On a bunny-moon.",
    "Why does Superman get invited to dinners? - Because he is a Supperhero.",
    "What's the worst part about being a cross-eyed teacher? - They can't control their pupils.",
    "What's a computer's favorite snack? - Microchips.",
    "What's the difference between a hippo and a zippo? - One is really heavy, the other is a little lighter."
  ]
}
"""


@app.get("/jokes-async")
async def receive_jokes_async():
    start = time.time()
    jokes = []
    async with httpx.AsyncClient() as client:
        tasks = [client.get(JOKE_URL) for _ in range(10)]
        response_list = await asyncio.gather(*tasks)
        for resp in response_list:
            data = resp.json()
            jokes.append(f"{data['setup']} - {data['punchline']}")
    end = time.time() - start
    return {"mode": "async", "elasped time": round(end, 3), "jokes": jokes}
"""
sample response:
{
  "mode": "async",
  "elasped time": 0.724,
  "jokes": [
    "How many hipsters does it take to change a lightbulb? - Oh, it's a really obscure number. You've probably never heard of it.",
    "What do you call a troublesome Canadian high schooler? - A poutine.",
    "Why did the belt go to prison? - He held up a pair of pants!",
    "Want to hear a joke about a piece of paper? - Never mind...it's tearable",
    "What do you call a group of disorganized cats? - A cat-tastrophe.",
    "How many lips does a flower have? - Tulips",
    "What's the best thing about Switzerland? - I don't know, but their flag is a big plus.",
    "How does a scientist freshen their breath? - With experi-mints!",
    "Is the pool safe for diving? - It deep ends.",
    "A SQL query walks into a bar, walks up to two tables and asks... - 'Can I join you?'"
  ]
}
"""
