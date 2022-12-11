
import customtkinter
from login import LoginFrame
from register import RegisterFrame
from main_frame import MainFrame

from PIL import Image
import os

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 1220
    height = 680
    def __init__(self):
        super().__init__()

        # Window settings
        self.geometry(f"{self.width}x{self.height}")
        self.title("SupGamers")
        self.resizable(False,False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/res/login.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)
        
        # root frame for other frames such as login panel or register etc.
        self.container = customtkinter.CTkFrame(self)
        self.container.grid(row=0,column=0,sticky='ns')
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
       
        self.frames= []  # which is actually the current frame linked to the main container
        self.show_frame('LoginFrame') # show LoginFrame
        
    # This is actually the method where the panes are switched on the container    
    def show_frame(self, name:str):

        if name == 'LoginFrame':   
            if len(self.frames) == 0:
                F = LoginFrame(self.container, self)
                self.frames.append(F)
                print(self.frames)
            else:
                self.frames[0].grid_forget()
                self.frames.pop(0)
                F = LoginFrame(self.container, self)
                self.frames.append(F)
                print(self.frames)

            F.grid(row=0,column=0,sticky='ns')
        elif name == 'RegisterFrame':
            self.frames[0].grid_forget()
            self.frames.pop(0)
            F = RegisterFrame(self.container, self)
            self.frames.append(F)
            F.grid(row=0,column=0)
            print(self.frames)  
        
        elif name == 'MainFrame':     
            self.frames[0].grid_forget()
            self.frames.pop(0)
            F = MainFrame(self.container, self)
            self.frames.append(F)
            F.grid(row=0,column=0,sticky='ns')
            self.container.configure(width=900)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()