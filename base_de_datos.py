#Antes de hacer el import, tenemos que ejecutar el comando pip install sqlite3, en la consola
import sqlite3
from tqdm import tqdm
import smtplib




def sendmailnow():
    print("Solo falta configurar el usuario y contrasena y ya se puede usar")
    try:
        message = str(input("Mensaje: "))
        destintario = str(input("destintario: "))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login("Your mail", "Your password")

        server.sendmail("addressee", destintario, message)
        server.quit()
        print("Finish")
    except:
        print("Error en sendmailnow")


def barload():
    for i in tqdm(range(int(9e6)), ascii = True, desc = "Loading.."):
        pass



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
            barload()#Simulador de carga
            print("FINISH")
    except:
        print('Error De valores')#Fin de la funcion
        
#Search Person
def search():
    iduser = str(input("ID of the User: "))
    cursor.execute("SELECT * FROM USER WHERE ID={0}".format(iduser))
    data = cursor.fetchone()
    print('|','Id user:', data[0], ' ', '\t', 'Name user: ',data[1], '\t','old year: ', data[2], '\t', '|')

def mostrar():#Inicio funcion para mostrar
    cursor.execute("SELECT * FROM USER")
    variable_users = cursor.fetchall()
    for user in variable_users:
        print('-'*74)
        print('|','ID user: ', user[0], ' ','\t', 'Name user: ', user[1], '\t', 'Old year user: ', user[2],'\t', '|')#Fin de la funcion
    print('-'*74)
print('1.Add to data base', '\n', '2. show data base', '\n', "3.enviar correo", '\n', "4.Mostrar dato especifico por ID")

option = str(input('Option: '))

if option == '1':
    agregar()
elif option == '2':
    mostrar()
elif option == "3":
    sendmailnow()
elif option == "4":
    search()
else:
    print("     ", option, 'Invalida')
    print('Opcion de valor invalida')

conection.commit()
conection.close()
print('Finish')
