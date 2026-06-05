from unicodedata import category

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World Audhil"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/recommendations")
def recommend_items(age: int, interest: str):
    """
    Example GET: /recommend?age=4&interest=music
    :param age:
    :param interest:
    :return:
    """
    if age < 18:
        category = "Teen"
    elif age < 40:
        category = "Adult"
    else:
        category = "Senior"
    if interest.lower() == "music":
        recommendations = ["Spotify", "Music", "Amazon"]
    elif interest.lower() == "sports":
        recommendations = ["Gym", "Swimming", "Running"]
    else:
        recommendations = ["Gift card", "Surprise box", "Experience"]
    return {"category": category,
            "interest": interest,
            "recommendations": recommendations}