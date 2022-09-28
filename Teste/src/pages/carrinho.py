import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho
from controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController

def layout_carrinho(product):
    st.write('__________________________________________________________')
    colA, colB, colC = st.columns(3)
    with colA:
        st.subheader(product.getList()[0].name)
        st.image(image = product.getList()[0].url, width = 250)

    
try:
    if st.session_state.zoro:
        st.title("Carrinho")
        layout_carrinho(st.session_state["carrinho"])
        # st.write(st.session_state["carrinho"].getList()[0])
        # st.write(st.session_state["carrinho"].getList()[0][1])



       
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass