import streamlit as st
from controllers.product_controller import ProductController
from models.product import Product
controller = ProductController()
def layout_visualizar_produtos():
    try:
        with st.container():
            for itens in controller.pegar_todos_itens():
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
                        # st.experimental_rerun
                        
                st.write('')
                st.write('')
    except:
        print("Erro layout visualizar produtos")
    
controller = ProductController()
i = 0
if st.session_state.zoro:
    st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
    st.title("Produtos")
    tab1, tab2 = st.tabs(["Cadastrar", "Visualizar"])
    with tab1:
        try:
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
                            # st.experimental_rerun()
                            print(st.session_state['id_input'])
                            st.write(f'id: {st.session_state["id_input"]}')
                            st.write(f'name: {st.session_state["name_input"]}')
                            st.write(f'price: {st.session_state["price_input"]}')
                            st.write(f'url: {st.session_state["url_input"]}')       
                            st.success("Produto cadastrado com sucesso")           
                        else:
                            st.warning("Preencha todos os campos!")
        except:
            print('Erro cadastrar produtos')
    with tab2:
        with st.container():
            
            layout_visualizar_produtos()
            
            
                
        
                    
            
else:
    st.title("Bem vindo ao meu site!")
    st.text("__________________________________________________________")
    st.write("Por favor, faça o login para acessar a loja!")

