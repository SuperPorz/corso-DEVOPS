from fastapi import FastAPI, Form
import uvicorn
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from fastapi.responses import RedirectResponse

app = FastAPI()

# struttura dati per salvare i post
db = ['Sinner ha vinto', 'Terremoto in Afghanistan']

# 1a rotta (non esistono percorso relativi, solo assoluti, quindi serve '/' iniziale nelle rotte)
@app.post('/api/createPost')
def createPost(post:Annotated[str, Form()]):
    db.append(post)
    return RedirectResponse('/statics/index.html', 303)

# dati asincroni
@app.get('/api/listPost')
def listPost():
    return db

app.mount('/statics', StaticFiles(directory='statics'))

uvicorn.run(app, host = '0.0.0.0', port = 8000)