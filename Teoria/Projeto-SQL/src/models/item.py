class Item:
    def __init__(self,id,nome,preco):
        self.id = id
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f'Item["id":{self.id},"nome":{self.nome},"preco":{self.preco}]'