from tkinter.ttk import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *

class LoginUI:
    def _construir_base(self):
        janela = ttk.Window(
            title="Minha GUI Mauá",
            size= (1440,1024),
            position= (100,100),
            minsize= (600,300),
            maxsize= (1800,900),
            themename= "flatly",
            alpha=1.0
        ).iconphoto(False, PhotoImage(file='Imagens/github_icon.png'))
        return janela
    
    def __init__(self) -> None:
        self.janela = self._construir_base()
        
        
    
    def run(self):
        self.janela.mainloop()
        
     
    
        

        