from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.mount('/', StaticFiles(directory='statics'))

uvicorn.run(app, host='0.0.0.0', port=8000)