from cProfile import label
from re import A
from turtle import onclick, width
import streamlit as st
from controllers.user_controller import UserController

main, info, cadastro = st.tabs(["Home", "Info", "Cadastro"])
if UserController.verificar() == True:
    st.write("Ola Mundo!")
with main:
    col1 , col2, col3, col4= st.columns(4)
    def clicado():
        click = True
        st.session_state["kratos"] = click
    with col1:
        st.image(
            image = "assets/github_icon.png",
            width = 75,
        )
        st.button(
        label="Clicar aqui🍳",
        help="a!",
        on_click=clicado
    )
    with col2:
        st.text_input(
            label = "",
        )
        if "kratos" in st.session_state :
            casa , infor, home = st.tabs(["Home", "Info", "Cadastro"])
    with col3:
        st.image(
            image = "assets/search_icon_flat.png",
            width = 25,
        )
    
   
def fui_apertado():
    print("Ola Mundo!")

def somar_dois(v1,v2):
    resultado = v1+v2
    st.session_state["kratos"] = resultado



#######################################################################################################

with info:
    numero1 = st.number_input(
        label="Valor 1:",
        min_value= 0,
        max_value = 100
    )
    numero2 = st.number_input(
        label="Valor 2:",
        min_value= 0,
        max_value = 100
    )

    st.button(
        label="Clicar aqui🍳",
        help="Clique para ver comida!",
        on_click=somar_dois,
        kwargs={"v1":numero1, "v2":numero2}
    )

    if "kratos" in st.session_state:
        st.metric(
                label="Resultado:",
                value=st.session_state["kratos"]
        )
    else:
        st.write("Ainda nenhum calculo foi realizado!")

    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)

with cadastro:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://assets.reedpopcdn.com/Scarlet_Violet_Key_Art.jpg/BROK/thumbnail/1200x1200/quality/100/Scarlet_Violet_Key_Art.jpg",
            caption="Imagem polêmica de pokemon"
        )


    with col2:
        st.image(
            image="assets/github_icon.png",
            caption="Lechonk"
        )

    with col3:
        st.image(
            image="assets/github_icon.png",
            caption="Professor Oak"
        )

