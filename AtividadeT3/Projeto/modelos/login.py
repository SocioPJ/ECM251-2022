from turtle import color
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *

class LoginUI():
    def _construir_base(self):
        janela = ttk.Window(
            title="Minha GUI Mauá",
            size= (1440,1024),
            position= (100,100),
            minsize= (600,300),
            maxsize= (1800,900),
            alpha=1.0
        ).iconphoto(False, PhotoImage(file='Imagens/github_icon.png'))
        ttk.Frame(
            janela,
            bootstyle="default",
            height= 100,
            width=200,
        ).pack(padx = 100, pady = 100)
        
        return janela
    
    def __init__(self) -> None:
        self.base = self._construir_base()
        

        