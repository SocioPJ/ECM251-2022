from controllers.product_controller import ProductController
from models.product import Product
from dao.product_dao import ProductDAO

controller = ProductController()


# items = controller.pegar_todos_itens()
# for item in items:
#     print(item)
    
produto1 = Product(4,"aaaaa",19.99,"blabla")
print(produto1.id)
print(produto1.name)
print(produto1.price)
print(produto1.url)

print(controller.inserir_item(produto1))
print(controller.pegar_todos_itens())

#print(ProductDAO.get_instance().inserir_item(produto1))



# novo_item = Product("OLA1", "Cooler REDRAGON Vermelho", 19.90)
# print(controller.inserir_item(novo_item))

# print("**************************************")
# items = controller.pegar_todos_itens()
# for item in items:
#     print(item)

# print("**************************************")
# item = controller.pegar_item("CAF6")
# print(item)
