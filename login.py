import streamlit as st
from datetime import datetime, timedelta
from views import membro_entrou
from utils import inserir_fundo,css_login
from db_sqlserver import *
from Usuario import Usuario
 

fundo_login = None
#"https://m.media-amazon.com/images/M/MV5BMjI3MzY4NTcwMl5BMl5BanBnXkFtZTgwNDQyMzg3MjE@._V1_.jpg"

#deleta os cookies
def deletar_cookies(cookies):
    cookies["login_realizado"] = ""  # Remove o cookie de login
    cookies["login_timestamp"] = ""  # Remove o timestamp do login
    cookies.save()  # Salva as mudanças nos cookies


def verificar_expiracao_cookie(cookies,cookie_name):
    if cookie_name in cookies:
        # Recupera o timestamp de criação do cookie
        timestamp = cookies.get(cookie_name)
        # Converte para datetime
        timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        if datetime.now() > timestamp + timedelta(minutes=1):  # Expira após 1 minutos, por exemplo
            deletar_cookies(cookies)
            return True
    return False


def pagina_login(cookies):
    # Inicializa as variáveis para controlar o estado de login
    login_realizado = cookies.get("login_realizado")

    if login_realizado and not verificar_expiracao_cookie(cookies, "login_timestamp"):
        membro_entrou(login_realizado)  # Mostra a view passando o nome do usuário
        return
    
    st.title("MOJANGAO + AGREGADOS")

    inserir_fundo(fundo_login)

    
    #st.markdown(css_login(), unsafe_allow_html=True)

    with st.form(key='login_form'):

        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        submit_button = st.form_submit_button(label="Entrar")

        if submit_button:
            # Verifica as credenciais
            user = Usuario.buscar_por_username(usuario)
            if user and user.verificar_senha(senha):
                cookies["login_realizado"] = user.username   # Marca como logado
                cookies["login_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cookies.save()
                st.success("Login bem-sucedido!")
                st.rerun()  #Recarrega a página
            else:
                st.error("Usuário ou senha incorretos. Tente novamente.")
        
        novo_usuario = st.text_input("Novo Usuário (cadastro)")
        nova_senha = st.text_input("Nova Senha", type="password")
        cadastrar = st.form_submit_button(label="Cadastrar")

        if cadastrar:
            try:
                Usuario.criar_usuario(novo_usuario, nova_senha)
                st.success("Usuário cadastrado com sucesso! Faça o login.")
            except ValueError as e:
                st.error(str(e))
            except:
                st.error("Erro ao cadastrar usuário.")
