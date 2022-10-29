from ast import expr_context
from dao.product_dao import ProductDAO
from models.product import Product
class ProductController():
    def __init__(self):
        pass 
    # def getProducts(self):
    #     for i in range(len(self.product)):
    #         return self.product
    def pegar_item(self, id):
        item = ProductDAO.get_instance()
        return item

    def inserir_item(self, item) -> bool:
        try:
            ProductDAO.get_instance().inserir_item(item)
        except:
            return False
        return True
    
    def pegar_todos_itens(self) -> list[Product]:
        try:
            itens = ProductDAO.get_instance().get_all()
            return itens
        except:
            print("Erro ao pegar todos itens")
            
    def deletar_item(self, id) -> bool:
        return ProductDAO.get_instance().deletar_item(id)
    
    
    
    