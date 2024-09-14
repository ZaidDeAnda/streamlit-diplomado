import streamlit as st
import plotly.express as px
import seaborn as sns
import numpy as np
import pandas as pd

# Título de la aplicación
st.title("Visualización de datos en Streamlit")

st.write("Streamlit tiene algunos tipos de gráficas de forma nativa, como gráficas de area, de línea, etc.")

st.warning("Realmente no es de forma nativa, solo son wrappers alrededor de un framework de gráficos llamado Altair. Pero nos permite ahorrar líneas de código, graficar cosas de manera más sencilla a coste de menos flexibilidad")

st.write("Pero por si esto llega a ser poco, también puede renderizar gráficas de los frameworks más comunes: matplotlib, seaborn, plotly, graphviz, etc.")

st.write("Veremos las gráficas nativas de streamlit y luego trabajaremos un poco con plotly")

st.info("**¿Por qué plotly?** Plotly ofrece una manera fácil de realizar gráficos interactivos sin el esfuerzo/líneas de código adicionales que requeriría matplotlib.")

st.header("Tipos de gráficos")

st.write("Primero exploraremos los tipos de gráficos nativos de streamlit:")
st.subheader("Gráfico de area (area chart)")
area_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(area_chart_data)
if st.button("Mostrar información", key="area"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.area_chart).")

st.divider()

st.subheader("Gráfico de barras (bar chart)")
bar_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(bar_chart_data)
if st.button("Mostrar información", key="bar"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart).")

st.divider()

st.subheader("Gráfico de linea (line chart)")
line_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(line_chart_data)
if st.button("Mostrar información", key="line"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.line_chart).")

st.divider()

st.subheader("Gráfico de dispersión (scatter chart)")
scatter_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(scatter_chart_data)
if st.button("Mostrar información", key="scatter"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart).")

st.warning("*Ejercicio*: Crea un gráfico de dispersión sobre el dataset iris sobre dos ejes que el usuario seleccione")
######## Inicio de zona de ejercicio


######## Final de zona de ejercicio

st.divider()

st.subheader("Mapas!")
st.write("streamlit también permite gráficos de dispersión sobre mapas de forma 'nativa'")
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [21.12, -101.67],
    columns=["lat", "lon"],
)
st.map(df)
if st.button("Mostrar información", key="map"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.map).")

st.header("Gráficos con plotly!")

st.write("Finalmente, intentemos agregar unos gráficos con plotly usando los datos de iris.")


#Crea un histograma
iris = sns.load_dataset('iris')
st.write(iris)
columna = "petal_length"
fig = px.histogram(iris, x=columna, nbins=20, title=f"Histograma de {columna}", color="species", marginal="box")
st.plotly_chart(fig)

#Crea un scatter graph
fig = px.scatter(iris, x="petal_length", y="sepal_length", color="petal_width")
st.plotly_chart(fig)

st.success("Finalizado del día 1!")