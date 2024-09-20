import streamlit as st

st.header("Información adicional")

st.write("Antes de pasar a la creación de dashboards, necesitamos ver dos temas importantes, columnas y estructura de una aplicación de streamlit")

st.subheader("Columnas")

st.write("Primero, veremos una función extra para acomodo de columnas, `st.columns`. Se llama de la siguiente manera")

st.code("""
cols = st.columns(2)

cols[0].write("columna 1")
cols[1].write("columna 2")
""")

st.write("Con el siguiente resultado")

cols = st.columns(2)

cols[0].write("columna 1")
cols[1].write("columna 2")

st.write("Si queremos columnas de tamaño variable, en lugar de pasar un número como argumento, pasamos una lista cuya longitud equivale al número de columnas que queramos, y cada valor de la lista la anchura de dicha columna. Por ejemplo")

st.code("""
cols = st.columns([1,5,1])

cols[0].write("columna 1")
cols[1].write("columna 2")
cols[2].write("columna 3")
""")

cols = st.columns([1,5,1])

cols[0].write("columna 1")
cols[1].write("columna 2")
cols[2].write("columna 3")

st.info("Mas información en [link](https://docs.streamlit.io/develop/api-reference/layout/st.columns)")

st.subheader("Estructura de un proyecto en streamlit")

st.write("Cuando creas un proyecto de streamlit, quieres que tu estructura sea de la siguiente manera (si es una aplicación multipage)")

st.code("""
app/
├─ utils/
│  ├─ database.py
│  ├─ authentication.py
├─ pages/
│  ├─ page1.py
│  ├─ page2.py
├─ images/
│  ├─ img1.png
│  ├─ img2.png
├─ .gitignore
├─ app.py
├─ README.md
├─ requirements.txt
""")

st.write("Para crear una simple aplicación de streamlit, basta con crear con archivo con el import de streamlit y empezar a escribir!")

st.code("""
import streamlit as st
        
st.write("Hola mundo!")
""")

st.write("Y llamarlo con `streamlit run <nombre-archivo>.py`")

st.write("Para páginas multipage, es un poco más complicado. Tenemos que tener nuestros archivos (visualizaciones) en una carpeta. Desde aquí, hay dos maneras:")

st.write("La manera más sencilla, es dentro de una carpeta llamada `pages`, introducir todos nuestros archivos, y streamlit automáticamente reconocerá que es una página multipage")

st.write("Pros: es muy fácil de crear. Contras: No hay personalización de acuerdo al usuario.")

st.write("La manera un poco más completa, con `st.navigation`. Para ello, debemos de crear un diccionario que mapee las páginas y los archivos")

st.code("""
pages = {
    "Día 1": [
        st.Page("dia1/presentacion.py", title="Presentación"),
        st.Page("dia1/introduccion.py", title="Introducción a streamlit"),
        st.Page("dia1/conceptos_basicos.py", title="Conceptos básicos"),
        st.Page("dia1/visualizacion_datos.py", title="Visualización de datos")
    ],
    "Día 2": [
        st.Page("dia2/estado_sesion.py", title="Estado de sesión"),
        st.Page("dia2/cache.py", title="Caché"),
        st.Page("dia2/info.py", title="Información adicional"),
        st.Page("dia2/dashboard.py", title="Creación de Dashboards"),
    ],
}
""")

st.write("Y ahora solo llamamos `st.navigation(pages).run()` y voila!")

st.write("Pros de esto, mucho más control para las páginas, si tenemos varios usuarios, podemos mostrar algunas páginas a solo algunos usuarios; puedes mantener ciertos valores de widgets entre múltiples páginas, etc. El contra, es un poco más de trabajo, pero sigue siendo streamlit, así que es muy poco realmente!")

st.info("Más información en [multipage](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app) y en [navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation)")

st.subheader("Ahora sí, a los dashboards")

st.write("Un dashboard es un lugar donde mostramos de una forma muy gráfica los insights que podemos extraer del fenómeno que queramos modelar")
st.write("Por ejemplo, si quisiéramos estudiar sobre nuestra base de datos de pinturas, buscariamos responder preguntas como:")
st.markdown("-¿De qué país salieron más obras?")
st.markdown("-¿Cuál es la técnica más popular?")
st.markdown("-¿Hubo algún periodo de tiempo de cambios drásticos?")
st.markdown("-¿Cambio la popularidad de alguna técnica respecto del tiempo?")

st.write("Para todas esas preguntas, trabajaremos en la creación de un dashboard!")


