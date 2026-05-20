import streamlit as st

# CONFIG
st.set_page_config(
    page_title="Empresas Parceiras",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

/* FUNDO */
.stApp{
    background-color: #0b1020;
}

/* TITULO */
h1{
    color: white;
    font-size: 50px !important;
    margin-bottom: 40px;
}

/* CARD */
.card{
    background-color: #161b2e;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.5);
    transition: 0.3s;
    height: 100%;
}

/* EFEITO */
.card:hover{
    transform: translateY(-8px);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.8);
}

/* TITULO CARD */
.nome{
    color: white;
    font-size: 28px;
    font-weight: bold;
    margin-top: 15px;
}

/* TEXTO */
.desc{
    color: #d1d1d1;
    font-size: 16px;
    line-height: 1.6;
    margin-top: 10px;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# ================= TITULO =================
st.title("🌐 Empresas Parceiras")

# ================= COLUNAS =================
col1, col2, col3 = st.columns(3)

# =========================
# SPACEX
# =========================
with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image("spacex.png", use_container_width=True)

    st.markdown("""
    <div class="nome">🚀 SpaceX</div>

    <div class="desc">
    Empresa aeroespacial criada por Elon Musk.
    Atua no desenvolvimento de foguetes e viagens espaciais.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Acessar Site",
        "https://www.spacex.com/"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# APPLE
# =========================
with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image("apple.png", use_container_width=True)

    st.markdown("""
    <div class="nome">🍎 Apple</div>

    <div class="desc">
    Empresa mundialmente conhecida pelos seus produtos tecnológicos,
    como iPhone, iPad e MacBook.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Acessar Site",
        "https://www.apple.com/br/"
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# NETFLIX
# =========================
with col3:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.image("netflix.png", use_container_width=True)

    st.markdown("""
    <div class="nome">🎬 Netflix</div>

    <div class="desc">
    Plataforma de streaming com filmes, séries e documentários
    assistidos no mundo inteiro.
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Acessar Site",
        "https://www.netflix.com/br/"
    )

    st.markdown("</div>", unsafe_allow_html=True)
