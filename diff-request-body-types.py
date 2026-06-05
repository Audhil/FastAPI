# request body types = json, text, form, file
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


@app.post("/json")
def receive_json(item: Item):
    return {"type": "JSON",
            "name": item.name,
            "in_stock": item.in_stock,
            "price": item.price}


@app.post("/text")
def receive_text(content: str = Body(..., media_type="text/plain")):  # ... means mandatory; None means optional
    return {"type": "Plain text",
            "content": content}
