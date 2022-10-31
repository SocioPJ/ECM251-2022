import streamlit as st
from dao.product_dao import ProductDAO
from models.product import Product
class ProductController():
    def __init__(self):
        pass 
    # def getProducts(self):
    #     for i in range(len(self.product)):
    #         return self.product
    def pegar_item(self, id):
        item = ProductDAO.get_instance().pegar_item(id)
        return item

    
    def inserir_item(self, item) -> bool:
        try:
            ProductDAO.get_instance().inserir_item(item)
        except:
            return False 
        return True
    
    def pegar_todos_itens(self) -> list[Product]:
        try:
            itens = ProductDAO.get_instance().get_all()
            return itens
        except:
            print("Erro ao pegar todos itens")
            
    def deletar_item(self, id) -> bool:
        try:
            return ProductDAO.get_instance().deletar_item(id)
        except:
            raise Exception(" Erro ao deletar item ")
    
    def atualizar_item(self,item):
        try:
            return ProductDAO.get_instance().atualizar_item(item)
        except:
            raise Exception("Erro ao atualizar item")
    
    def buscar_todos_itens_nome(self, name) -> list[Product]:
        itens = ProductDAO.get_instance().search_all_for_name(name)
        return itens
    
    
    
    