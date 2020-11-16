import sqlite3

#namedb = str(input('Nombre de la BD: '))

conection = sqlite3.connect('Base')

cursor = conection.cursor()

#cursor.execute("CREATE TABLE USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR UNIQUE, EDAD INTEGER)")
name = str(input('Your name: '))
edad = int(input('Your old: '))

personanew = [
    (name, edad)
    ]

cursor.executemany("INSERT INTO USER VALUES (NULL,?,?)", personanew)

cursor.execute("UPDATE USER SET EDAD='edad' WHERE ID = 1")






conection.commit()
conection.close()
print('Finish')