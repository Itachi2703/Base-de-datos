import sqlite3

conection = sqlite3.connect('MiDB')
cursor = conection.cursor()

#cursor.execute("CREATE TABLE USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(20) UNIQUE, OLDYEAR INTEGER)")
def agregar():
    name = str(input('Your name: '))
    old_year = int(input('Your old year: '))
    variable = [
        (name,old_year)
        ]
    cursor.executemany("INSERT INTO USER VALUES (NULL,?,?)", variable)
def mostrar():
    cursor.execute("SELECT * FROM USER")
    variable_users = cursor.fetchall()
    for user in variable_users:
        print('ID user: ', user[0], 'Name user: ', user[1], 'Old year user: ', user[2])

print('1.Add to data base', '2. show data base')

option = str(input('Option: '))
try:
    if option == '1':
        agregar()
    elif option == '2':
        mostrar()
    else:
        print("     ", option, 'Invalida')
except:
    print('Opcion de valor invalida')

conection.commit()
conection.close()
print('Finish')