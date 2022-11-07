
from controllers.user_controller import UserController
import streamlit as st
        

col1, col2, col3 = st.columns(3,gap= "small")
with col2:
    st.image(
        image = "assets/github_icon.png",
        width = 100,      
    )
    
            
    email_usuario = st.text_input( # Input para email do usuario
        label = "Email",
         
    )
        
    senha_usuario = st.text_input( # Input para senha do usuario
        label = "Senha",
        type = "password",
        
    )        
    if st.button("Entrar"):
        user_controller = UserController()
        cond = False # Condição inicial
        if user_controller.checkLogin(email_usuario, senha_usuario): # verifica se o email e a senha dados constam no banco de dados
            st.success("Login realizado com sucesso!") # Caso verdadeiro, ou seja, consta no banco de dados, troca o valor da condição para True
            cond = True
            st.session_state["zoro"] = cond
        else:
            st.error("Login ou senha incorretos!") # Caso contrário, valor da condição permanece False
        
      


    
    


