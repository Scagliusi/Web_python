import streamlit as st


# Função para verificar login e senha
def verificar_login(usuario, senha):
    if usuario == "guigo miasatto" and senha == "Maminha@357297":
        return True
    else:
        return False

# Função principal
def pagina_login():
    # Inicializa as variáveis para controlar o estado de login
    if 'login_realizado' not in st.session_state:
        st.session_state['login_realizado'] = None  # Inicializa o estado de login no session_state

    if st.session_state['login_realizado'] == None:
        st.title("Confirme a identidade")
        with st.form(key='login_form'):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            submit_button = st.form_submit_button(label="Entrar")
            membro_comum_botao = st.form_submit_button(label="Entre como membro comum")
        
            if submit_button:
                # Verifica as credenciais
                if verificar_login(usuario, senha):
                    st.session_state['login_realizado'] = 'Guigo'   # Marca como logado
                    st.success("Login bem-sucedido!")
                    st.rerun()  # Recarrega a página
                else:
                    st.error("Usuário ou senha incorretos. Tente novamente.")
        
            if membro_comum_botao:
                st.session_state['login_realizado'] = 'membro comum'  
                st.success("Você entrou como membro comum!")
                st.rerun()  # Recarrega a página

    if st.session_state['login_realizado'] == 'Guigo':
        st.title("Bem-vindo Guigo")
        st.write("Você está logado com sucesso!")
        guigo_entrou()

    elif st.session_state['login_realizado'] == 'membro comum':
        st.title("Bem-vindo membro")
        st.write("Você está logado com sucesso!")
        membro_entrou()

pagina_login()

def guigo_entrou():
    pass

def membro_entrou():
    pass
