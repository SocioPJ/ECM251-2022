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
    