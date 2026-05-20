import streamlit as st
import base64

# CONFIG
st.set_page_config(
    page_title="Empresas Parceiras",
    layout="wide"
)

# ========= FUNÇÃO =========
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

.stApp{
    background-color: #0b1020;
}

/* TÍTULO */
.titulo{
    font-size: 52px;
    font-weight: bold;
    color: white;
    margin-bottom: 5px;
}

.subtitulo{
    color: #b3b3b3;
    font-size: 18px;
    margin-bottom: 40px;
}

/* CARD */
.card{
    background: #161b2e;
    border-radius: 20px;
    padding: 18px;
    transition: 0.3s;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}

.card:hover{
    transform: translateY(-5px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.6);
}

/* IMAGEM */
.card img{
    width: 100%;
    border-radius: 15px;
    margin-bottom: 15px;
}

/* NOME */
.nome{
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* DESCRIÇÃO */
.desc{
    color: #cfcfcf;
    font-size: 16px;
    line-height: 1.5;
    margin-bottom: 25px;
}

/* BOTÃO */
.botao{
    background-color: #2563eb;
    color: white !important;
    padding: 10px 20px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
}

.botao:hover{
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

# ========= SPACEX =========
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

# ========= APPLE =========
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

# ========= NETFLIX =========
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
    """, unsafe_allow_html=True))
