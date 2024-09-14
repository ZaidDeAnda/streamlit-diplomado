import streamlit as st
import seaborn as sns
import pandas as pd

# Mostrar código básico de ejemplo
st.subheader("Ejemplo básico")
st.code("""
import streamlit as st

st.title("Hola, Mundo en Streamlit")
st.write("Este es un ejemplo básico de una aplicación web con Streamlit.")
""", language='python')

st.warning("""
**Ejercicio:** Modifica el código para escribir un 'Hola mundo!' en la parte de abajo ⬇""")

st.divider()

st.subheader("zona de código")

######## Inicio de zona de ejercicio


######## Final de zona de ejercicio


st.divider()

st.info("`st.write` funciona para escribir (casi) cualquier tipo de datos en streamlit. Puede ser texto, una lista, un diccionario, hasta una imagen!")
st.write("Ahora escribamos tanto headers y subheaders")

st.divider()

st.subheader("zona de código")

######## Inicio de zona de ejercicio


######## Final de zona de ejercicio


st.divider()

st.info("Tanto `st.header` como `st.subheader` funcionan para formatear el texto en forma de títulos y subtítulos respectivamente.")

# Sección de Widgets Interactivos
st.header("2. Widgets Interactivos")
st.write("""
Streamlit provee diferentes widgets que permiten interacción con los usuarios.
A continuación, algunos ejemplos básicos.
""")

# Ejemplo de botón
st.subheader("Botones")
# Crea un botón aquí
if st.button("Mostrar información", key="button"):
    st.info("`st.button` funciona de manera peculiar. Regresa un `True` cuando se presiona, y por ende puedes usarlo como condicional. Solo recuerda que streamlit se recarga al presionarlo!  Más info: [link](https://docs.streamlit.io/develop/api-reference/widgets/st.button)")


# Ejemplo de selección
st.subheader("Cajas de selección")
#Crea una caja aqui
if st.button("Mostrar información", key="selectbox"):
    st.info("`st.selectbox` permite hacer una barra de selección para opciones preestablecidas.  Más info: [link](https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox)")

# Ejemplo de input de texto
st.subheader("Entradas de texto")
#Crea un text input aquí
if st.button("Mostrar información", key="text_input"):
    st.info("`st.text_input` permite que introduzcas el texto que quieras al programa! Cuando presionas enter, se hace submit al texto y se actualiza la página. Más info: [link]( Más info: [link]( Más info: [link](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input)")

# Ejemplo de slider
st.subheader("Sliders")
#Crea una slider aquí
if st.button("Mostrar información", key="sliders"):
    st.info("`st.slider` permite hacer un slider de diferentes tipos valores, incluso con tiempo! Más info: [link](https://docs.streamlit.io/develop/api-reference/widgets/st.slider)")

st.subheader("Slider de seleccion")
#Crea un select slider de colores aquí
if st.button("Mostrar información", key="select_sliders"):
    st.info("`st.select_slider` permite hacer un slider de valores categóricos (no discretos). Más info: [link](https://docs.streamlit.io/develop/api-reference/widgets/st.select_slider)")

# Ejemplo de checkbox 
estado = st.checkbox("Form checkbox")
#Crea una checkbox aquí
if st.button("Mostrar información", key="checkbox"):
    st.info("`st.checkbox` ayuda para valores booleanos interactivos. Puede ser util para una lista de tareas! Más info: [link](https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox)")

st.subheader("3. Trabajando con datos")

# Ilustración de cargar datos de pandas
st.write("También podemos trabajar con pandas directamente! Carguemos el dataset de Iris")

#Carga del dataset de iris de seaborn y crea un dataframe a partir de el

st.warning("*Ejercicio*: crea un slider para filtrar el dataframe de acuerdo a una columna")

######## Inicio de zona de ejercicio


######## Final de zona de ejercicio

st.divider()

st.subheader("zona de código")

st.divider()

st.warning("*Ejercicio*: ahora con dos sliders")

######## Inicio de zona de ejercicio


######## Final de zona de ejercicio

st.divider()

st.info("Pero... ¿Qué pasa si quiero que no se recarguen hasta realizar mi seleccion de valores?")

if st.button("Presione este botón para obtener una solución"):

    st.success("Para eso sirven los formularios! 💡")

st.subheader("Un formulario nos ayuda a agrupar ciertos componentes fuera de este ciclo de ejecución constante de streamlit.")

st.write("Este proceso puede ser una carga de modelos de ML, un query de datos (como lo que estamos haciendo, solo que más largo), o cualquier proceso que demore")

st.info("Un formulario tiene que llevar un botón `st.submit_button` que determina en qué momento se ejecutaran los elementos dentro del formulario")

st.warning("*Ejercicio*: Crea dentro del formulario dos sliders que controlen el filtrado del dataframe")

st.divider()

st.subheader("zona de código")

with st.form("my_form"):

    if st.form_submit_button():
        st.write("Se ejecutó el form!")

st.divider()