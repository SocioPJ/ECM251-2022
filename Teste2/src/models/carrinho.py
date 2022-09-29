from controllers.product_controller import ProductController
class Carrinho():
    def __init__(self):
        self.products = []
        self.quantidade = 1

    def addProduct(self, product):
        self.products.append(product)
    
    def verQuantidade(self,quantidade):
        return self.quantidade*quantidade

    def getList(self):
        return self.products

    def getQuantidade(self):
        return self.quantidade