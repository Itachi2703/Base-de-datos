import sqlite3

conection = sqlite3.connect("DataBaserPRO")

cursor = conection.cursor()

#cursor.execute("CREATE TABLE USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(30) UNIQUE, OLD INTEGER)")
cursor.execute("DELETE FROM USER WHERE ID=4")

conection.commit()



conection.close()