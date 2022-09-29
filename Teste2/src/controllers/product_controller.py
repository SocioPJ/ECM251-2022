from models.product import Product
class ProductController():
    def __init__(self):
        #Carrega os dados dos produtos
        self.product = [
            Product("Travesseiro Albedo",89.97,"https://http2.mlstatic.com/D_NQ_NP_2X_947943-MLB49335290710_032022-F.webp"),
            Product("Travesseiro Sukuna",1430.99,"https://http2.mlstatic.com/D_NQ_NP_2X_829677-MLB49337211586_032022-F.webp"),
            Product("Travesseiro Makima",11990.90,"https://http2.mlstatic.com/D_NQ_NP_2X_660537-MLB49337065154_032022-F.webp"),
        ]
    def getProducts(self):
        for i in range(len(self.product)):
            return self.product
    
    
    
    