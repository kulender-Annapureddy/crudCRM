import pymysql

dataBase = pymysql.connect(

	host ='localhost',
	user= 'root',
	passwd = '70676123'
   
	)

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute('CREATE DATABASE crudCRM')

print('All good')