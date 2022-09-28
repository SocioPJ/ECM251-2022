import streamlit as st
from controllers.user_controller import UserController
from models.carrinho import Carrinho
from controllers.product_controller import ProductController
from controllers.carrinho_controller import CarrinhoController

def layout_carrinho(product):
    st.write('__________________________________________________________')
    colA, colB, colC, colD, colE = st.columns(5,gap = 'small')
    with colA:
        st.image(image = product.getList()[0].url, width = 100)
    with colB:
        st.subheader("Adicionado")
        st.write(product.getList()[0].name)
    
    with colC:
        st.subheader("Qtd.")
        st.write(product.quantidade)
    with colD:
        st.subheader("Preço")
        st.write(product.getList()[0].price)
    with colE:
        st.write('Frete: R$ 10,00')
        st.metric(
            label = "Total",
            value = format(product.getList()[0].price*product.quantidade + 10, '.2f'),
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
            st.write('Compra realizada com sucesso!')
            st.write('Obrigado por comprar conosco!')
            


       
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.write("Por favor, faça o login para acessar a loja!")
except:
    pass