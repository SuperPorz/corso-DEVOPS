from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated
import uvicorn

app = FastAPI()

#implementiamo una sorta di meccanismo di LOGIN

@app.get("/login") #usiamo GET solo per velocizzare
def check_login(username:Annotated[str, Form()],
               password:Annotated[str, Form()]):
    if username == 'mirco' and password == 'botti':
        return RedirectResponse("/segreto", 303)
    elif username == None or password == None:
        return JSONResponse(False, 422)        
    else:
        return JSONResponse(False, 401)
# http://localhost:8000/login?username=mirco&password=botti


@app.post("/api/login2") #usiamo GET solo per velocizzare
def api_login2(username:Annotated[str, Form()],
               password:Annotated[str, Form()]): # py -m pip install python-multipart    (serve installare questa libreria)
    if username == 'mirco' and password == 'botti':
        return RedirectResponse("/segreto", 303)
    elif username == None or password == None:
        return JSONResponse(False, 422)        
    else:
        return RedirectResponse("/login", 303) # serve usare 303 perche passa a get eliminando di fatto i dati sensibili
    # i nomi delle variabili username/password devono essere uguali agli attributi "name" degli input
    

@app.get('/segreto')
def segreto():
    return "Mastro Lorenzoni non ha installato python"

from fastapi.responses import FileResponse   
@app.get("/") #con queste riche, non serve specificare il file.html nella url (localhost:8000/index.html = localhost:8000)
def index():
    #return FileResponse ('lezione02/statics/index.html')  # ritorna un file, pagina statica
    return RedirectResponse ('/index.html') #ridireziona

@app.get('/attacchino') #simulazione furto dati
def attacchino(path:str):
    return FileResponse(path)


# il mount serve a ridirezionare l'utente quando vengono chieste pagine non specificate prima: una qualsiasi pagina non implementata, verrà gestita dal mount
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="statics"))

uvicorn.run(app, host="localhost", port=8000)


#esercizio. creare una pagina con registrazione.html e api/registrazione che permettano di inserire utenti in un dizionario