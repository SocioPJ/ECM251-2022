
from models.carrinho import Carrinho
import streamlit as st
from controllers.user_controller import UserController
from controllers.product_controller import ProductController
controller = ProductController()
if "carrinho" not in st.session_state:
    st.session_state["carrinho"] = Carrinho()
if "zoro" not in st.session_state:
    st.session_state.zoro = False
    # carrinho = Carrinho()

    
if "quantidade" not in st.session_state:
    st.session_state["quantidade"] = 0
if "quantidade2" not in st.session_state:
    st.session_state["quantidade2"] = 0
if "quantidade3" not in st.session_state:
    st.session_state["quantidade3"] = 0


def layout_produtos():
    for itens in controller.pegar_todos_itens():
        with st.container():
            colA, colB , colC = st.columns(3)
            with colA:
                st.subheader(itens.name)
                st.image(image = itens.url, width = 250)
            
            with colB: 
                st.text('      Novo | 256823 Vendidos')
            with colC:
                st.metric(label = "Preço", value = f'R$ {itens.price}', delta = -0.5)
                quantidade = st.number_input("Quantidade", min_value=1, max_value=10, value=1, key = itens.name)
                st.text('🚛 Chegará grátis amanhã!!')
                if st.button("Adicionar ao carrinho"):
                    st.session_state["carrinho"].addProduct(itens)
                    st.session_state["quantidade"] = quantidade
                
# print(ProductController().getProducts())   

try:
    if st.session_state.zoro:
        col1 , col2, col3, col4= st.columns(4)
       
        # Coluna 1
        with col1:
            
            st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
            st.title("Produtos")
            
        st.subheader("Produtos selecionados especialmente para você!")
        st.text("__________________________________________________________________________________________")   
            # Primeiro Produto:
        
        # for i in range(len(ProductController().getProducts())):
        #     layout_produtos(ProductController().getProducts()[i])
            
    
        # st.write("__________________________________________________________")
        #  layout_produtos(ProductController().getProducts()[1])
        # # st.write('__________________________________________________________')
        # layout_produtos(ProductController().getProducts()[2])
        # for i in range(len(ProductController().getProducts())):
        #     st.title(ProductController().getProducts()[i].name)
        #     st.write(ProductController().getProducts()[i].price)
        #     st.image(
        #         image = ProductController().getProducts()[i].url,
        #         width = 200
        #         )
        
        
        # produto1 = ProductController().getProducts()[0]
        
        produto1 = controller.pegar_item(0)
        # produto2 = ProductController().getProducts()[1]
        # produto3 = ProductController().getProducts()[2]
        # colA, colB , colC = st.columns(3)
        # with colA:
            
        #     st.subheader(produto1.name)
        #     st.image(image = produto1.url, width = 200)
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('__________________________________________________________')
        #     st.subheader(produto2.name)
        #     st.image(image = produto2.url, width = 200)
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('__________________________________________________________')
        #     st.subheader(produto3.name)
        #     st.image(image = produto3.url, width = 200)
            
     
        # with colB:
        #     st.text('')
        #     st.text('      Novo | 256823 Vendidos')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.text('      Novo | 5 Vendidos')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        
        #     st.text('    Novo | 1832450192 Vendidos')
        # with colC:
        #     st.write('')
        #     st.metric(label = "Preço", value = f'R$ {produto1.price}', delta = f'R$ 10')
        #     quantidade = st.number_input("Quantidade", min_value=1, max_value=10, value=1)
        #     st.text('🚛 Chegará grátis amanhã!!')
        #     if st.button("Adicionar ao carrinho"):
        #         st.session_state["carrinho"].addProduct(produto1)
        #         st.session_state["quantidade"] = quantidade              
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.metric(label = "Preço", value = f'R$ {produto2.price}', delta = f'R$ 300')
        #     quantidade2 = st.number_input("Quantidade ", min_value=1, max_value=10, value=1)
        #     st.text('🚛 Chegará grátis amanhã!!')
        #     if st.button("Adicionar ao carrinho "):
        #         st.session_state["carrinho"].addProduct(produto2)
        #         st.session_state["quantidade2"] = quantidade2
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.write('')
        #     st.metric(label = "Preço", value = f'R$ {produto3.price}', delta = f'R$ {produto3.price}')
        #     quantidade3 = st.number_input("Quantidade  ", min_value=1, max_value=10, value=1)
        #     st.text('🚛 Chegará grátis amanhã!!')
        #     if st.button("Adicionar ao carrinho  "):
        #         st.session_state["carrinho"].addProduct(produto3)
        #         st.session_state["quantidade3"] = quantidade3
                
            
            
            
        # # Coluna 2
        # with col2:
        #     st.text_input('')
        # # Coluna 3
        # with col3:
        #     st.write("")
        #     st.write("")

        #     st.image(
        #         image = "assets/search_icon_flat.png",
        #         width = 25,
        #         )      
        # with col4:
        #     st.subheader(f"Bem vindo, joao")
        #     st.subheader(
        #         label = st.session_state["zoro"],
        #         )
        

    else:
        st.title("Bem vindo ao meu site!")
        st.text("__________________________________________________________")
        st.text(" ")    
        st.write("Por favor, faça o login para acessar a loja!")
        
except:
    print("Erro")
