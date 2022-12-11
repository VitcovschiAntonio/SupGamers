import mysql.connector
from Account import User

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd ='1234',
    database = 'supgamers'
)

mycursor = mydb.cursor()

idk = 'INSERT INTO users (username,password,email) VALUES (%s, %s)'
user = ('add22','1234','test1@yahoo.com')

mycursor.execute(idk, user)



u = User('add44','1234','test@yahoo.com')
u1 = User('add22','1234','tes1@yahoo.com')