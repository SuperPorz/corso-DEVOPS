from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse
import uvicorn
from typing import Annotated

app = FastAPI()

users = {"mirco":"botti", "paola":"rossi"}

@app.post("/api/login")
def api_login(username:Annotated[str,Form()] = None,
              password:Annotated[str,Form()] = None):
    
    if username in users and users[username] == password:
        response = RedirectResponse("/index.html", 303)
        response.set_cookie("auth", "futura")
        return response
    elif username == None or password == None:
        return JSONResponse(False, 422)
    else:
        return RedirectResponse("/login.html?error=wrongdata", 303)


@app.post("/api/registrazione")
def api_registrazione(username:Annotated[str,Form()] = None,
                      password:Annotated[str,Form()] = None):
    if username in users:
        return RedirectResponse("/registrazione.html?error=userexists", 303)
    else:
        users[username] = password
        return RedirectResponse("/login.html?message=registrationok", 303)

@app.get("/segreto")
def segreto(request:Request):
    auth = request.cookies.get("auth")
    if auth == None:
        return RedirectResponse("/login.html?error=forbidden", 303)
    if auth != "futura":
        return RedirectResponse("/login.html?error=tokenerror", 303)
    return "Python è un bel linguaggio"


@app.get("/segreto2")
def segreto(request:Request):
    auth = request.cookies.get("auth")
    if auth == None:
        return RedirectResponse("/login.html?error=forbidden", 303)
    if auth != "futura":
        return RedirectResponse("/login.html?error=tokenerror", 303)
    return "Manca poco"


app.mount("/", StaticFiles(directory="lezione02/statics"))

uvicorn.run(app, host="0.0.0.0", port=8000)