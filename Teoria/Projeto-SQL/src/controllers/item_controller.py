from src.models.item import Item
from src.dao.item_dao import ItemDAO
class ItemController:
    def __init__(self):
        pass
    
    def pegar_item(self,id):
        item = ItemDAO.get_instance().pegar_item(id)
        return item
    
    def pegar_todos_itens(self):
        itens = ItemDAO.get_instance().get_all()
        return itens
    
    def atualizar_item(self,item):
        return ItemDAO.get_instance().atualizar(item)
    
    def deletar_item(self,id):
        return ItemDAO.get_instance().deletar_item(id)
    
    def buscar_todos_itens_nome(self,nome):
        itens = ItemDAO.get_instance.search_all_for_name(nome)
        return itens