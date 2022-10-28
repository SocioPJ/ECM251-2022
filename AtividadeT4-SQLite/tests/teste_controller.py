from src.controllers.product_controller import ProductController
from src.models.product import Product

controller = ProductController()

produto1 = Product(1,"blabla",19.99,"blabla")
print(produto1.id)
print(produto1.name)
print(produto1.price)
print(produto1.url)

print(controller.inserir_item(produto1))
