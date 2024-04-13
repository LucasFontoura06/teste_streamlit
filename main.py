import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
import numpy as np


# ---- PAGE CONFIG ----
# SE QUISER DEIXAR A TELA TODA = ESTICADO
# st.set_page_config(page_title="My Webpage", page_icon=":jack_o_lantern:", layout="wide")

st.set_page_config(page_title="My Webpage", page_icon=":jack_o_lantern:")

# ---- FUNCAO AUXILIAR ----

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_senatran = Image.open("C:\\Users\\lucas\\Arquivos_Lucas\\04.Python_Projects\\website\\images\\site_senatran_home_page.png")

# ---- VARIABLES ----

IMAGEM_LUCAS = "C:\\Users\\lucas\\Arquivos_Lucas\\04.Python_Projects\\website\\images\\LUCAS.jpg"

# ---- SUMÁRIO ----

st.sidebar.header('Sumário')
st.sidebar.markdown("""
- <span style="color:white;border-bottom: none;">**[Sobre](#começo):** Informações sobre Lucas</span>
- <span style="color:white;">**[Projetos](#projetos):** Alguns projetos de Lucas</span>
- <span style="color:white;">**[Gráficos](#graficos):** Visualização de dados</span>
""", unsafe_allow_html=True)


# ---- HEADER SECTION ----

st.write('<div id="começo"></div>', unsafe_allow_html=True)
with st.container():
    # Dividindo a largura da linha em duas partes
    col1, col2 = st.columns([10, 2])
    
    # Coluna 1 contém o subcabeçalho, título e texto
    with col1:
        st.subheader("Hi, I am Lucas :wave:")
        st.title("A Data Analyst From Brazil")
        st.write("I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings.")
    
    # Coluna 2 contém a imagem
    with col2:
        # Aplicando estilo CSS para tornar a imagem redonda
        st.image(IMAGEM_LUCAS, width=200)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do?")
        st.write("##")
        st.write(
            """
            I work at SENATRAN, where I'm part of the RENAEST team.
            - I develop automation scripts to streamline tasks.
            - I clean spreadsheets to ensure clearer data reading.
            - I verify the codes used in the tickets.
            """
        )
        st.write("[WebSite SENATRAN >](https://www.gov.br/transportes/pt-br/assuntos/transito/arquivos-senatran/docs/renaest)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
        
st.write('<div id="projetos"></div>', unsafe_allow_html=True)        
with st.container():
    st.write("----")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_senatran)
    with text_column:
        st.subheader("Website for team SENATRAN")
        st.write(
            """
            I have created a web page using HTML and CSS, hosted on Firebase for the CGSIE team, streamlining information access for the team.
            """
        )
        st.markdown("[Link...](https://senatran-cgsie.web.app/index.html)")

# ---- GRAFICOS ----

st.write('<div id="graficos"></div>', unsafe_allow_html=True)        
with st.container():
    st.write("----")
    st.header("Gráficos")
    st.write("##")
    st.write("Esse é um exemplo de grafico de barras feito em python!")

    # Gerando dados para o gráfico de barras
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [10, 20, 15, 25, 30]

    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    bars = ax.bar(categories, values, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

    # Adicionando rótulos com os valores em cima de cada barra
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, height,
                ha='center', va='bottom', color='black')

    ax.set_xlabel('Categorias')
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico de Barras')

    # Removendo as bordas da figura
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Exibindo o gráfico no Streamlit
    st.pyplot(fig)

