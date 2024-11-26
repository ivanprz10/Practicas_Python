#realizando la conexion a una base de datos de mysql e imprimiendo los resultados

import mysql.connector
#importando la libreria "mysql.connector" Este módulo permite conectar y trabajar con bases de datos MySQL desde Python.
# en dado caso de no contar con ella la instalaremos en la terminal con: 
#pip install mysql-connector-python

conector = mysql.connector.connect(#crea la conexion a la base de datos con los parametros siguientes
    user = "root",                  #nombre de usuario de mysql
    password = "Examen0202",        #contraseña de mysql
    host = "localhost",             #host de mysql
    database = "primera_conexion"   #nombre de la base de datos

)
cursor = conector.cursor()                  
cursor.execute("SELECT * FROM Usuario")

result = cursor.fetchall()

for user in result:
    print(user)