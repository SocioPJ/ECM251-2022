from tkinter.tix import INTEGER
from token import STRING
import streamlit as st
from controllers.product_controller import ProductController
from models.product import Product


controller = ProductController()
i = 0
if st.session_state.zoro:
    st.title("Cadastrar Produtos")
    id_input = st.text_input(
        label = "Digite o id do novo produto"
    )
    
    if id_input != "":
        i+=1
    print(id_input)
    print(f'numero: {i}')
    
    name_input = st.text_input(
        label= "Digite o nome do novo produto"
        )
    
    if name_input != "":
        i+=1
   
    print(name_input)
    print(f'numero: {i}')
    
    price_input = st.text_input(
        label = "Digite o preço do novo produto"
        )
    if price_input != "":
        i+=1
    print(price_input)
    print(f'numero: {i}')
    
    url_input = st.text_input(
        label = "Digite o link da imagem do novo produto"
        )
    if url_input != "":
        i+=1
    print(url_input)
    print(f'numero: {i}')
    
    with st.container():
        colA, colB, colC, colD = st.columns(4,gap = 'small')
        with colD:
            if st.button("Cadastrar"):
                if i == 4:
                    #st.session_state.zoro = False
                    controller.inserir_item(Product(id_input,name_input,price_input,url_input))
                    st.success("Produto cadastrado com sucesso")
                else:
                    st.warning("Preencha todos os campos!")
                    #st.session_state.zoro = True
            
else:
    st.title("Bem vindo ao meu site!")
    st.text("__________________________________________________________")
    st.write("Por favor, faça o login para acessar a loja!")
