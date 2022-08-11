from item import Item
#from carrinho import Carrinho
item1 = Item(
    preço = 350,
    nome = 'Dark Souls 3')

item2 = Item(
    preço = 100,
    nome = 'Elden Ring',
    descrição = 'Jogo de RPG Mundo aberto')

carrinho1 = Carrinho
carrinho1.adicionar_item(item1)
carrinho1.adicionar_item(item2)
#print(carrinho1.get_quantidade_itens())

print (item1.get_nome())
print(item1)