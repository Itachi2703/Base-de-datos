
import sqlite3



conection = sqlite3.connect('dbnew') #Creamos y nos conectamos ala base de datos
cursor = conection.cursor() #Cramos un cursor
#cursor.execute("CREATE TABLE USER (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(20), OLDYEAR INTEGER, JOB VARCHAR(20), SalaryBYhr INTEGER, SalaryBYWeek INTEGER)")

print("db created")

class dbs:#clase de todas las operaciones sobre la base de datos



    def user_by_ID():
        try:
            id_of_the_user = str(input("Id of the user: "))
            cursor.execute("SELECT * FROM USER WHERE ID={0}".format(id_of_the_user))
            data = cursor.fetchone()
            print("="*20)
            print("ID: ", data[0], "NAME: ", data[1], "AGE: ", data[2], "JOBS",data[3], "salary by hr: ", data[4], "salary by week: ", data[5])
            conection.commit()
        except:
            print(id_of_the_user, "not valid")
    def add_to_db():
        try:
            print("Add to Data Base")
            i = 1
            number_of_users = int(input("Number of the users: "))
            while i <= number_of_users:
                i = i + 1
                print("Option for add to Data Base")
                print("="*20)
                nombre = str(input("Nombre de la persona: "))
                print("="*20)
                edad = int(input("Your age: "))
                print("="*20)
                job = str(input("Enter you job: "))
                print("="*20)
                salarybyweek = int(input("Salary by hr: "))
                print("="*20)
                salarybyhr = int(input("Salary by Week: "))
                print("="*20)

                var_of_the_use = [
                   (nombre, edad, job, salarybyhr, salarybyweek)
                ]
                cursor.executemany("INSERT INTO USER VALUES (NULL, ?,?,?,?,?)",var_of_the_use)
                conection.commit()
            conection.commit()
        except:
            print("Error of datas")
    def show_data_base():

        cursor.execute("SELECT * FROM USER")
        data = cursor.fetchall()
        for i in data:
            print("ID: ", i[0], "NAME: ", i[1], "AGE: ", i[2], "JOBS",i[3], "salary by hr: ", i[4], "salary by week: ", i[5])
            conection.commit()
    def change_datas_by_id():
        try:
            print("Change datas of the user by ID")
            id_of_the_user = str(input("Id of the user to Change: "))
            cursor.execute("SELECT * FROM USER WHERE ID={0}".format(id_of_the_user))
            data = cursor.fetchone()
            print("="*20)
            print("ID: ", data[0], "NAME: ", data[1], "AGE: ", data[2], "JOBS",data[3], "salary by hr: ", data[4], "salary by week: ", data[5])
            print("1.SI \t 2.NO")
            yess_and_not = str(input("This is user to change: "))
            print("="*20)
            print(" 1.NAME \t 2.OLDYEAR \t 3.JOB \t 4.SalaryBYhr \t 5.SalaryBYWeek")
            print("="*20)
            qelqc = str(input("Que desea cambiar: "))
            if yess_and_not == "1":
                if qelqc == "1":#change to name
                    print("change to name")
                    new_name = str(input("New name of the user: "))
                    cursor.execute("UPDATE USER SET NAME='{0}' WHERE ID={1}".format(new_name, id_of_the_user))
                    print("Change completed...")
                    conection.commit()
                elif qelqc == "2":#change to OLDYEAR
                    print("change to OLDYEAR")
                    new_name = str(input("New age of the user: "))
                    cursor.execute("UPDATE USER SET OLDYEAR='{0}' WHERE ID={1}".format(new_name, id_of_the_user))
                    print("Change completed...")
                    conection.commit()
                elif qelqc == "3":#change to JOB
                    print("change to JOB")
                    new_name = str(input("New job of the user: "))
                    cursor.execute("UPDATE USER SET JOB='{0}' WHERE ID={1}".format(new_name, id_of_the_user))
                    print("Change completed...")
                    conection.commit()
                elif qelqc == "4":#change to SalaryBYhr
                    print("change to salary by hr")
                    new_name = str(input("New Salary BY hr of the user: "))
                    cursor.execute("UPDATE USER SET SalaryBYhr='{0}' WHERE ID={1}".format(new_name, id_of_the_user))
                    print("Change completed...")
                    conection.commit()
                elif qelqc == "5":#change to SalaryBYWeek
                    print("change to salary by week")
                    new_name = str(input("New Salary BY Week of the user: "))
                    cursor.execute("UPDATE USER SET SalaryBYWeek='{0}' WHERE ID={1}".format(new_name, id_of_the_user))
                    print("Change completed...")
                    conection.commit()
                else:
                    print(qelqc, "Not valid")
            elif yess_and_not == "2":
                print("Execute la opcion 2 para ver todos los usuarios y asi ver el correcto")
            else:
                print(yess_and_not, " Not valid")
            conection.commit()
        except:
            print("Error of datas")
conection.commit()

