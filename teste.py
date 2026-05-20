import streamlit as st

# ================= CONFIG =================
st.set_page_config(
    page_title="Empresas Parceiras",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

/* FUNDO */
.stApp{
    background-color: #0B1020;
}

/* TITULO */
h1{
    color: white !important;
    font-size: 50px !important;
    margin-bottom: 40px;
}

/* TEXTO */
p{
    color: #D1D5DB;
}

/* BOTÃO */
div.stButton > button,
div.stLinkButton > a {
    background-color: #2563EB !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 10px 20px !important;
    text-decoration: none !important;
}

/* IMAGEM */
img{
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ================= TITULO =================
st.title("🌐 Empresas Parceiras")

# ================= COLUNAS =================
col1, col2, col3 = st.columns(3)

# ================= SPACEX =================
with col1:

    st.image("spacex.png", use_container_width=True)

    st.subheader("🚀 SpaceX")

    st.write("""
    Empresa aeroespacial criada por Elon Musk.
    Atua no desenvolvimento de foguetes e viagens espaciais.
    """)

    st.link_button(
        "Acessar Site",
        "https://www.spacex.com/"
    )

# ================= APPLE =================
with col2:

    st.image("apple.png", use_container_width=True)

    st.subheader("🍎 Apple")

    st.write("""
    Empresa mundialmente conhecida pelos seus produtos tecnológicos,
    como iPhone, iPad e MacBook.
    """)

    st.link_button(
        "Acessar Site",
        "https://www.apple.com/br/"
    )

# ================= NETFLIX =================
with col3:

    st.image("netflix.png", use_container_width=True)

    st.subheader("🎬 Netflix")

    st.write("""
    Plataforma de streaming com filmes, séries e documentários
    assistidos no mundo inteiro.
    """)

    st.link_button(
        "Acessar Site",
        "https://www.netflix.com/br/"
    )
