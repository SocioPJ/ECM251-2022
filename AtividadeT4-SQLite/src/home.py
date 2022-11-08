import random
from models.cart import Cart
import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
from controllers.cart_controller import CartController
from dao.cart_dao import CartDAO
controller = ProductController()
controller_carrinho = CartController()
condicao_produto = ['Suja', 'Nova', 'Usada', 'Rasgada', 'Mofada', 'Queimada']
if "zoro" not in st.session_state:
    st.session_state.zoro = False
def layout_produtos(): # Layout para exposição dos produtos da loja.
    try:
        with st.container():
            for itens in controller.pegar_todos_itens():
                colA, colB , colC = st.columns(3)
                with colA:
                    st.subheader(itens.name)
                    st.image(image = itens.url, width = 250)
                    
                with colB: 
                    st.text(f'      {random.choice(condicao_produto)} | {random.randrange(0,1000)} Vendidos') # Gera valores aleatorio com a biblioteca random do Python
                with colC:
                    try:
                        st.metric(label = "Preço", value = f'R$ {itens.price}')
                        quantidade = st.number_input("Quantidade", min_value=1, max_value=10, value=1, key = itens.id)
                        if st.button("Adicionar ao carrinho", key = itens.name ):
                            products_id_in_cart = []
                            for product in controller_carrinho.pegar_todos_itens():
                                products_id_in_cart.append(product.product_id) # Adiciona todos ids em um array
                            if itens.id not in products_id_in_cart: # Verifica se o id do produto ja esta no banco de dados. Caso não esteja, produto adicionado ao carrinho, caso contrário a quantidade é somada no carrinho
                                controller_carrinho.inserir_item(Cart(itens.id,itens.name,itens.price,itens.url,quantidade))
                                st.success('Produto adicionado ao carrinho!')
                            else:
                                quantidade_anterior = controller_carrinho.pegar_quantidade_item_carrinho(itens.id)
                                quantidade_nova = quantidade + quantidade_anterior
                                controller_carrinho.atualizar_quantidade_item_carrinho(itens.id,quantidade_nova)
                                st.success('Produto adicionado ao carrinho!')
                    except:
                        print('Erro ao adicionar ao carrinho')
                st.write("")
                st.write('')
    except:
        print("Erro layout produtos")

try:
    if st.session_state.zoro:
        col1 , col2, col3, col4= st.columns(4)
       
        # Coluna 1
        with col1:
            
            st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
            st.title("AnimeHub")
            
        st.subheader("Camisetas selecionados especialmente para você!")
        st.caption("__________________________________________________________________________________________") 
        
        layout_produtos()
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
    raise Exception("erro na pagina home")
