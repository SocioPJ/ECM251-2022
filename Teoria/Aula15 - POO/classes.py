class Carrinho:
    #Método construtor
    def __init__(self): # __init__ é um método construtor do Python
        self.itens = []
    #Demais métodos
    def get_valor_total(self):
        pass
    def get_quantidade_itens(self):
        pass
    def adicionar_item(self, item):
        pass
    def remover(self,item):
        pass

class Item():
    #Construtor
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor


item = Item("Celular", 1000)
print(item.get_nome())