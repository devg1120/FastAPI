from typing import Optional

import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/item/")
def read_items():
    df = pd.DataFrame(
        [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]],
        index=["a", "b", "c", "d"],
        columns=["c1", "c2", "c3"],
    )
    return df.to_dict()


@app.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

