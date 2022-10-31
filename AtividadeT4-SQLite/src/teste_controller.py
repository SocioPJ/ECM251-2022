from controllers.product_controller import ProductController
from models.product import Product
from dao.product_dao import ProductDAO

controller = ProductController()


# items = controller.pegar_todos_itens()
# for item in items:
#     print(item)
    
# produto1 = Product(1,"aaaaa",19.99,"blabla")
# print(produto1.id)
# print(produto1.name)
# print(produto1.price)
# print(produto1.url)

# id_input = int(input("digite id: "))
# name_input = input("digite nome: ")
# price_input = float(input("digite preço: "))
# url_input = input('digite url:')

# produto2 = Product(id_input,name_input,price_input,url_input)
controller.deletar_item(0)
controller.deletar_item(1)
controller.deletar_item(2)
controller.deletar_item(3)
controller.deletar_item(4)
controller.deletar_item(5)
controller.deletar_item(6)
controller.deletar_item(7)
controller.deletar_item(8)
controller.deletar_item(9)
controller.deletar_item(10)
# controller.inserir_item(Product(0,"bla",10.99,'abobora'))
# controller.inserir_item(Product(0,"bla",10.99,'abobora'))
# controller.inserir_item(Product(2,"bla",10.99,'abobora'))


# controller.inserir_item(Product(1,"azeitona",20.50,'canja'))
# print(controller.pegar_item(0))
# print(controller.buscar_todos_itens_nome("bla"))





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
