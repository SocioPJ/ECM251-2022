
from controllers.user_controller import UserController
import streamlit as st
        

col1, col2, col3 = st.columns(3,gap= "small")
with col2:
    st.image(
        image = "assets/github_icon.png",
        width = 100,      
    )
    
            
    email_usuario = st.text_input(
        label = "Email",
         
    )
        
    senha_usuario = st.text_input(
        label = "Senha",
        type = "password",
        
    )        
    if st.button("Entrar"):
        user_controller = UserController()
        cond = False
        if user_controller.checkLogin(email_usuario, senha_usuario):
            st.success("Login realizado com sucesso!")
            cond = True
            st.session_state["zoro"] = cond
        else:
            st.error("Login ou senha incorretos!")
        
      


    
    


