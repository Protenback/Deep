

import pymssql

server = 'jvpdatos.database.windows.net'
user = 'jcverni@jvpsa.onmicrosoft.com@jvpdatos'
password = 'Juan11121923'
database = 'Laboratorio'
conn = pymssql.connect(server, user, password, database)

cursor = conn.cursor()  
cursor.execute('Select * from Total_Abril_2020_Consolidado where Promedio IS NOT NULL ')  
print (cursor)
usuarios = cursor.fetchall()

for usuario in usuarios:
 
    print(usuario[0],usuario[1],usuario[2])


    
    