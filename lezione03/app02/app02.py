from fastapi import FastAPI, Form, Request #form per i dati in post, request per chiedere oggetto (cookie)
import uvicorn #si occupa del run dell'app sull'host indicato
from fastapi.staticfiles import StaticFiles #per i file statici
from typing import Annotated #estrapola dati dagli oggetti e li converte in qualche modo (tipo in stringa)
import json #libreria che ci permette di operare con dati formattati in json o di formattarli come tali
from fastapi.responses import JSONResponse # scrive una risposta intesa come 'client-server', contenente dati strutturati JSON

app = FastAPI()


@app.post('/api/inserisci')
def api_inserisci(prodotto:Annotated[str, Form()], request:Request):
    
    #fase 1: richiesta del cookie e lettura
    carrello = request.cookies.get('carrello')
    
    #fase 2: se cookie vuoto => lista creata, altrimenti deserializzata cioè si ricostruisce la struttura dati
    if carrello == None:  
        carrello = [ ]
    else:                 
        carrello = json.loads(carrello)
        
    #fase 3: manipolazione dati (aggiunta al carrello)
    carrello.append(prodotto)
    
    #fase 4: risposta al client
    risposta = JSONResponse(carrello)           # risposta 'client-server', dati strutturati JSON
    carrello = json.dumps(carrello)             # .dumps SERIALIZZA un object in una stringa formattata JSON
    risposta.set_cookie('carrello', carrello)   # .set_cookie setta il cookie con la chiave indicata nel 1° param e con contenuto dentro carrello
    
    #fase 5: return della risposta
    return risposta
    
    
        
    
    


app.mount('/', StaticFiles(directory='statics'))

uvicorn.run(app, host='0.0.0.0', port=8000)