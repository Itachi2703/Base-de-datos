from tqdm import tqdm
import sqlite3
 



conection = sqlite3.connect('dbnew') #Creamos y nos conectamos ala base de datos
cursor = conection.cursor() #Cramos un cursor

#cursor.execute("CREATE TABLE USER(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(20) , OLDYEAR INTEGER)") #Creacion de la tabla 
class dbcone:
    def barload():
        for i in tqdm(range(int(8e6)), ascii = True, desc = "Loading.."):
            pass

    def agregar():#Inicio de la funcion para agregar dator
        try:
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
                conection.commit()#Simulador de carga
            dbcone.barload()
            print("FINISH")
            conection.commit()
        except:
            print('Error de dato')
    #Search Person
    def search():
        iduser = str(input("ID of the User: "))
        dbcone.barload()
        cursor.execute("SELECT * FROM USER WHERE ID={0}".format(iduser))
        data = cursor.fetchone()
        print('|','Id user:', data[0], ' ', '\t', 'Name user: ',data[1], '\t','old year: ', data[2], '\t', '|')
        conection.commit()

    def mostrar():#Inicio funcion para mostrar
        dbcone.barload()
        cursor.execute("SELECT * FROM USER")
        variable_users = cursor.fetchall()
        for user in variable_users:
            print('-'*74)
            print('|','ID user: ', user[0], ' ','\t', 'Name user: ', user[1], ' ','\t', 'Old year user: ', user[2],'\t', '|')#Fin de la funcion
        print('-'*74)
    def cambiaruser():
        try:
            dbcone.mostrar()
            print("1.Cambiar nombre", '\t', '2.Cambiar edad')
            cambiarop = str(input('Eliga opcion: '))
            if cambiarop == '1':
                iddu = str(input('Id of the user to change: '))
                cursor.execute("SELECT * FROM USER WHERE ID={0}".format(iddu))
                data = cursor.fetchone()
                print('|','Id user:', data[0], ' ', '\t', 'Name user: ',data[1], '\t','old year: ', data[2], '\t', '|')
                print('1.SI','\n', '2.N0')
                siono = str(input("Este es el usuario que eligio: "))
                if siono == "1":
                    namecha = str(input('New name: '))
                    cursor.execute("UPDATE USER SET NAME='{0}' WHERE ID={1}".format(namecha, iddu))
                elif siono == '2':
                    print('Entonces ejecute nuevamente')
                else:
                    print(siono, 'Opcion Invalida')
            elif cambiarop == '2':
                iddu = str(input('Id of the user to change: '))
                cursor.execute("SELECT * FROM USER WHERE ID={0}".format(iddu))
                data = cursor.fetchone()
                print('|','Id user:', data[0], ' ', '\t', 'Name user: ',data[1], '\t','old year: ', data[2], '\t', '|')
                print('Este es usuario que eligio')
                print('1.SI','\n', '2.N0')
                siono = str(input("Este es el usuario que eligio: "))
                if siono == '1':
                    newage = str(input('Cual es el nueva edad: '))
                    cursor.execute("UPDATE USER SET OLDYEAR={0} WHERE ID={1}".format(newage, iddu))
                elif siono == '2':
                    print('Entonces ejecute nuevamente')
                else:
                    print(siono, 'Opcion Invalida')
            else:
                print(cambiarop, 'Opcion Invalida')
            dbcone.barload()
            print('FINISH')
            conection.commit()
        except:
            print('Error en rango')
conection.commit()
