from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
from typing import Annotated
import json

app = FastAPI()

@app.post('/api/inserisci')
def api_inserisci(prodotto:Annotated[str, Form()], request:Request):
    
    #fase lettura cookie
    carrello = request.cookies.get('carrello')
    
    if carrello == None:
        carrello = []
    else:
        # leggere una lista da una stringa
        carrello = json.loads(carrello) # legge un json e lo ritorna con la struttura dati richiesta (deserializza)

    # fase manipolazione dati
    carrello.append(prodotto)
    
    #fase risposta al client
    response = JSONResponse(carrello) #creiamo risposta in modo esplicito
    carrello = json.dumps(carrello) #converto l'oggetto in stringa con json.dump (serializza)
    response.set_cookie('carrello', carrello) # qui scriviamo nella risposta che client deve creare cookie con contenuto carrello
    
    return response



app.mount('/', StaticFiles(directory = 'statics'))

uvicorn.run(app, host='localhost', port=8000)