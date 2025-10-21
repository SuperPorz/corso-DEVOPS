from fastapi import FastAPI, Form, Request #form per i dati in post, request per chiedere oggetto (cookie)
import uvicorn #si occupa del run dell'app sull'host indicato
from fastapi.staticfiles import StaticFiles #per i file statici
from typing import Annotated #estrapola dati dagli oggetti e li converte in qualche modo (tipo in stringa)
import json #libreria che ci permette di operare con dati formattati in json o di formattarli come tali
from fastapi.responses import JSONResponse # scrive una risposta intesa come 'client-server', contenente dati strutturati JSON

app = FastAPI()


@app.post('/api/inserisci')
def api_inserisci(prodotto:Annotated[str, Form()], quantita:Annotated[int, Form()],request:Request):
    
    #fase 1: acquisizione del cookie
    carrello = request.cookies.get('carrello')
    
    #fase 2: lettura cookie: se vuoto => lista creata, altrimenti deserializzata (cioè ricostruisce struttura dati)
    if carrello == None:  
        carrello = { }
    else:                 
        carrello = json.loads(carrello)
        
    #fase 3: manipolazione dati (aggiunta al carrello)
    carrello[prodotto] = quantita
    
    #fase 4: risposta al client
    risposta = JSONResponse(carrello)           # risposta 'client-server', dati strutturati JSON
    carrello = json.dumps(carrello)             # .dumps SERIALIZZA un object in una stringa formattata JSON
    risposta.set_cookie('carrello', carrello)   # .set_cookie setta il cookie con la chiave indicata nel 1° param e con contenuto dentro carrello
    
    #fase 5: return della risposta
    return risposta
    
    
@app.post('/api/modifica') 
def api_modifica(prodotto:Annotated[str, Form()], quantita:Annotated[int, Form()],request:Request):
    
    #fase 1: acquisizione del cookie
    carrello = request.cookies.get('carrello')
    
    #fase 2: lettura cookie: se vuoto => lista creata, altrimenti deserializzata (cioè ricostruisce struttura dati)
    if carrello == None:  
        carrello = { }
    else:                 
        carrello = json.loads(carrello)

    # Fase 3: controllo se il prodotto esiste e modifica
    if prodotto in carrello:
        carrello[prodotto] = quantita
    else:
        print('Modifica fallita; prodotto non presente in lista.')
    
    #fase 4: risposta al client
    risposta = JSONResponse(carrello)           # risposta 'client-server', dati strutturati JSON
    carrello = json.dumps(carrello)             # .dumps SERIALIZZA un object in una stringa formattata JSON
    risposta.set_cookie('carrello', carrello)   # .set_cookie setta il cookie con la chiave indicata nel 1° param e con contenuto dentro carrello
    
    #fase 5: return della risposta
    return risposta  


@app.post('/api/elimina')
def api_elimina(prodotto:Annotated[str, Form()], request:Request):
    
    carrello = request.cookies.get('carrello')
    
    if carrello == None:
        carrello = {}
    else:
        carrello = json.loads(carrello)
        
    # Soluzione 1: Controllo se la chiave esiste prima di rimuoverla
    if prodotto in carrello:
        carrello.pop(prodotto)
    else:
        # Opzionale: puoi gestire l'errore qui se vuoi
        print('Prodotto mai inserito in lista.')
    
    risposta = JSONResponse(carrello)
    carrello = json.dumps(carrello)
    risposta.set_cookie('carrello', carrello)
    
    return risposta      
    
    
    


app.mount('/', StaticFiles(directory='statics'))

uvicorn.run(app, host='0.0.0.0', port=8000)