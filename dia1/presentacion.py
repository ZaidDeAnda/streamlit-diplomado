import streamlit as st

st.title("Presentación del instructor")

st.header("Bienvenidos a la clase de streamlit!")

st.write("Ahora mismo, estamos viendo esta 'presentación' a través de streamlit :D")

st.write("Pero antes de seguir, me presento:")

if st.button("Presentarse 🤺"):

    cols = st.columns([2,3])

    cols[0].image("images/yojeje.jpeg")

    cols[1].subheader("Mi nombre es Zaid De Anda")

    cols[1].markdown("- Me desempeño como ML Engineer en The Home Depot")

    cols[1].markdown("- También trabajo como analista de datos para el gobierno de Nuevo León")

    cols[1].markdown("- Me gustan mucho los videojuegos 🎮")

    cols[1].markdown("- Llevo cerca de 4 años trabajando en la industria con ML, sistemas de visión computacional 📸🧠, etc")

    st.subheader("Ahora sí, empecemos a aprender sobre streamlit.")

    st.success("En el menú de la izquierda, selecciona 'Introducción a Streamlit'")
