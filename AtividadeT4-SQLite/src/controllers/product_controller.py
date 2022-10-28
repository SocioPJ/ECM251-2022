from dao.product_dao import ProductDAO
from models.product import Product
class ProductController():
    def __init__(self):
        pass 
    # def getProducts(self):
    #     for i in range(len(self.product)):
    #         return self.product
    def pegar_item(self, id):
        item = ProductDAO.get_instance().get
        return item

    def inserir_item(self, item) -> bool:
        try:
            ProductDAO.get_instance().inserir_item(item)
        except:
            return False
        return True
    
    def pegar_todos_itens(self) -> list[Product]:
        itens = ProductDAO.get_instance().get_all()
        return itens
    
    
    
    