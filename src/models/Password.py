from cryptography.fernet import Fernet

class Password:
    def __init__(self, password:str):
        _key = Fernet.generate_key()
        self.fernet = Fernet(_key)
        self._password = password
        self._password = self.encrypt_password()

    def encrypt_password(self):
        return self.fernet.encrypt(self._password.encode())

    def _decrypt_password(self):
        return self.fernet.decrypt(self._password).decode()

