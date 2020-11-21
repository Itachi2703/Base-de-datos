#Antes de hacer el import, tenemos que ejecutar el comando pip install sqlite3, en la consola
import sqlite3

conection = sqlite3.connect('MiDB') #Creamos y nos conectamos ala base de datos
cursor = conection.cursor() #Cramos un cursor

#cursor.execute("CREATE TABLE USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(20) UNIQUE, OLDYEAR INTEGER)")  Creacion de la tabla 
def agregar():#Inicio de la funcion para agregar dator
    try:#Manejo de error de valores
        cantidad = int(input('Cuantos datos desea agregar: '))
        i = 1
        while i <= cantidad:
            i = i + 1
            name = str(input('Your name: '))
            old_year = int(input('Your old year: '))
            print('='*10, '\n', 'Nuevos Datos', '\n','='*10)
            variable = [
                (name,old_year)
                ]
            cursor.executemany("INSERT INTO USER VALUES (NULL,?,?)", variable)
            conection.commit()
    except:
        print('Error De valores')#Fin de la funcion
        

def mostrar():#Inicio funcion para mostrar
    cursor.execute("SELECT * FROM USER")
    variable_users = cursor.fetchall()
    for user in variable_users:
        print('ID user: ', user[0], '||','Name user: ', user[1], '||','Old year user: ', user[2])#Fin de la funcion

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
