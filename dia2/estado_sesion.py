import streamlit as st
import psycopg2
import pandas as pd

st.header("Estado de sesión")

st.write("A veces queremos cargar datos muy pesados o utilizar modelos de ML. El problema viene cuando streamlit se recarga con cada interacción que realicemos, como habíamos visto")

st.write("¿Cuál es la solución a esto? El caché!")

st.info("El caché es una memoria que guarda datos de interacciones, para que en el futuro si se necesitan dichos datos, puedan ser leidos desde el caché en lugar de repetir la interacción")

st.write("Streamlit usa de forma 'oculta' el caché, podemos verlo imprimiento `st.session_state`. Funciona de forma muy similar a los diccionarios en python")

st.write(st.session_state)

st.write("Parece un poco vacio, añadamos dos botones con llave")

cols = st.columns(2)

st.warning("**Ejercicio:** Añade dos botones, cada uno con llaves separadas")

######## Inicio de zona de ejercicio


######## Final de zona de ejercicio

st.success("Ajá! Podemos ver como va cambiando los valores del session state.")

st.info("El session state es una memoria que guarda todas las interacciones que realizamos en streamlit, aun cuando no guardamos nuestros valores de widgets en una variable")

st.write("Podemos hacer esto para más interactividad:")

st.button("Boton 1", key="boton1")

if st.session_state['boton1']:
    st.session_state['boton2'] = True

if 'boton2' in st.session_state:
    st.button("Boton 2 magico")

st.write("Funciona para todos los widgets!")

st.info("Esto puede ser util para contraseñas por ejemplo, puesto que nunca tenemos que sacar la variable contraseña y podemos hacer las comparaciones con el cache. Y también, podemos hacer vistas!")

st.warning("**Ejercicio sencillo**: Crea un botón de log in que te muestre una imagen cuando loggeas")

st.warning("**Ejercicio difícil/colaborativo:** crea un sistema de login que muestre una imagen cuando loggeas")

if st.button("Boton de pista"):
    st.write("Puedes empezar creando en caché una variable de logeado, y empezar revisandola")
    st.write("Si no estas logeado, aparece una caja de texto para la contraseña y hace el chequeo")
    st.write("De ser correcta la contraseña, cambias la variable de logeo porque ya no necesitas el input para la contraseña")

######## Inicio de zona de ejercicio

if 'logged_in' in st.session_state:

    st.header("apartado secreto")

    st.write("información secreta")

else:
    st.text_input("Input de prueba", key="input")

if 'input' in st.session_state:

    if st.session_state['input'] == "contraseña":

        st.session_state['logged_in'] = True

######## Final de zona de ejercicio

st.info("Puedes consultar más información en [link](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)")

st.success("Ahora pasa a la página de `Caché` ⬅")
