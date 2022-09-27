import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from pages.login import verificar_nome

    
if "zoro" not in st.session_state:
    st.session_state.zoro = False
try:
    if st.session_state.zoro:
        col1 , col2, col3, col4= st.columns(4)
        def clicado():
            click = True
            st.session_state["kratos"] = click
        # Coluna 1
        with col1:
            st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
        st.subheader("Produtos selecionados especialmente para você!")
            # Primeiro Produto:
            
        for i in range(len(ProductController().getProducts())):
            st.title(ProductController().getProducts()[i].name)
            st.write(ProductController().getProducts()[i].price)
            st.image(
                image = ProductController().getProducts()[i].url,
                width = 200
                )
            
            
            
            
        # Coluna 2
        with col2:
            
            st.text_input(
                    label = "",
                    value = "Buscar produtos"
                )
        # Coluna 3
        with col3:
            st.write("")
            st.write("")
            
            st.image(
                image = "assets/search_icon_flat.png",
                width = 25,
                )      
        with col4:
            st.subheader("Bem vindo,")
            st.subheader(
                label = st.session_state["zoro"],
                )
        

    else:
        st.title("Bem vindo ao meu site!")
        st.write("Por favor, faça o login para acessar a loja!")
        st.image(
            image ="https://dacolonia.com.br/public/uploads/2021/03/a37fcd67071aaf3e2a4ec1428a0fc61d-product_photo.png",
        )
except:
    print("Erro")
