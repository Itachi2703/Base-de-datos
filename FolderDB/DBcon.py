
import sqlite3
import random

IDNEW = random.randint(1000000, 1000000000000)



conection = sqlite3.connect('dbnew') #Creamos y nos conectamos ala base de datos
cursor = conection.cursor() #Cramos un cursor
cursor.execute("CREATE TABLE USER (ID INTEGER PRIMARY KEY UNIQUE, NAME VARCHAR(20), OLDYEAR INTEGER)")
print("DB CREATED")
class dbcone:
    def agregar():#Inicio de la funcion para agregar dator
        cantidad = int(input('Cuantos datos desea agregar: '))
        i = 0
        while i <= cantidad:
            i = i + 1
            name = str(input('Your name: '))
            old_year = int(input('Your old year: '))
            print('='*10, '\n', 'Nuevos Datos', '\n','='*10)
            variable = [
            (IDNEW,name,old_year)
                ]
            cursor.executemany("INSERT INTO USER VALUES (?,?,?)", variable)
            conection.commit()#Simulador de carga
            print("FINISH")
            conection.commit()
        print('Error de dato')
    #Search Person
    def search():
        try:
            iduser = str(input("ID of the User: "))
        
            cursor.execute("SELECT * FROM USER WHERE ID={0}".format(iduser))
            data = cursor.fetchone()
            print('|','Id user:', data[0], ' ', '\t', 'Name user: ',data[1], '\t','old year: ', data[2], '\t', '|')
            conection.commit()
        except:
            print('La opcion ', iduser, 'Es Invalida')
    def mostrar():#Inicio funcion para mostrar
        
        cursor.execute("SELECT * FROM USER")
        variable_users = cursor.fetchall()
        for user in variable_users:
            print('-'*74)
            print('|','ID user: ', user[0], '  ','\t', 'Name user: ', user[1], ' ','\t', 'Old year user: ', user[2]," ",'\t', " ",'|')#Fin de la funcion
        print('-'*74)
    def cambiaruser():
        try:
            dbcone.mostrar()
            print("1.Cambiar nombre", '\t', '2.Cambiar edad', '\t', '3.Borrar por ID', "\t", "4.Delet datas of the table")
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
            elif cambiarop == '3':
                iddu = str(input('Id user to delet: '))
                cursor.execute("SELECT * FROM USER WHERE ID={0}".format(iddu))
                data = cursor.fetchone()
                print('1.SI, 2.N0')
                print('|','Id user:', data[0], ' ', '\t', 'Name user: ',data[1], '\t','old year: ', data[2], '\t', '|')
                siono = str(input('Este es el usuario que eligio: '))
                if siono == '1':
                    print('1.SI, 2.N0')
                    seguro = str(input('Esta seguro que desea borrar: '))
                    if seguro == '1':
                        cursor.execute("DELETE FROM USER WHERE ID={0}".format(iddu))
                        print('Usuario borrado')
                    elif seguro == '2':
                        print('Ejecute de Nuevo')
                    else:
                        print('Opcion Invalida')
                elif siono == '2':
                    print('Ejecute de Nuevo')
                else:
                    print('Valor Invado')
            elif cambiarop == "4":
                cursor.execute("SELECT * FROM TABLASNEWS")
                data = cursor.fetchall()
                for tabless in data:
                    print("Name of the table: ", tabless[0])
                print("1.SI", "\t", "2.NO")
                obdt = str(input("Desea borrar los datos de la tabla: "))
                namofthetable = str(input("Name of the table: "))
                if obdt == "1":
                    cursor.execute("DROP TABLE '{0}'".format(namofthetable))
                    print("Datos borrados")#option 2 not created ok 
                elif obdt == "2":
                    print("OK")
            else:
                print(cambiarop, 'Opcion Invalida')
            
            print('FINISH')
            conection.commit()
        except:
            print('Error en rango')
conection.commit()
