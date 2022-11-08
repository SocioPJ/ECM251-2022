from models.cart import Cart
from controllers.product_controller import ProductController
from dao.cart_dao import CartDAO
class CartController():
    def __init__(self):
        pass
    
    
    def inserir_item(self, item) -> bool:
        try:
            CartDAO.get_instance().inserir_item_carrinho(item)
        except:
            return False 
        return True
    
    def pegar_todos_itens(self) -> list[Cart]:
        try: 
            return CartDAO.get_instance().get_all()
        except:
            print("Erro ao pegar todos itens")
            
    def deletar_item_carrinho(self, id) -> bool:
        try:
            return CartDAO.get_instance().deletar_item_carrinho(id)
        except:
            raise Exception(" Erro ao deletar item ")
    
    def pegar_quantidade_item_carrinho(self,id):
        try:
            return CartDAO.get_instance().pegar_quantidade_item_carrinho(id)
        except:
            print('Erro pegar quantidade de um item no carrinho')
            
    def pegar_preco_item_carrinho(self,id):
        try:
            return CartDAO.get_instance().pegar_preco_item_carrinho(id)
        except:
            print('Erro pegar quantidade de um item no carrinho')
            
    def atualizar_quantidade_item_carrinho(self,id,quantidade):
        try:
            return CartDAO.get_instance().atualizar_quantidade_item_carrinho(id,quantidade)
        except:
            print('erro ao atualizar quantidade produto')
    
   