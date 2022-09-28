import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho
from controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController

carrinho = Carrinho()

try:
    if st.session_state.zoro:
        st.title("Carrinho")
        if carrinho.getList() == []:
            st.write("Carrinho vazio!")

        else:
            if st.session_state.botao_carrinho == True:
                carrinho.addProduct(ProductController().getProducts()[0])
                st.session_state.botao_carrinho = False
                for i in range(len(carrinho.getList())):
                    st.title(carrinho.getList()[i].name)
                    st.write(carrinho.getList()[i].price)
                    st.image(
                        image = carrinho.getList()[i].url,
                        width = 250
                    )
        
        
        
        
        
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass