from controllers.product_controller import ProductController
import streamlit as st
class Cart():
    def __init__(self, product_id, product_name, product_price, product_url, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_url = product_url
        self.quantity = quantity
    
    def __str__(self):
        return f'Cart(Product_id: {self.product_id}, Product_name: {self.product_name}, Product_price: {self.product_price}, Product URL: {self.product_url}, Quantity: {self.quantity})'
        

    # def addProduct(self, product):
    #     if product not in st.session_state["carrinho"].getList():
    #         self.products.append(product)
    #     else:
    #         st.error("Produto já adicionado ao carrinho!")
    
    # def verQuantidade(self):
    #     return self.quantidade*st.session_state["quantidade"]

    # def getList(self):
    #     return self.products

    # def getQuantidade(self):
    #     return self.quantidade
    
    # def removeProduct(self,product):
    #     if product in st.session_state["carrinho"].getList():
    #         self.products.remove(product)
    #     else:
    #         print('Não existe o produto no carrinho')
    
    # def remover_todos_produtos(self):
    #     for product in st.session_state['carrinho'].getList():
    #         self.products.remove(product)