import mysql.connector as db
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/database")
def database():
    connection = db.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="database",
    database="lezione06"
    )
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    
    # fetchall   
    rows = cursor.fetchall()
    print(rows)
    return rows

uvicorn.run(app, host="0.0.0.0", port=8000)

    


# fetchone
""" while True:
    row = cursor.fetchone()
    if row == None:
        break
    
    print(row) """




