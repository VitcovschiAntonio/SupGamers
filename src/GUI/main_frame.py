import customtkinter

class MainFrame(customtkinter.CTkFrame):
    def __init__(self,parent, controller, *args, **kwargs):
        super().__init__(parent,*args, **kwargs,width=400)

    
        self.main_label = customtkinter.CTkLabel(self, text="CustomTkinter\nMain Page",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"),width=500)
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        self.back_button = customtkinter.CTkButton(self, text="go back",command=lambda: controller.show_frame('LoginFrame') , width=200)
        self.back_button.grid(row=9, column=0, padx=30, pady=(5, 15))