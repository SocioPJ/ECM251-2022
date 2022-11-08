from controllers.cart_controller import CartController
from controllers.product_controller import ProductController
from models.cart import Cart


controller_carrinho = CartController()
controller_produto = ProductController()

# produtos = controller_produto.pegar_todos_itens()
# print(produtos[1])
# produto = produtos[1]
# quantidade = 2

# item = Cart(produto.id,produto.name,produto.price,produto.url,quantidade) 
# carrinho = controller_carrinho.inserir_item(item)

controller_carrinho.deletar_item(0)
controller_carrinho.deletar_item(1)