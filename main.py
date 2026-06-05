from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
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


# POST request sample
class User(BaseModel):
    name: str
    age: int
    interests: List[str]

class UserResponse(BaseModel):
    message: str
    user: User
    recommendations: List[str]

@app.post("/users", response_model=UserResponse)
def create_user(user: User):
    first_interest = user.interests[0] if user.interests else "general"
    if first_interest.lower() == "music":
        recommendations = ["Spotify", "Music", "Amazon"]
    elif first_interest.lower() == "sports":
        recommendations = ["Gym", "Swimming", "Running"]
    else:
        recommendations = ["Gift card", "Surprise box", "Experience"]
    return {"message": "User profile created successfully",
            "user": user,
            "recommendations": recommendations
            }
    return user