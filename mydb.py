

import mysql.connector

# cnx = mysql.connector.connect(user='root', password='Mysql@123', host='localhost')

dataBase = mysql.connector.connect(
     host ='mylocal.mysql.pythonanywhere-services.com',
     user ='mylocal',
     passwd ='Mydata@12',
    #  auth_plugin='mysql_native_password'
 )

#prepare a cursor object
cursorObject = dataBase.cursor()


#Create a database
cursorObject.execute("CREATE DATABASE mylocal")

print ("All DOne!")