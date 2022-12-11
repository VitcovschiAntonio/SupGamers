import customtkinter

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self,parent, controller, *args, **kwargs):
        super().__init__(parent,*args, **kwargs)

        self.login_label = customtkinter.CTkLabel(self, text="CustomTkinter\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.password_entry = customtkinter.CTkEntry(self, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = customtkinter.CTkButton(self, text="Login",command=lambda:controller.show_frame('MainFrame') , width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        self.msg_label = customtkinter.CTkLabel(self, text="Are you new tu SupGamers?",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"))
        self.msg_label.grid(row=4, column=0, padx=30, pady=(15, 15))

        self.register_button = customtkinter.CTkButton(self, text="Register", command=lambda:controller.show_frame('RegisterFrame'),width=200)
        self.register_button.grid(row=5, column=0, padx=30, pady=(5, 15))