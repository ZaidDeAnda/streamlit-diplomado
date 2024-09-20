import streamlit as st

st.header("Creación de dashboards")

st.write("Finalmente, lo que todos esperábamos, ¿Cómo hacer dashboards?")

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

st.subheader("Ahora sí, a los dashboards")

st.write("Un dashboard es un lugar donde mostramos de una forma muy gráfica los insights que podemos extraer del fenómeno que queramos modelar")
st.write("Por ejemplo, si quisiéramos estudiar sobre nuestra base de datos de pinturas, buscariamos responder preguntas como:")
st.markdown("-¿De qué país salieron más obras?")
st.markdown("-¿Cuál es la técnica más popular?")
st.markdown("-¿Hubo algún periodo de tiempo de cambios drásticos?")
st.markdown("-¿Cambio la popularidad de alguna técnica respecto del tiempo?")

st.write("Para todas esas preguntas, trabajaremos en la creación de un dashboard!")


