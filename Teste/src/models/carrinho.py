from controllers.product_controller import ProductController
class Carrinho():
    def __init__(self):
        self.products = []
        self.total = 0

    def addProduct(self, product):
        self.products.append(product)
        self.total += product.price
    
    def getList(self):
        return self.products