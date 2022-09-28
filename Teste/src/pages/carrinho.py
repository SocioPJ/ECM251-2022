import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho
from controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController

carrinho = Carrinho()
def layout_carrinho(product):
    st.write('__________________________________________________________')
    colA, colB, colC = st.columns(3)
    with colA:
        st.subheader(product.name)
        st.image(image = product.url, width = 250)
    
try:
    if st.session_state.zoro:
        st.title("Carrinho")

       
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass