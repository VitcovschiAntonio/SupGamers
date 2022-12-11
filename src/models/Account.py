from Password import Password


class User:
    def __init__(self, username: str, password: str, email :str):
        # USER CREDENTIAL INFORMATION
        self.username = username
        self.password = Password(password)
        self.email = email
        self.phonenumber = 0
        self.firstname= ''
        self.lastname = ''
        # FEaTS
        self.wallet = 0
        self.orders = {}
        self.products  = {}

    def get_username(self) ->str:
        return self.username

    def get_email(self) ->str:
        return self.username

    def get_phoneNumber(self) -> int:
        return self.phonenumber

    def set_phoneNumber(self,number):
        try:
            self.phonenumber = int(number) 
          
        except ValueError:
            print('Please use a valid phone number (Numbers only!)')

    def get_wallet(self) -> int:
        return self.wallet

    def set_wallet(self, number):
        try:
            self.wallet = int(number) 
          
        except ValueError:
            print('WAllet.ERROR (Numbers only!)')




import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd ='1234',
    database = 'supgamers'
)

mycursor = mydb.cursor()
u = User('add44','1234','test@yahoo.com')
u1 = User('add2','1234','tes1@yahoo.com')

query = '''

SELECT EXISTS(SELECT * FROM users WHERE username = 'add22')
'''

mycursor.execute(query)

for u in mycursor:
    print(u)




        


