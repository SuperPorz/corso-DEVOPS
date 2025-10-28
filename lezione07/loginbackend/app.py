from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# classe basemodel ha tutte le funzionalità per aiutare fastapi con 
# le richieste post sapendo la struttura dati che verrà passata

class Login(BaseModel):
    username:str
    password:str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/login")
def api_login(user:Login):
    if user.username == 'admin' and user.password == 'admin':
        return {"success":True, "message":"Benvenuto!"}
    else:
        return {"success":False, "message":"Dati errati!"}

#mapperemo le porte con docker
uvicorn.run(app, host="0.0.0.0", port=8000)