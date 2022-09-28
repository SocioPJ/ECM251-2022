from controllers.product_controller import ProductController
class Carrinho():
    def __init__(self):
        self.products = []
        self.quantidade = 1

    def addProduct(self, product):
        self.products.append(product)
    
    def getList(self):
        return self.products

    