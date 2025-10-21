from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float

prodotti = []

@app.post("/create")
def create(obj:Item):
    prodotti.append(obj)
    return True

@app.post("/createMultiple/{quantity}")
def createMultiple(obj:Item, quantity:int):
    global prodotti
    """
    for i in range(quantity):
        prodotti.append(obj) # bisogna inserirlo
    # quantity volte
    """
    prodotti += [ obj ] * quantity
    [0] * 65536
    return True

@app.get("/read")
def read():
    return prodotti

uvicorn.run(app, host="0.0.0.0", port=8765)