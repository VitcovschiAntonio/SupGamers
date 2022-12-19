import sys
sys.path.insert(1,'C:/Users/Tons/Desktop/SupGamers/src/models')
from Account import User
sys.path.insert(2,'C:/Users/Tons/Desktop/SupGamers/src/database')
from backend import Backend



class SupGamersAPI:
    def __init__(self):
        pass
    
    def create_account(self, username:str, password:str, email:str) -> bool:
        b = Backend()
        if b.check_existing(username):
            print('Username allready taken')
            return False
            
        else:
            b.create_account(username,password,email)
            return True

    def check_credentials(self, username:str, password :str) ->bool:
        b = Backend()
        if b.check_credentials(username,password):
            return True
        else: return False
        

       



        