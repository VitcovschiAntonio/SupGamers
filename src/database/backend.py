import mysql.connector
 
class Backend:
    def __init__(self):
        # Conexion to db
        self.mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd ='1234',
        database = 'supgamers')
        self.response = False

        self.mycursor = self.mydb.cursor()
    # ACCOUNT CREATION
    def check_existing(self, username:str)->bool:
        query = f'''
          SELECT EXISTS(SELECT * FROM users WHERE username = '{username}')
                                                                          '''
        response = -1
        self.mycursor.execute(query)
        for x in self.mycursor:
             response = x[0]
        
        if response == 1:
            return True
        else:
            return False

    def create_account(self,username :str, password :str, email :str):
        query = f'''
        INSERT INTO users
        VALUES('{username}','{password}','{email}');
        '''
        self.mycursor.execute(query)
        self.mydb.commit()

    # ACCOUNT AUTHENTIFICATION
    def check_credentials(self, username :str, password :str)->bool:
        query = f'''
                    SELECT EXISTS(SELECT * FROM users WHERE username = '{username}' AND password = '{password}')
                                                                                                      '''
        response = -1
        self.mycursor.execute(query)
        for x in self.mycursor:
             response = x[0]
        
        if response == 1:
            
            return True
        else:
            
            return False

    


        

        






  






