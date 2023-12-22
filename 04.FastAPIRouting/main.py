# File: main.py
from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

# Dummy data as an in-memory database
items = [
    {"item_id": 1, "name": "Item 1"},
    {"item_id": 2, "name": "Item 2"},
    {"item_id": 3, "name": "Item 3"},
]

# Route to get all items
@app.get("/items/", response_model=list)
async def read_items():
    return items

# Route to get a specific item by ID
@app.get("/items/{item_id}", response_model=dict)
async def read_item(item_id: int = Path(..., title="The ID of the item to retrieve")):
    item = next((item for item in items if item["item_id"] == item_id), None)
    if item:
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Route to create a new item
@app.post("/items/", response_model=dict)
async def create_item(item: dict):
    new_item = {"item_id": len(items) + 1, **item}
    items.append(new_item)
    return new_item

# Route to update an existing item
@app.put("/items/{item_id}", response_model=dict)
async def update_item(item_id: int, updated_item: dict):
    index = next((index for index, item in enumerate(items) if item["item_id"] == item_id), None)
    if index is not None:
        items[index].update(updated_item)
        return items[index]
    raise HTTPException(status_code=404, detail="Item not found")

# Route to delete an item by ID
@app.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    global items
    updated_items = [item for item in items if item["item_id"] != item_id]
    deleted_item = next((item for item in items if item["item_id"] == item_id), None)
    items = updated_items
    if deleted_item:
        return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")
