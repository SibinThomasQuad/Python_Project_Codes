from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example data class
class Item(BaseModel):
    id: int
    name: str
    price: float

# Example in-memory storage
items = [
    Item(id=1, name="Item 1", price=10.0),
    Item(id=2, name="Item 2", price=20.0),
]

# GET /items - Get all items
@app.get("/items")
async def get_items():
    return items

# GET /items/{item_id} - Get item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

# POST /items - Create a new item
@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return {"message": "Item created successfully"}

# PUT /items/{item_id} - Update an item
@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    for item in items:
        if item.id == item_id:
            item.name = updated_item.name
            item.price = updated_item.price
            return {"message": "Item updated successfully"}
    return {"error": "Item not found"}

# DELETE /items/{item_id} - Delete an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return {"message": "Item deleted successfully"}
    return {"error": "Item not found"}

# Run the server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8)
