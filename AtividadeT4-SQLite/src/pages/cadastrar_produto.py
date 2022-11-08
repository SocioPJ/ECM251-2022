import streamlit as st
from controllers.product_controller import ProductController
from models.product import Product
controller = ProductController()
def layout_visualizar_produtos(): # Layout para visualizar produtos na segunda aba "Visualizar"
    try:
        with st.container():
            for itens in controller.pegar_todos_itens(): # Passo por cada item no banco de dados e cria um container para cada um.
                colA, colB , colC, colD = st.columns(4)
                with colA:
                    
                    st.image(image = itens.url, width = 115)
                    
                with colB: 
                    st.caption(itens.name)
                    st.caption(f'Id: {itens.id}')
                with colC:
                    st.caption(f'Preço: {itens.price}')
                with colD:
                    if st.button("Remover", key = itens.name):
                        controller.deletar_item(itens.id)
                        
                st.write('')
                st.write('')
    except:
        print("Erro layout visualizar produtos")
    
controller = ProductController()
i = 0

# QUANDO ESTÁ LOGADO
if st.session_state.zoro:
    st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
    st.title("Produtos")
    tab1, tab2 = st.tabs(["Cadastrar", "Visualizar"])
    with tab1: # Primeira aba para cadastrar produtos
        try:
            with st.container():
                with st.form("entry_form", clear_on_submit=True):
                    id_input = st.number_input( # Input id novo produto.
                        label = "Digite o id do novo produto",
                        min_value = 0,
                        key = 'id_input'  
                    )
                    if id_input != "":
                        i+=1
                    name_input = st.text_input( # Input nome produto.
                        label= "Digite o nome do novo produto",
                        key = 'name_input'
                        )
                    if name_input != "":
                        i+=1
                    price_input = st.number_input( # Input preço produto.
                        label = "Digite o preço do novo produto",
                        min_value= 0.01,
                        max_value= 1000000.00,
                        step= 0.01,
                        format='%.2f',
                        key = 'price_input'
                        )
                    if price_input != "":
                        i+=1
                    url_input = st.text_input( # Input link imagem do produto.
                        label = "Digite o link da imagem do novo produto",
                        key = 'url_input'
                        )
                    if url_input != "":
                        i+=1
                    if st.form_submit_button("Cadastrar"):
                        ids = []
                        if i == 4: # Verifica se todos os campos estão preenchidos
                            for i in range(len(controller.pegar_todos_itens())): # Adiciono todos ids em um array
                                ids.append(controller.pegar_todos_itens()[i].id)
                            if id_input not in ids: # Verifica se o id selecionado ja é atribuido a outro produto
                                controller.inserir_item(Product(st.session_state["id_input"],st.session_state["name_input"],st.session_state["price_input"],st.session_state["url_input"])) # Insere o produto ao banco de dados
                                st.write(f'id: {st.session_state["id_input"]}')
                                st.write(f'name: {st.session_state["name_input"]}')
                                st.write(f'price: {st.session_state["price_input"]}')
                                st.write(f'url: {st.session_state["url_input"]}')       
                                st.success("Produto cadastrado com sucesso")
                            else:
                                st.error("ID inválido. Tente outro")           
                        else:
                            st.warning("Preencha todos os campos!")
        except:
            print('Erro cadastrar produtos')
    with tab2: # Segunda aba "Visualizar"
        with st.container():
            layout_visualizar_produtos() # Visualiza todos produtos que estao no banco de dados
            
            
            
                
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
    

