import streamlit as st
from streamlit_cookies_manager import  EncryptedCookieManager
from datetime import datetime, timedelta
from views import guigo_entrou, membro_entrou
from utils import inserir_fundo,css_login


fundo_login = "https://m.media-amazon.com/images/M/MV5BMjI3MzY4NTcwMl5BMl5BanBnXkFtZTgwNDQyMzg3MjE@._V1_.jpg"


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
        if datetime.now() > timestamp + timedelta(minutes=5):  # Expira após 5 minutos, por exemplo
            deletar_cookies(cookies)
            return True

    return False


# Função para verificar login e senha
def verificar_login(usuario, senha):
    if usuario.lower() == "guigo miasatto" and senha == "Maminha@357297":
        return True
    else:
        return False

# Função principal
def pagina_login(cookies):
    # Inicializa as variáveis para controlar o estado de login
    login_realizado = cookies.get("login_realizado")



    if login_realizado == 'Guigo' and not verificar_expiracao_cookie(cookies,"login_timestamp"):
        guigo_entrou()  # Mostra a página do Guigo
        return
    elif login_realizado == 'membro comum' and not verificar_expiracao_cookie(cookies,"login_timestamp"):
        membro_entrou()  # Mostra a página do membro comum
        return

    st.title("MOJANGAO + AGREGADOS")
    inserir_fundo(fundo_login)

    
    #st.markdown(css_login(), unsafe_allow_html=True)

    with st.form(key='login_form'):

        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        submit_button = st.form_submit_button(label="Entrar")
        membro_comum_botao = st.form_submit_button(label="Entre como membro comum")

        
        if submit_button:
            # Verifica as credenciais
            if verificar_login(usuario, senha):
                cookies["login_realizado"] = 'Guigo'   # Marca como logado
                cookies["login_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cookies.save()
                st.success("Login bem-sucedido!")
                st.rerun()  # Recarrega a página
            else:
                st.error("Usuário ou senha incorretos. Tente novamente.")
        if membro_comum_botao:
            cookies["login_realizado"] = 'membro comum'  
            cookies["login_timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cookies.save()
            st.success("Você entrou como membro comum!")
            st.rerun()  # Recarrega a página
