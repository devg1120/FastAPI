from fastapi import FastAPI

#app = FastAPI()

app = FastAPI(
    title="IIJ Bootcamp HandsOn",
    description="IIJ Bootcamp Web Application by FastAPI.",
    version="1.0",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
def read_query_item(skip: int = 0, limit: int = 10):
    """クエリパラメータ"""
    return fake_items_db[skip : skip + limit]


from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
def create_item(item: Item):
    """リクエストボディ"""
    return item

from fastapi import FastAPI, HTTPException

items = {"hoge": "This is Hoge"}


@app.get("/error/{item_id}")
def read_item_with_error_handling(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}



