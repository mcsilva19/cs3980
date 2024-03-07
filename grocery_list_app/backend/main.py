from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  
    allow_headers=["*"],  
)

class Item(BaseModel):
    name: str
    quantity: int

db = []

@app.post("/items/")
async def create_item(item: Item):
    db.append(item)
    return item

@app.get("/items/")
async def get_items():
    return db

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = item
    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id >= len(db):
        raise HTTPException(status_code=404, detail="Item not found")
    db.pop(item_id)
    return {"message": "Item deleted successfully"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Grocery List API"}
