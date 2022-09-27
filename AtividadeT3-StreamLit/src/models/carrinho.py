from controllers.product_controller import ProductController
class Carrinho():
    def __init__(self,products):
        products = ProductController().getProducts()
        
        
        