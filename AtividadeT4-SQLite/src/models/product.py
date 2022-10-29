class Product():
    def __init__(self,id,name, price, url):
        self.id = id
        self.name = name
        self.price = price
        self.url = url
        
    def __str__(self) -> str:
        return f'Product(id:{self.id}, name:{self.name}, price:{self.price}, url:{self.url})'
    def __eq__(self, __o: object) -> bool:
        if type(__o) != Product:
            return False
        return self.name == __o.name
    
    @classmethod
    def criar_novo_produto(self,id,name,price,url):
        produto = Product(id,name,price,url)
        return produto