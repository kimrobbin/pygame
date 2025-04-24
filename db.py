import mysql.connector

dbconn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Pygame"
)

mycursor = dbconn.cursor()

if (dbconn):
    print("Connected to database")
else:
    print("Failed to connect to database")
