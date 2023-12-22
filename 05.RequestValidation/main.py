from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    """
    Example of request validation using Pydantic model.
    The 'item' parameter is automatically validated based on the Item model.
    """
    item_dict = item.dict()
    if item.tax:
        total_price = item.price + item.tax
        item_dict.update({"total_price": total_price})
    return item_dict
