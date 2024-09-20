import streamlit as st
import pandas as pd
import psycopg2
import ultralytics

st.subheader("Cache para funciones")

st.write("Ahora que exploramos un poco como funciona el cache, veamos como utilizarlo para almacenar datos pesados")

st.write("Para esto, tenemos que guardar nuestra carga de datos dentro de una función de python, y a esta agregarle un decorador especial")

st.info("Los decoradores en python se marcan con el caracter @ y añaden comportamientos especiales a una función. Más información en [link](https://www.learnpython.org/es/Decorators)")

st.write("Para estos ejemplos, ahora vamos a conectarnos a nuestra base de datos de arte!")

#Inserte datos de DB

conn = psycopg2.connect(
    **params
)

#return_df = pd.read_sql_query('SELECT * From "Pinturas"', conn)

#st.write(return_df)

st.button("Presioname!")

st.write("Notamos que con cada interacción que hacemos, se recarga la página y por ende recargamos los datos.")

st.write("Vamos a guardar esta función en caché! Usaremos el decorador `st.cache_data`")

st.info("Hay dos tipos de cache en streamlit, `st.cache_data` y `st.cache_resource`. Aprende más sobre ellos en [link](https://docs.streamlit.io/develop/concepts/architecture/caching)")

st.code("""
@st.cache_data
def load_data(query, params):
    conn = psycopg2.connect(
        **params
    )
    return pd.read_sql_query(query, conn)
""")

@st.cache_data
def load_data(query, params):
    conn = psycopg2.connect(
        **params
    )
    return pd.read_sql_query(query, conn)

st.write("Esta función solo se ejecutará cuando alguno de sus argumentos cambie.")

cached_df = load_data('SELECT * From "Pinturas"', params)

st.write(cached_df)

st.write("Ahora comentemos el df anterior y dejemos solo el df en cache")

st.warning("También podemos acelerar la carga del programa cargando una cantidad menor de datos, en lugar de la DB entera. Depende mucho del enfoque del trabajo y de las capacidades del servidor. Food for thought 🧠")

st.info("Esto funciona igual para modelos de ML. Los cargas con una función en caché, y solo los llamas cuando necesites. Esto puede ser util cuando tienes diferentes modelos que puedes cargar")

st.warning("**Ejercicio:** Carguemos un modelo yolo variable!")
