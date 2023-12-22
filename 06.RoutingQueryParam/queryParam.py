from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, query_param: str = None):
    """
    Example of using path and query parameters in FastAPI.
    
    Parameters:
    - item_id: Path parameter representing the item identifier (integer).
    - query_param: Query parameter representing an optional string.

    Usage:
    - /items/42
    - /items/42?query_param=example
    """
    return {"item_id": item_id, "query_param": query_param}
