from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI REST API Assignment")


class Item(BaseModel):
    name: str
    description: str
    price: float


# In-memory store for assignment practice.
items: dict[int, Item] = {
    1: Item(name="Notebook", description="200-page notebook", price=4.99),
    2: Item(name="Pen", description="Blue ink pen", price=1.49),
}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items")
def list_items() -> list[dict]:
    return [{"id": item_id, **item.model_dump()} for item_id, item in items.items()]


@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items[item_id].model_dump()}


@app.post("/items")
def create_item(item: Item) -> dict:
    new_id = max(items.keys(), default=0) + 1
    items[new_id] = item
    return {"id": new_id, **item.model_dump()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> dict:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"id": item_id, **item.model_dump()}


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
