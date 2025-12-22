from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id == 1:
        return  {
            "item_id": item_id,
            "name": "Example Item"
        }

    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )