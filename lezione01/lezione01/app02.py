from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    
prodotti = []

@app.post('/create')
def create(obj: Item):
    prodotti.append(obj)
    # prodotti += [ obj ]   altra sintassi equivalente
    return True

@app.post('/createMultiple/{quantity}')
def create_multiple(obj: Item, quantity:int):
    # global prodotti   -->in quesot modo diciamo che prodotti non è definita in locale ma è globale
    for idx in range(quantity):
        prodotti.append(obj)
    # prodotti += [obj] * quantity  altro metodo equivalente
    return True

@app.get('/read')
def read():
    return prodotti

'''
esercizio casa: paginazione dei risultati a blocchi di 100 risultati per pagina
'''


uvicorn.run(app) # dati di default uvicorn:     host='127.0.0.1', port=8000    localhost:8000/docs --> apre un'interfaccia POST/GET