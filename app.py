import streamlit as st

pages = {
    "Día 1": [
        st.Page("dia1/presentacion.py", title="Presentación"),
        st.Page("dia1/introduccion.py", title="Introducción a streamlit"),
        st.Page("dia1/conceptos_basicos.py", title="Conceptos básicos")
    ],
    "Día 2": [
        st.Page("dia2/cache.py", title="Manejo de cache"),
    ],
}

pg = st.navigation(pages)

pg.run()