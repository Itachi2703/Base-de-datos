from moduleSearchbyId import sendmail
from FolderDB import DBcon

print('1.Add to data base', '\n', '2. show data base', '\n', "3.Mostrar dato especifico por ID",'\n', '4.Cambiar Nombre o edad')

option = str(input('Option: '))
if option == "1":
    print("hi guys")
    DBcon.dbs.add_to_db()
elif option == "2":
	DBcon.dbs.show_data_base()
elif option == "3":
	DBcon.dbs.user_by_ID()
elif option == "4":
	DBcon.dbs.change_datas_by_id()
else:
    print(option, " Not valid")
