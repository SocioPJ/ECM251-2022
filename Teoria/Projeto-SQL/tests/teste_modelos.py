from src.models.pedido import Pedido 
from src.models.item import Item

pedido1 = Pedido(1,"abc",10,"qwerty", "teste", "19/10/2022-9:18")
pedido2 = Pedido(2,"def",20,"qwerty", "teste", "19/10/2022-9:18")

print(pedido1)
print(pedido2)

item1 = Item(1,"jogo",10.99)
item2 = Item(2,"jogo2",20.99)

print(item1)
print(item2)