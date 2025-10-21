# ESERCIZIO: creare una pagina con registrazione.html e api/registrazione che permettano di inserire utenti in un dizionario

from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated
import uvicorn
app = FastAPI()

################  APP  ###################
utenti_registrati = {'mirco':'123'}

@app.post('/api/registrazione')
def api_registrazione(username:Annotated[str, Form()],
               password:Annotated[str, Form()]):
    
    if username in utenti_registrati:
        return RedirectResponse("/login.html?user_already_exist", 303)
    else:
        utenti_registrati[username] = password
        return RedirectResponse("/login.html?registrazione_avvenuta", 303)

@app.post("/api/login")
def api_login(username:Annotated[str, Form()],
               password:Annotated[str, Form()]):

    if username in utenti_registrati and utenti_registrati[username] == password: 
        response = RedirectResponse("/segreto.html?login_effetuato", 303)
        response.set_cookie('authentication', 'successful')
        return response
    else:
        return RedirectResponse("/registrazione.html?utente_sconosciuto", 303)


@app.get("/segreto")
def segreto(request: Request):
    autenticazione = request.cookies.get("authentication")
    if autenticazione == 'successful':
        return RedirectResponse("/segreto.html", 303)
    elif autenticazione == None:
        return RedirectResponse("/login.html?unauthorized", 303)
    else:
        return RedirectResponse("/login.html?authentication_failed", 303)

        
        
        
        

#con queste righe, non serve specificare il file.html nella url (localhost:8000/index.html = localhost:8000)
from fastapi.responses import FileResponse   
@app.get("/") 
def index():
    return FileResponse ('statics/index.html') #ridireziona su index.html


# il mount serve a ridirezionare l'utente quando vengono chieste pagine non specificate prima: una qualsiasi pagina non implementata, verrà gestita dal mount
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="statics"))

uvicorn.run(app, host="localhost", port=8000)