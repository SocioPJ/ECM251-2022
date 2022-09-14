import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *
from login import LoginUI


if __name__ == "__main__":
    app = LoginUI()
    app.run()




# class MinhaUI():
#     def acao_botao(self):
#         print("Click!")

#     def _construir_base(self):
#         janela = ttk.Window(
#             title="Minha GUI Mauá",
#             size= (1024,400),
#             position= (100,100),
#             minsize= (600,300),
#             maxsize= (1800,900),
#             alpha=1.0
#         )
#         janela.iconphoto(False, PhotoImage(file='calculator.png'))
#         return janela

#     def __init__(self) -> None:
#         self.base = self._construir_base()
#         #Criando um botão
#         ttk.Button(
#             self.base,
#             text="Ola Mundo!",
#             bootstyle="default",
#             command=self.ativar_bot
#         ).pack(side=LEFT, padx= 10, pady=5)

#         #Criando um segundo botão
#         self.bot2 = ttk.Button(
#             self.base,
#             text="Segundo Botão",
#             bootstyle=(DANGER,OUTLINE),
#             command=self.desativar_bot
#         )
#         self.bot2.pack(side=LEFT, padx= 10, pady = 5)
#     def run(self):
#         self.base.mainloop()
    
#     def ativar_bot(self):
#         print('Ligando o botão')
#         self.bot2.configure(state='enabled')
#     def desativar_bot(self):
#         print('Desligando o botão')
#         self.bot2.configure(state='disabled')


    

