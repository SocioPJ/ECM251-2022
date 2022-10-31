
import streamlit as st
from controllers.product_controller import ProductController
from models.product import Product

st.set_page_config(layout='centered')
    
j = 0
j+=j
controller = ProductController()
i = 0
if st.session_state.zoro:
    st.header("Cadastrar Produtos")
    with st.container():
        with st.form("entry_form", clear_on_submit=True):
            id_input = st.number_input(
                label = "Digite o id do novo produto",
                min_value = 0,
                key = 'id_input'
                
            )
            
            if id_input != "":
                i+=1
            
            
            name_input = st.text_input(
                label= "Digite o nome do novo produto",
                key = 'name_input'
                )
            
            if name_input != "":
                i+=1
        
            
            
            price_input = st.number_input(
                label = "Digite o preço do novo produto",
                min_value= 0.01,
                max_value= 1000000.00,
                step= 0.01,
                format='%.2f',
                key = 'price_input'
                )
            if price_input != "":
                i+=1
            
            
            url_input = st.text_input(
                label = "Digite o link da imagem do novo produto",
                key = 'url_input'
                )
            if url_input != "":
                i+=1
            
            
            
            
            if st.form_submit_button("Cadastrar"):
                if i == 4:
                    controller.inserir_item(Product(st.session_state["id_input"],st.session_state["name_input"],st.session_state["price_input"],st.session_state["url_input"]))
                    st.experimental_rerun()
                    print(st.session_state['id_input'])
                    st.write(f'id: {st.session_state["id_input"]}')
                    st.write(f'name: {st.session_state["name_input"]}')
                    st.write(f'price: {st.session_state["price_input"]}')
                    st.write(f'url: {st.session_state["url_input"]}')       
                    st.success("Produto cadastrado com sucesso")
                    
                
                # Problema : Nao to conseguindo adicionar dois itens de uma vez sem q eu tenha q mudar alguma coisa no codigo
                            
                else:
                    st.warning("Preencha todos os campos!")
                #st.session_state.zoro = True
        
                    
            
else:
    st.title("Bem vindo ao meu site!")
    st.text("__________________________________________________________")
    st.write("Por favor, faça o login para acessar a loja!")
