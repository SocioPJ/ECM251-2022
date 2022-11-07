import streamlit as st
from controllers.user_controller import UserController
from models.user import User
contagem_blocos_respondidos=0
controller_usuario = UserController()
def layout_visualizar_usuarios(): # Layout criado para visualizar usuarios existentes na aba "Visualizar"
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

st.image( # Inicio da Página
            image = "assets/github_icon.png",
            width = 75,
            )
st.title("Usuários")
tab1, tab2,tab3 = st.tabs(["Cadastrar", "Visualizar", 'Editar'])
with tab1: # Primeira aba para Cadastrar os usuarios
    try:
        with st.container():
            with st.form("entry_form", clear_on_submit=True): # Dentro de um form para quando o botão no final for acionado, todos os blocos de inputs resetem.
                    name_input = st.text_input( # Input para nome do usuario
                        label= "Digite o nome do novo usuario",
                        key = 'name_input'
                        )
                    if name_input != "":
                        contagem_blocos_respondidos+=1 # Criei essa contagem para verificar se todos os campos foram preenchidos, caso não tenha sido todos preenchidos, não sera criado o novo usuário.
                    email_input = st.text_input( # Input para email do usuário
                        label = "Digite o email do novo usuario",
                        key = 'email_input'
                        )
                    if email_input != "":
                        contagem_blocos_respondidos+=1
                    password_input = st.text_input( # Input senha do usuário
                        label = "Digite a senha do novo usuario",
                        key = 'password_input'
                        )
                    if password_input != "":
                        contagem_blocos_respondidos+=1
                    if st.form_submit_button("Cadastrar"):
                        if contagem_blocos_respondidos == 3: # Caso os 3 blocos de input forem preenchidos, a contagem vai para 3 e permite que o usuario seja criado
                            for i in range(len(controller_usuario.pegar_todos_usuarios())): # Escaneio todos os usuarios no banco de dados
                                emails.append(controller_usuario.pegar_todos_usuarios()[i].email) # Adiciono todos os email dentro de um array.
                            if email_input not in emails: # Verifico se o email dado é repetido ou não. Se não for, o usuario será criado com email inexistente. Caso contrário, email já existe no banco de dados, então não é criado o usuario.
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

with tab2: # Segunda aba para visualizar todos usuarios ja existentes.
    layout_visualizar_usuarios()

with tab3: # Terceira aba para editar nome ou senha de algum usuario
    email_usuarios=[]
    for i in range(len(controller_usuario.pegar_todos_usuarios())): # Adiciono todos emails em um array
        email_usuarios.append(controller_usuario.pegar_todos_usuarios()[i].email)
    # st.write(nome_usuarios)
    try:
        with st.container():
            option =  st.selectbox( # Crio uma selectbox com todos emails 
                "Email dos usuários: ",
                (email_usuarios)
            )
            usuario = controller_usuario.buscar_todos_usuarios_email(option) # Busco o usuario que possui o email selecionado
            usuario = usuario[0]
            st.write(usuario)
            with st.form('entry changes',True): # Form criado para alterar nome e/ou senha do usuario selecionado.
                colA, colB = st.columns(2)
                with colA:
                    new_name_input=st.text_input( # Input para novo nome.
                        label = 'Digite um novo nome'
                    )
                with colB:
                    new_password_input = st.text_input( # Input para nova senha.
                        label = 'Digite uma nova senha'
                    )
                if st.form_submit_button('Atualizar'):
                    try:
                        if new_name_input != "": # Verifica se text input esta vazio
                            if new_name_input != usuario.name: # Verifica se o novo nome é igual ao anterior
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
        
    