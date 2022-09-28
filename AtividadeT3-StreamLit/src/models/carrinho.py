from controllers.product_controller import ProductController
class Carrinho():
    def __init__(self,products,value):
        self.products = products
        products = []
        self.value = 0
        self.value = self.calcular_valor()
        
    def __str__(self) -> str:
        return f'Carrinho(products:{self.products}, value:{self.value})'
    
    def getProducts(self):
        return self.products
    
    def getList(self):
        i=0
        for i in range(len(self.products)):
            cont = i+1
        