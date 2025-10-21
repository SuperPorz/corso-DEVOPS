from fastapi import FastAPI
# from fastapi.responses import 
app = FastAPI()


## METODO GET ####

@app.get('/') #decoratore
def funzione1(): #una pagina web si crea con una funzione
    return 'Ciao FastATPI'



@app.get('/root01')
def funzione1():
    x = 5
    return x

@app.get('/root02')
def funzione1():
    x = [1,2]
    return x

@app.get('/studenti')
def studenti():
    return ['Lorenzo', 'Michele', 'Sandra']

@app.get('/html')
def html():
    return '<h1>Ciao</h1>'

@app.get('/echo')
def echo(parola1, parola2=''):
    return f"{parola1[::-1]} - {parola2[::-1]}"

@app.get('/dicom')
def dicom(cognome, nome=None):
    if nome == '':
        return cognome
    elif cognome == None:
        return "cognome non isnerito! inserirlo."
    else:
        return f"{cognome}^{nome}"

@app.get('/somma')
def somma(a:int, b:int):
    return a + b

'''
creare una rotta che accetti 3 parametri a,b,c, e calcoli la soluzione di una equazione di secondo grado 
del tipo a*x^2 + b*x + c

x[1,2] = (-b +- sqrt(b^2 -4ac))/2a
'''

@app.get('/equazione')
def equazione(a:float, b:float, c:float):
    
    if a == 0:
        if b == 0 and c != 0:
            return None
        if b == 0 and c == 0:
            return "equazione indefinita"            
        x = c/b
        return x
    else:
        delta = b**2 -4*a*c
        if delta < 0:
            return None
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        return x1, x2
        #return f"x1= {x1} e x2= {x2}"

'''
Data una richiesta con un parametro, la RAL, calcolare lo stipendio netto mensile
formula
reddito < 28'000 = 23% tasse
28'000 < reddito < 50'000 = 35% tasse
reddito > 50'000 = 43%tasse
Solo le eccedenze allo scaglione precedente sono tassate di più
'''

@app.get('/ral/{val}')
def calcolo_ral(val:float):
    
    if val < 28000:
        tasse = val*0.23
        stipendio = (val-tasse)/13
        return stipendio
    if val >= 28000 and val < 50000:
        tasse1 = 28000*0.23
        tasse2 = (val-28000)*0.35
        stipendio = (val-tasse1-tasse2)/13
        return stipendio
    if val >= 50000:
        tasse1 = 28000*0.23
        tasse2 = (50000-28000)*0.35
        tasse3 = (val-50000)*0.43
        stipendio = (val-tasse1-tasse2-tasse3)/13
        return stipendio

@app.get("/prodotto/{parametro}/{azione}")
def acquisto(parametro, azione=""):
    return parametro, azione

from fastapi import Request
@app.get("/request")
def page_request (request: Request):
    print(type(request._query_params))
    print(request._query_params.keys)
    print(request._query_params.values)
    return "ciao"



        
        
    
    
    
    
    
    
import uvicorn 
uvicorn.run(app, host='127.0.0.1', port=8989)