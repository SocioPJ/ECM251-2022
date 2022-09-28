import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho

def layout_produtos():
    st.title("Produtos")
    
    
try:
    if st.session_state.zoro:
        st.title("Carrinho")
        
        
        
        
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass