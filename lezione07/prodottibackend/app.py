from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import database as db

# classe basemodel ha tutte le funzionalità per aiutare fastapi con 
# le richieste post sapendo la struttura dati che verrà passata
class Prodotto(BaseModel):
    idProdotto: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/prodotti")
def get_prodotti():
    return db.get_all("select * from prodotti")

@app.put("/api/aggiungiProdotto")
def aggiungi_prodotto(prodotto: Prodotto):
    db.execute(f"""
               insert into carrello values ({prodotto.idProdotto}, 1) 
               on duplicate key update quantita = quantita + 1
               """)
    return (f"Prodotto inserito correttamente!")

#mapperemo le porte con docker
uvicorn.run(app, host="0.0.0.0", port=8000)