from controllers.product_controller import ProductController
import streamlit as st
class Carrinho():
    def __init__(self):
        self.products = []
        self.quantidade = 1

    def addProduct(self, product):
        self.products.append(product)
    
    def verQuantidade(self):
        return self.quantidade*st.session_state["quantidade"]

    def getList(self):
        return self.products

    def getQuantidade(self):
        return self.quantidade