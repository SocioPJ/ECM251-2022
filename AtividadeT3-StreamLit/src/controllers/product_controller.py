from models.product import Product
class ProductController():
    def __init__(self):
        #Carrega os dados dos produtos
        self.product = [
            Product("paçoca",10.99,"https://www.acasaencantada.com.br/wp-content/uploads/2021/09/casaencantada_capablog_pacoca-fit-1200x900.png"),
            Product("pimenta verde",5.99,"https://tudoela.com/wp-content/uploads/2018/09/Pimenta-verde-3.jpg"),
            Product("berinjela",399.90,"https://static.tuasaude.com/media/article/2n/7p/berinjela_14525_l.jpg"),
        ]
    def getProducts(self):
        return self.product
    
    
    
    