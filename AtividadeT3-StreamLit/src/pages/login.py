import streamlit as st
col1, col2, col3 = st.columns(3,gap= "small")
with col2:
    st.image(
        image = "assets/github_icon.png",
        width = 100,      
    )
    st.text_input(
        label = "Nome de usuário",       
    )
    st.text_input(
        label = "Senha",
    )
    st.button(
        
    )
    


