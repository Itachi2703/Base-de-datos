
import sqlite3
 



conection = sqlite3.connect('dbnew') #Creamos y nos conectamos ala base de datos
cursor = conection.cursor() #Cramos un cursor

def tablaaa():
    try:
        i = 1
        varndt = int(input('Numbrs of tables: '))
        while i <= varndt:
            i = i + 1
            vartab = str(input("Name of the table: "))
            cursor.execute("INSERT INTO TABLASNEWS VALUES ('{0}')".format(vartab))
            conection.commit()
    except:
        print('Error de dato lineas 10-1')

class dbcone:
    def creartable():
        print('1.SI     2.NO')
        creart = str(input('Desea crear una nueva tabla: '))
        if creart == '1':
            ndlt = str(input('Nombre de la tabla: '))
            cursor.execute("CREATE TABLE {0}(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(20) , OLDYEAR INTEGER)".format(ndlt)) #Creacion de la tabla 
            print('Tabla creada')
        elif creart == '2':
            print("OK")
        else:
            print('Opcion Invalida')
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
            print("FINISH")
            conection.commit()
        except:
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
            print('|','ID user: ', user[0], ' ','\t', 'Name user: ', user[1], ' ','\t', 'Old year user: ', user[2],'\t', '|')#Fin de la funcion
        print('-'*74)
    def cambiaruser():
        try:
            dbcone.mostrar()
            print("1.Cambiar nombre", '\t', '2.Cambiar edad', '\t', '3.Borrar por ID')
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
            else:
                print(cambiarop, 'Opcion Invalida')
            
            print('FINISH')
            conection.commit()
        except:
            print('Error en rango')
conection.commit()
