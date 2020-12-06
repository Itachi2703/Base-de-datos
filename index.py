from moduleSearchbyId import sendmail
from FolderDB import DBcon

print('1.Add to data base', '\n', '2. show data base', '\n', "3.enviar correo", '\n', "4.Mostrar dato especifico por ID",'\n', '5.Cambiar Nombre o edad', '\n', "6.Crear tabla")

option = str(input('Option: '))
if option == '1':
    DBcon.dbcone.agregar()
elif option == '2':
    DBcon.dbcone.mostrar()
elif option == "3":
    sendmail.sendmailclass.sendmailnow()
elif option == "4":
    DBcon.dbcone.search()
elif option == '5':
    DBcon.dbcone.cambiaruser()
else:
    print("     ", option, 'Invalida')
    print('Opcion de valor invalida')
