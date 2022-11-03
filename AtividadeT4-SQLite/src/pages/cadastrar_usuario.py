import streamlit as st
from controllers.user_controller import UserController
from models.user import User
contagem_blocos_respondidos=0
controller_usuario = UserController()


st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
st.title("Cadastrar Usuários")
tab1, tab2 = st.tabs(["Cadastrar", "Visualizar"])
with tab1:
    try:
        with st.container():
            with st.form("entry_form", clear_on_submit=True):
                    # id_input = st.number_input(
                    #     label = "Digite o id do novo usuario",
                    #     min_value = 0,
                    #     key = 'id_input'  
                    # )
                    # if id_input != "":
                    #     contagem_blocos_respondidos+=1
                    name_input = st.text_input(
                        label= "Digite o nome do novo usuario",
                        key = 'name_input'
                        )
                    if name_input != "":
                        contagem_blocos_respondidos+=1
                    email_input = st.text_input(
                        label = "Digite o email do novo usuario",
                        key = 'email_input'
                        )
                    if email_input != "":
                        contagem_blocos_respondidos+=1
                    password_input = st.text_input(
                        label = "Digite a senha do novo usuario",
                        key = 'password_input'
                        )
                    if password_input != "":
                        contagem_blocos_respondidos+=1
                    if st.form_submit_button("Cadastrar"):
                        if contagem_blocos_respondidos == 3:
                            controller_usuario.inserir_usuario(User(st.session_state["name_input"],st.session_state["email_input"],st.session_state["password_input"]))
                            st.write(f'name: {st.session_state["name_input"]}')
                            st.write(f'email: {st.session_state["email_input"]}')
                            st.write(f'password: {st.session_state["password_input"]}')       
                            st.success("Produto cadastrado com sucesso")           
                        else:
                            st.warning("Preencha todos os campos!")
    except:
        print('Erro cadastrar usuarios')
