import streamlit as st
import base64

# CONFIG
st.set_page_config(
    page_title="Empresas Parceiras",
    layout="wide"
)

# ========= FUNÇÃO BASE64 =========
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# ========= IMAGENS =========
spacex = get_base64_image("spacex.png")
apple = get_base64_image("iphone.png")
netflix = get_base64_image("netflix.png")

# ========= CSS =========
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0f1117;
    color: white;
    font-family: Arial;
}

/* TÍTULO */
.titulo {
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitulo {
    color: #a0a0a0;
    margin-bottom: 40px;
}

/* CARD */
.card {
    background-color: #181c24;
    border-radius: 18px;
    padding: 15px;
    transition: 0.3s;
    height: 100%;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.4);
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px rgba(255,255,255,0.1);
}

/* IMAGEM */
.card img {
    width: 100%;
    border-radius: 15px;
    margin-bottom: 15px;
}

/* TITULO CARD */
.nome {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* DESCRIÇÃO */
.desc {
    color: #b0b0b0;
    font-size: 16px;
    margin-bottom: 20px;
}

/* BOTÃO */
.botao {
    background-color: #2563eb;
    color: white;
    padding: 10px 20px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
}

.botao:hover {
    background-color: #1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# ========= TÍTULO =========
st.markdown("""
<div class="titulo">
    Empresas Parceiras -
</div>

<div class="subtitulo">
    Conheça algumas empresas de tecnologia
</div>
""", unsafe_allow_html=True)

# ========= COLUNAS =========
col1, col2, col3 = st.columns(3)

# ========= CARD 1 =========
with col1:
    st.markdown(f"""
    <div class="card">

        <img src="data:image/png;base64,{spacex}">

        <div class="nome">
            🚀 SpaceX
        </div>

        <div class="desc">
            Empresa de exploração espacial fundada por Elon Musk.
        </div>

        <a class="botao"
           href="https://www.spacex.com/"
           target="_blank">
           Acessar
        </a>

    </div>
    """, unsafe_allow_html=True)

# ========= CARD 2 =========
with col2:
    st.markdown(f"""
    <div class="card">

        <img src="data:image/png;base64,{apple}">

        <div class="nome">
            🍎 Apple
        </div>

        <div class="desc">
            Empresa multinacional criadora do iPhone e MacBook.
        </div>

        <a class="botao"
           href="https://www.apple.com/br/"
           target="_blank">
           Acessar
        </a>

    </div>
    """, unsafe_allow_html=True)

# ========= CARD 3 =========
with col3:
    st.markdown(f"""
    <div class="card">

        <img src="data:image/png;base64,{netflix}">

        <div class="nome">
            🎬 Netflix
        </div>

        <div class="desc">
            Plataforma líder de filmes e séries online.
        </div>

        <a class="botao"
           href="https://www.netflix.com/br/"
           target="_blank">
           Acessar
        </a>

    </div>
    """, unsafe_allow_html=True)
