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
            usuario = usuario[0]
            st.write(usuario)
            # st.info(f'Nome usuario: {usuario[0].name}')
            # st.info(f'Email do usuário: {usuario[0].email}')
            # st.info(f'Senha do usuário: {usuario[0].password}')
            with st.form('entry changes',True):
                colA, colB = st.columns(2)
                with colA:
                    new_name_input=st.text_input(
                        label = 'Digite um novo nome'
                    )
                with colB:
                    new_password_input = st.text_input(
                        label = 'Digite uma nova senha'
                    )
                if st.form_submit_button('Atualizar'):
                    try:
                        if new_name_input != "": # Verifica se text input esta vazio
                            if new_name_input != usuario.name: # verifica se o novo nome é igual ao anterior
                                usuario.name = new_name_input
                                st.success('Nome alterado com sucesso')
                            else:
                                st.error('Nome usuario igual')
                        else:
                            new_name_input = usuario.name # Se a caixa de entrada estiver vazia, o novo nome sera igual ao anterior, se não houvesse essa condição, o nome seria vazio no banco de dados.
                        if new_password_input != "": # Mesma coisa com a senha
                            if new_password_input != usuario.password or new_password_input != "":
                                usuario.password = new_password_input
                                st.success('Senha alterada com sucesso')
                            else:
                                print("Senha igual a anterior")
                        else:
                            new_password_input = usuario.password
                        controller_usuario.atualizar_usuario(usuario)
                    except:
                        print("Erro atualizar usuário")
                    
                
    except:
        print('erro selecionar usuario em Editar')            
        
    