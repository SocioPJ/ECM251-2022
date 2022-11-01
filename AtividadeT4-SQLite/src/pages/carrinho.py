import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho
from controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController
import time


def layout_carrinho(product_carrinho):
    st.write('__________________________________________________________')
    print(len(product_carrinho.getList()))
    for item in product_carrinho.getList():
        with st.container():
            colA, colB, colC, colD, colE = st.columns(5,gap = 'small')
            with colA:
                st.image(image = item.url, width = 100)
            with colB:
                st.subheader("Adicionado")
                st.write(item.name)
                
            with colC:
                st.subheader("Qtd.")
                st.write(product_carrinho.verQuantidade())
            with colD:
                st.subheader("Preço")
                st.write(item.price)
            with colE:
                st.metric(
                    label = "Valor",
                    value = format(item.price*product_carrinho.verQuantidade(), '.2f'),
                        )
        
    
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
            # try:
            #     for itens in st.session_state['carrinho']:
            #         total = 0
            #         total += itens.price
            # except:
            #     print("erro ao totalizar compra")
            # st.write('Frete: R$ 10,00')
            # st.metric(
            #         label = "Valor",
            #         value = format(total+10, '.2f'),
            #             )
        
        # st.write('Frete: R$ 10,00')
        # for product in st.session_state["carrinho"].getList():
        #     print(product.price*product.verQuantidade())
                   
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
                    st.session_state["carrinho"].removeProduct()
            
            


       
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass