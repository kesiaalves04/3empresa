import streamlit as st

st.set_page_config(page_title="Empresas Parceiras", layout="wide")

st.title("🌐 Empresas Parceiras")

col1, col2, col3 = st.columns(3)

# SPACE X
with col1:
    st.image("espaçox.png", use_container_width=True)
    st.subheader("🚀 SpaceX")
    st.write("Empresa aeroespacial criada por Elon Musk.")
    st.link_button("Acessar Site", "https://www.spacex.com/")

# APPLE
with col2:
    st.image("iphone.png", use_container_width=True)
    st.subheader("🍎 Apple")
    st.write("Empresa mundialmente conhecida pela tecnologia.")
    st.link_button("Acessar Site", "https://www.apple.com/br/")

# NETFLIX
with col3:
    st.image("netflix.png", use_container_width=True)
    st.subheader("🎬 Netflix")
    st.write("Plataforma de streaming de filmes e séries.")
    st.link_button("Acessar Site", "https://www.netflix.com/br/")
