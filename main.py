import streamlit as st
from login import pagina_login
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(prefix="loginsupimpa/", password="supersecretkey")

# Verifica se os cookies estão prontos
if not cookies.ready():
    st.stop()  # app volta a rodar na proxma interacao


pagina_login(cookies)
