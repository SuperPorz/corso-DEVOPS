from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def funzion1():
    return "Ciao FastAPI"

@app.get("/studenti")
def studenti():
    return ["Lorenzo","Michele","Eric","Francesca"]

@app.get("/html")
def html():
    return "<h1>ciao</h1>"

@app.get("/echo")
def echo(parola1, parola2=""):
    return f"{parola1[::-1]} - {parola2[::-1]}"
# ip:port/echo?parola1=abaco&parola2=cotoletta

"""
Il protocollo DICOM è un insieme di regole per esportare dati clinici.
Nel formato dati "name" e "surname" è necessario convertirli in "surname^name".
Il congome dovrebbe essere sempre presente e se il nome non è presente non inserire il carattere ^
"""
@app.get("/dicom")
def dicom(surname, name=""):
    if name == "":
        return surname
    return f"{surname}^{name}"

@app.get("/somma")
def somma(a:int,b:int):
    return a + b
# /somma?a=5&b=7

"""
Creare una rotta che accetti 3 parametri chiamati a, b, c
e calcoli la soluzione di una equazione di secondo grado del tipo
a*x^2 + b*x + c = 0
"""
@app.get("/eq")
def eq(a:float, b:float, c:float):
    if a == 0:
        if b == 0 and c != 0:
            return None
        if b == 0 and c == 0:
            return "indefinito"
        return -c/b
        
    delta = b*b - 4*a*c
    if delta < 0:
        return None
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    return x1, x2

"""
Data una richiesta con un parametro, la RAL
Calcolare lo stipendio netto
Per i redditi fino a 28.000 euro: 23%
Per i redditi tra 28.000 e 50.000 euro: 35%
Per i redditi oltre 50.000 euro: 43%
Solo le eccedenze allo scaglione precedente sono tassate di più
"""

@app.get("/prodotto/{nome_parametro}/{azione}")
def RAL(nome_parametro, azione=""):
    return nome_parametro, azione
# /prodotto/ax0064

from fastapi import Request
@app.get("/request")
def request_page(request: Request):
    print( type( request.query_params ) )
    for key in request.query_params.keys():
        print(key)
    for val in request.query_params.values():
        print(val)
    for k,v in request.query_params.items():
        print(k,v)
    return "ciao"

#http://192.168.200.171:8765/request?a[]=1&a[]=2

import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8765)