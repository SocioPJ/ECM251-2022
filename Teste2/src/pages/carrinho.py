import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho
from controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController
import time


def layout_carrinho(product_carrinho):
    st.write('__________________________________________________________')
    colA, colB, colC, colD, colE = st.columns(5,gap = 'small')
    with colA:
        st.image(image = product_carrinho.getList()[0].url, width = 100)
    with colB:
        st.subheader("Adicionado")
        st.write(product_carrinho.getList()[0].name)
    
    with colC:
        st.subheader("Qtd.")
        quantidade_carrinho = product_carrinho.verQuantidade()
        st.write(product_carrinho.verQuantidade())
    with colD:
        st.subheader("Preço")
        st.write(product_carrinho.getList()[0].price)
    with colE:
        st.write('Frete: R$ 10,00')
        st.metric(
            label = "Total",
            value = format(product_carrinho.getList()[0].price*product_carrinho.verQuantidade() + 10, '.2f'),
            )
        
    
try:
    if st.session_state.zoro:
        st.title("Carrinho")
        layout_carrinho(st.session_state["carrinho"])
        # st.write(st.session_state["carrinho"].getList()[0])
        # st.write(st.session_state["carrinho"].getList()[0][1])
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.selectbox(
            label = "Forma de pagamento",
            options = ["Cartão de crédito", "Boleto", "Pix"],
        )
        if st.button("Finalizar compra"):

            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.1)
                my_bar.progress(percent_complete + 1)
                if percent_complete == 99:
                    st.balloons()
                    st.success("Compra finalizada com sucesso!")
                    st.session_state["carrinho"].clear()
            
            


       
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass