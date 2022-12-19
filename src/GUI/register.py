import customtkinter
import sys
sys.path.insert(0,'C:/Users/Tons/Desktop/SupGamers/src/API')
from api import SupGamersAPI

class RegisterFrame(customtkinter.CTkFrame):
    def __init__(self,parent,controller, *args, **kwargs):
        super().__init__(parent,*args, **kwargs)

        
        self.username_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="username *")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.password_entry = customtkinter.CTkEntry(self, width=200, show="*", placeholder_text="password *")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.email_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="email *")
        self.email_entry.grid(row=3, column=0, padx=30, pady=(15, 15))

        self.phone_entry = customtkinter.CTkEntry(self, width=200, show="*", placeholder_text="phone number")
        self.phone_entry.grid(row=4, column=0, padx=30, pady=(0, 15))

        self.firstName_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="first name")
        self.firstName_entry.grid(row=5, column=0, padx=30, pady=(15, 15))

        self.lastName_entry = customtkinter.CTkEntry(self, width=200, show="*", placeholder_text="last name")
        self.lastName_entry.grid(row=6, column=0, padx=30, pady=(0, 15))

        self.create_button = customtkinter.CTkButton(self, text="Create",  width=200,command = self.create 
        ,fg_color='gray')
        self.create_button.grid(row=8, column=0, padx=30, pady=(5, 15))

        self.back_button = customtkinter.CTkButton(self, text="go back",command=lambda: controller.show_frame('LoginFrame') , width=200)
        self.back_button.grid(row=9, column=0, padx=30, pady=(5, 15))
 
    def create(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()

        api = SupGamersAPI()
        if api.create_account(username,password,email):
            print('User Details:\n')
        else:
            print('Gresit')
    
        
        



