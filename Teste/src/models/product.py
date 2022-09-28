class Product():
    def __init__(self,name, price, url,id):
        self.name = name
        self.price = price
        self.url = url
        self.id = id
    def __str__(self) -> str:
        return f'Product(name:{self.name}, price:{self.price}, url:{self.url}, id:{self.id})'