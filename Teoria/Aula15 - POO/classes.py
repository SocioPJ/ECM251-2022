from pydoc import describe


class Carrinho:
    #Método construtor
    def __init__(self): # __init__ é um método construtor do Python
        self.itens = []
    #Demais métodos
    def get_valor_total(self):
        pass    # equivalente a abre e fecha chaves vazios
    def get_quantidade_itens(self):
        pass
    def adicionar_item(self, item):
        pass
    def remover(self,item):
        pass

class Item():
    #Construtor
    def __init__(self, preço, nome, descrição = None):
        self._nome = nome
        self._preço = preço
        self._descrição = descrição
    def get_nome(self):
        return self._nome
    def __str__(self):
        return f'Nome : {self._nome}, Preço: {self._preço}, Descrição: {self._descrição}'

    #Métodos


item1 = Item(
    preço = 350,
    nome = 'Dark Souls 3')

item2 = Item(
    preço = 100,
    nome = 'Elden Ring',
    descrição = 'Jogo de RPG Mundo aberto')

print (item1.get_nome())
print(item1)