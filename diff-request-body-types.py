# request body types = json, text, form, file
from fastapi import FastAPI, Body, Form, UploadFile, File
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


# json
@app.post("/json")
def receive_json(item: Item):
    return {"type": "JSON",
            "name": item.name,
            "in_stock": item.in_stock,
            "price": item.price}


# text
@app.post("/text")
def receive_text(content: str = Body(..., media_type="text/plain")):  # ... means mandatory; None means optional
    return {"type": "Plain text",
            "content": content}


# form
@app.post("/form")
def receive_form(username: str = Form(...), password: str = Form(...)):
    return {"type": "form",
            "username": username,
            "password": password}


# file upload
@app.post("/upload")
def receive_upload_file(file: UploadFile = File(...)):
    return {"type": "file",
            "filename": file.filename,
            "content_type": file.content_type}
