import streamlit as st
from controllers.user_controller import UserController
from models.user import User
contagem_blocos_respondidos=0
controller_usuario = UserController()
def layout_visualizar_usuarios():
    try:
        with st.container():
            for users in controller_usuario.pegar_todos_usuarios():
                colA, colB , colC = st.columns(3)
                with colA:
                    st.write('')
                    st.image (
                        image = "assets/user_icon.png",
                        width = 75
                        )
                    
                with colB: 
                    st.caption(f'Nome : {users.name}')
                    st.caption(f'Email : {users.email}')
                    st.caption(f'Senha: {users.password}')
                with colC:
                    if st.button("Remover", key = users.email):
                        controller_usuario.deletar_usuario(users.email)
                     
                        

                st.caption('-----------------------------------------------')
    except:
        print("Erro layout visualizar usuarios")
emails = []
st.image(
            image = "assets/github_icon.png",
            width = 75,
            )
st.title("Usuários")
tab1, tab2,tab3 = st.tabs(["Cadastrar", "Visualizar", 'Editar'])
with tab1:
    try:
        with st.container():
            with st.form("entry_form", clear_on_submit=True):
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
                            for i in range(len(controller_usuario.pegar_todos_usuarios())):
                                emails.append(controller_usuario.pegar_todos_usuarios()[i].email)
                            if email_input not in emails:
                                controller_usuario.inserir_usuario(User(st.session_state["name_input"],st.session_state["email_input"],st.session_state["password_input"]))
                                st.write(f'name: {st.session_state["name_input"]}')
                                st.write(f'email: {st.session_state["email_input"]}')
                                st.write(f'password: {st.session_state["password_input"]}')       
                                st.success("Usuario cadastrado com sucesso!")
                            else:
                                st.error('Email ja cadastrado. Tente novamente')          
                        else:
                            st.warning("Preencha todos os campos!")
    except:
        print('Erro cadastrar usuarios')

with tab2:
    layout_visualizar_usuarios()

with tab3:
    email_usuarios=[]
    for i in range(len(controller_usuario.pegar_todos_usuarios())):
        email_usuarios.append(controller_usuario.pegar_todos_usuarios()[i].email)
    # st.write(nome_usuarios)
    try:
        with st.container():
            option =  st.selectbox(
                "Email dos usuários: ",
                (email_usuarios)
            )
            usuario = controller_usuario.buscar_todos_usuarios_email(option)
            st.write(usuario[0])
            st.write(f'Nome usuario: {usuario[0].name}')
            st.write(f'Email do usuário: {usuario[0].email}')
            st.write(f'Senha do usuário: {usuario[0].password}')
    except:
        print('erro selecionar usuario em Editar')            
        
    