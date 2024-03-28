

import mysql.connector

# cnx = mysql.connector.connect(user='root', password='Mysql@123', host='localhost')

dataBase = mysql.connector.connect(
     host ='localhost',
     user ='root',
     passwd ='Mysql@123',
     auth_plugin='mysql_native_password'
 )

#prepare a cursor object
cursorObject = dataBase.cursor()


#Create a database
cursorObject.execute("CREATE DATABASE myapp")

print ("All DOne!")