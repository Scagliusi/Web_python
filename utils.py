import streamlit as st

def inserir_fundo(fundo):

    img_pagina = f"""
    <style>
        .stApp {{
            background-image:url({fundo});
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        .stAppHeader{{
            background-color: rgba(0,0,0,0);
        }}
    </style>
    """
    st.markdown(img_pagina, unsafe_allow_html=True)

#RESOLVER ISSO
def css_login():
    css = """ 
    <style>
        /* Estilizando os rótulos (label) do texto acima dos campos */
        div[data-testid="stTextInput"] label {
            color: #000000 !important; /* Cor preta */
            font-weight: bold !important; /* Negrito */
            font-size: 20px !important; /* Tamanho maior */
        }

        /* Estilizando o campo de entrada (input) */
        div[data-testid="stTextInput"] input {
            color: #000000 !important; /* Cor do texto no input */
            font-size: 18px !important; /* Tamanho do texto no input */
            font-weight: normal !important; /* Peso da fonte normal */
        }

        /* Estilo do input ao passar o mouse */
        div[data-testid="stTextInput"] input:hover {
            background-color: #ADD8E6 !important; /* Fundo azul claro */
        }

        /* Estilo do input ao estar em foco */
        div[data-testid="stTextInput"] input:focus {
            border-color: #007bff !important; /* Azul da borda */
        }
    </style>
    """
    return css

