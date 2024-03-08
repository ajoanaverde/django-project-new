import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

#preparer un cursor object

cursorObject = dataBase.cursor()

# créer la base de données
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")