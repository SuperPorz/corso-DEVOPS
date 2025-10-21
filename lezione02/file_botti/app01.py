from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, RedirectResponse
import uvicorn
from typing import Annotated

app = FastAPI()

"""
Dati user e password verificare se l'utente è ammesso
"""
@app.get("/login") # il metodo giusto è post, per velocizzare facciamo get
def check_login(username:str=None, password:str=None):
    if username == "mirco" and password == "botti":
        # return True
        return RedirectResponse("/segreto", 303)
    elif username == None or password == None:
        return JSONResponse(False, 422)
    else:
        return JSONResponse(False, 401)
    # http://127.0.0.1:8000/login?username=mirco&password=botti


@app.post("/api/login")
def api_login2(username:Annotated[str,Form()],
               password:Annotated[str,Form()]):
    
    if username == "mirco" and password == "botti":
        # return True
        return RedirectResponse("/segreto", 303)
    elif username == None or password == None:
        return JSONResponse(False, 422)
    else:
        return RedirectResponse("/login.html?error=wrongdata", 303)
        # return JSONResponse(False, 401)
    # http://127.0.0.1:8000/login?username=mirco&password=botti



@app.get("/segreto")
def segreto():
    return "Michele no ha installato Python"

from fastapi.responses import FileResponse
@app.get("/")
def index():
    return FileResponse("lezione02/statics/index.html")
    return RedirectResponse("/index.html", 303)

@app.get("/attacchino")
def attacchino(path:str):
    return False
    #return FileResponse(path)


from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="lezione02/statics"))

uvicorn.run(app, host="0.0.0.0", port=8000)