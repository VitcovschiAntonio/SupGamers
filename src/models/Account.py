from Password import Password


class User:
    def __init__(self, username: str, password: str):
        # USER CREDENTIAL INFORMATION
        self.username = username
        self.password = Password(password)
        self.email = ''
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







        


