from operator import truediv
from turtle import onclick
import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from pages.login import verificar_nome
def carrinho_click():
    click = True
    st.session_state["botao_carrinho"] = click

def layout_produtos(product):
    colA, colB , colC = st.columns(3)
    with colA:
        st.subheader(product.name)
        st.image(image = product.url, width = 250)
     
    with colB: 
        st.text('      Novo | 256823 Vendidos')
        # numero = st.number_input("Quantidade", min_value=1, max_value=10, value=1)
        # botao = st.button("Adicionar ao carrinho")
    with colC:
        st.metric(label = "Preço", value = f'R$ {product.price}', delta = -0.5)
        st.number_input("Quantidade", min_value=1, max_value=10, value=1)
        st.text('🚛 Chegará grátis amanhã!!')
        st.button(
            label = "Adicionar ao carrinho",
            on_click = carrinho_click,
        )
        if st.session_state.botao_carrinho == True:
            st.write("Adicionado ao carrinho!")
            st.session_state.botao_carrinho = False
        
        

print(ProductController().getProducts())   
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
            st.title("Produtos")
            
        st.subheader("Produtos selecionados especialmente para você!")
        st.text("|_________________________________________________________________________________|")   
            # Primeiro Produto:
        
        # for i in range(len(ProductController().getProducts())):
        #     layout_produtos(ProductController().getProducts()[i])
            
        layout_produtos(ProductController().getProducts()[0])
        st.write("__________________________________________________________")
        # layout_produtos(ProductController().getProducts()[1])
        # st.write('__________________________________________________________')
        # layout_produtos(ProductController().getProducts()[2])
        # for i in range(len(ProductController().getProducts())):
        #     st.title(ProductController().getProducts()[i].name)
        #     st.write(ProductController().getProducts()[i].price)
        #     st.image(
        #         image = ProductController().getProducts()[i].url,
        #         width = 200
        #         )
            
            
            
            
        # Coluna 2
        with col2:
            st.text_input('')
        # Coluna 3
        with col3:
            st.write("")
            st.write("")
            
            st.image(
                image = "assets/search_icon_flat.png",
                width = 25,
                )      
        with col4:
            st.subheader(f"Bem vindo, joao!")
            st.subheader(
                label = st.session_state["zoro"],
                )
        

    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.text(" ")    
        st.write("Por favor, faça o login para acessar a loja!")
        
except:
    print("Erro")
