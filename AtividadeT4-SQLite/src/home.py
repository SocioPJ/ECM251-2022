
from models.carrinho import Carrinho
import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
controller = ProductController()
if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = Carrinho()
if "zoro" not in st.session_state:
    st.session_state.zoro = False
def layout_produtos():
    try:
        with st.container():
            for itens in controller.pegar_todos_itens():
                colA, colB , colC = st.columns(3)
                with colA:
                    st.subheader(itens.name)
                    st.image(image = itens.url, width = 250)
                    
                with colB: 
                    st.text('      Novo | 256823 Vendidos')
                with colC:
                    st.metric(label = "Preço", value = f'R$ {itens.price}', delta = -0.5)
                    quantidade = st.number_input("Quantidade", min_value=1, max_value=10, value=1, key = itens.id)
                    st.text('🚛 Chegará grátis amanhã!!')
                    if st.button("Adicionar ao carrinho", key = itens.name ):
                        st.session_state["carrinho"].addProduct(itens)
                        st.session_state["quantidade"] = quantidade
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
            
        st.subheader("Produtos selecionados especialmente para você!")
        st.text("__________________________________________________________________________________________") 
        
        layout_produtos()
    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.text(" ")    
        st.write("Por favor, faça o login para acessar a loja!")
        
except:
    raise Exception("erro na pagina home")
