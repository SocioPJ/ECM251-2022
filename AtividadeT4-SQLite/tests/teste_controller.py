from src.controllers.product_controller import ProductController
from src.models.product import Product

controller = ProductController()

# items = controller.pegar_todos_itens()
# for item in items:
#     print(item)
    
produto1 = Product(1,"blabla",19.99,"blabla")
print(produto1.id)
print(produto1.name)
print(produto1.price)
print(produto1.url)

print(controller.inserir_item(produto1))



# novo_item = Product("OLA1", "Cooler REDRAGON Vermelho", 19.90)
# print(controller.inserir_item(novo_item))

# print("**************************************")
# items = controller.pegar_todos_itens()
# for item in items:
#     print(item)

# print("**************************************")
# item = controller.pegar_item("CAF6")
# print(item)