from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return "FastApi working on docker"

uvicorn.run(app, host="0.0.0.0", port=8000)