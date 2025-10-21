from fastapi import FastAPI, Request
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get('/ral/{val}')
def calcolo_ral(val:float):
    
    if val < 28000:
        tasse = val*0.23
        stipendio = (val-tasse)/13
        return round(stipendio, 2)
    if val >= 28000 and val < 50000:
        tasse1 = 28000*0.23
        tasse2 = (val-28000)*0.35
        stipendio = (val-tasse1-tasse2)/13
        return round(stipendio, 2)
    if val >= 50000:
        tasse1 = 28000*0.23
        tasse2 = (50000-28000)*0.35
        tasse3 = (val-50000)*0.43
        stipendio = (val-tasse1-tasse2-tasse3)/13
        return round(stipendio, 2)
    
    

uvicorn.run(app) # dati di default uvicorn:     host='127.0.0.1', port=8000



#ISTRUZIONE 1 - INSTALLAZIONE FASTAPI:   python.exe -m pip install --upgrade pip   
#ISTRUZIONE 2 - INSTALLAZIONE FASTAPI:   python -m pip install fastapi   
#ISTRUZIONE 3 - INSTALLAZIONE FASTAPI:   python -m pip install uvicorn