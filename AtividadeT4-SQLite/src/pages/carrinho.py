import streamlit as st
from controllers.user_controller import UserController
from models.cart import Cart
from controllers.product_controller import ProductController
from controllers.cart_controller import CartController
import time

controller_cart = CartController()
def layout_carrinho():
    total = 0
    try:
        st.write('__________________________________________________________')
        for item in controller_cart.pegar_todos_itens():
            with st.container():
                
                colA, colB, colC, colD, colE = st.columns(5,gap = 'small')
                with colA:
                    st.image(image = item.product_url, width = 100)
                    pass
                with colB:
                    st.subheader("Adicionado")
                    st.write(item.product_name)
                    
                with colC:
                    st.subheader("Qtd.")
                    st.write(item.quantity)
                with colD:
                    pass
                    st.subheader("Preço")
                    st.write(item.product_price)
                with colE:
                    pass
                    st.metric(
                        
                        label = "Valor",
                        value = format(item.product_price*item.quantity, '.2f'),
                            )
                    total += item.product_price*item.quantity
    except:
        print("Erro layout carrinho")
        
    
try:
    if st.session_state.zoro:
        st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
        st.title("Carrinho")
        layout_carrinho()
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
            total = 0
            for itens in controller_cart.pegar_todos_itens():
                total += controller_cart.pegar_quantidade_item_carrinho(itens.product_id)*controller_cart.pegar_preco_item_carrinho(itens.product_id)
            total = format(total, '.2f')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.text("Total")
            st.text(f'R${total}')
            
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
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
                if percent_complete == 99:
                    st.balloons()
                    st.success("Compra finalizada com sucesso!")
                    for itens in controller_cart.pegar_todos_itens():
                        controller_cart.deletar_item_carrinho(itens.product_id)
            
            


       
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