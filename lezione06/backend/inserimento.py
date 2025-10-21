import mysql.connector as db

connection = db.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="database",
    database="lezione06"
)

cursor = connection.cursor()
cursor.execute("INSERT INTO users VALUES ('stgmhl', 'michelangelo', 'stega'), ('rckbrb', 'ricky', 'barabba');")

""" insert into users values 
	("bttmrc", "mirco", "botti"),
    ("lrnmch", "lorenzo", "michelon"); """