import streamlit as st
from controllers.user_controller import UserController
from models.cart import Carrinho
from controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController
import time


def layout_carrinho(product_carrinho):
    try:
        st.write('__________________________________________________________')
        for item in product_carrinho.getList():
            with st.container():
                colA, colB, colC, colD, colE = st.columns(5,gap = 'small')
                with colA:
                    st.image(image = item.url, width = 100)
                    pass
                with colB:
                    st.subheader("Adicionado")
                    st.write(item.name)
                    
                with colC:
                    st.subheader("Qtd.")
                    st.write(product_carrinho.verQuantidade())
                with colD:
                    pass
                    st.subheader("Preço")
                    st.write(item.price)
                with colE:
                    pass
                    st.metric(
                        label = "Valor",
                        value = format(item.price*product_carrinho.verQuantidade(), '.2f'),
                            )
    except:
        print("Erro layout carrinho")
        
    
try:
    if st.session_state.zoro:
        st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
        st.title("Carrinho")
        layout_carrinho(st.session_state["carrinho"])
        colA ,colB, colC, colD, colE = st.columns(5)
        with colA:
            pass
        with colB:
            pass
        with colC:
            pass
        with colD:
            pass
        with colE:
            pass
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
                    st.session_state["carrinho"].remover_todos_produtos()
            
            


       
# =================================================================================#       
                    
# ANTES DE LOGAR:           
    else:
        colA, colB, colC = st.columns(3)
        with colA:
            pass
            
        with colB:
            st.image(
                image = "assets/github_icon.png",
                width = 100,
            )
        with colC:
            pass
        st.write('')
        st.write('')
        st.write('')
        st.info('Faça login para acessar essa página')
except:
    pass