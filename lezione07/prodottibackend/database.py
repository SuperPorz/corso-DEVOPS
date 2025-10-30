import mysql.connector as db


def connect():
    connection = db.connect(
        host="db", #nome del servizio docker
        port=3306, #questa app e il backend python comunicano su questa porta del CONTAINER e non del pc localhost
        user="root",
        password="database",
        database="lezione07"
    )
    return connection
    
def get_all(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query) #passiamo la query che arriva dai parametri della funz.
    rows = cursor.fetchall()
    #print(rows)
    return rows

def execute(query):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit() 
    cursor.close()
    connection.close()
    return cursor.rowcount  # Restituisce righe modificate