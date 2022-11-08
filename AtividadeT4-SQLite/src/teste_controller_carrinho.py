from controllers.cart_controller import CartController
from controllers.product_controller import ProductController
from dao.cart_dao import CartDAO
from models.cart import Cart


controller_carrinho = CartController()
controller_produto = ProductController()



# produtos = controller_produto.pegar_todos_itens()
# print(produtos[1])
# produto = produtos[1]
# quantidade = 2

# item = Cart(produto.id,produto.name,produto.price,produto.url,quantidade) 
# carrinho = controller_carrinho.inserir_item(item)

# print(controller_carrinho.pegar_quantidade_item_carrinho(0))
# quantidade = 2
# controller_carrinho.atualizar_quantidade_item_carrinho(0,quantidade)
# print(controller_carrinho.pegar_quantidade_item_carrinho(0))

# print(CartDAO.get_instance().pegar_quantidade_item_carrinho(0))
# CartDAO.get_instance().atualizar_quantidade_item_carrinho(0,quantidade)
# print(CartDAO.get_instance().pegar_quantidade_item_carrinho(0))

for itens in controller_carrinho.pegar_todos_itens():
    controller_carrinho.deletar_item_carrinho(itens.product_id)