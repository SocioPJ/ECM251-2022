from controllers.product_controller import ProductController
from models.product import Product
from dao.product_dao import ProductDAO

controller = ProductController()


# items = controller.pegar_todos_itens()
# for item in items:
#     print(item)
    
produto1 = Product(1,"aaaaa",19.99,"blabla")
print(produto1.id)
print(produto1.name)
print(produto1.price)
print(produto1.url)

id_input = int(input("digite id: "))
name_input = input("digite nome: ")
price_input = float(input("digite preço: "))
url_input = input('digite url:')

produto2 = Product(id_input,name_input,price_input,url_input)
controller.inserir_item(produto2)

# print(controller.inserir_item(produto1))
# print(controller.deletar_item(1))


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
