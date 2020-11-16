import sqlite3

#namedb = str(input('Nombre de la BD: '))

conection = sqlite3.connect('Base')

cursor = conection.cursor()

#cursor.execute("CREATE TABLE USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR UNIQUE, EDAD INTEGER)")
def agregar():
    name = str(input('Your name: '))
    edad = int(input('Your old: '))

    personanew = [
        (name, edad)
        ]
    cursor.executemany("INSERT INTO USER VALUES (NULL,?,?)", personanew)

def mostra():
    cursor.execute("SELECT * FROM USER")
    VAR = cursor.fetchall()
    for users in VAR:
        print('Id user: ', users[0], ' '*10, 'Name user: ', users[1], ' '*10, 'Old year: ', users[2])


print(' '*20, '1.agregar', '2.Mos')
opcion = str(input('Eliga opcion: '))

if opcion == '1':
    agregar()
elif opcion == '2':
    mostra()
else:
    print('Hola no hay opcion buena')







conection.commit()
conection.close()
print('Finish')