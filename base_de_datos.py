import sqlite3

conection = sqlite3.connect('MiDB')
cursor = conection.cursor()

conection.commit()
conection.close()
print('Finish')