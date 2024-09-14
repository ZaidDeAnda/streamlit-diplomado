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
#Crea un dataframe de datos random y grafícalo en un area chart
if st.button("Mostrar información", key="area"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.area_chart).")

st.divider()

st.subheader("Gráfico de barras (bar chart)")
#Crea un dataframe de datos random y grafícalo en un bar chart
if st.button("Mostrar información", key="bar"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart).")

st.divider()

st.subheader("Gráfico de linea (line chart)")
#Crea un dataframe de datos random y grafícalo en un line chart
if st.button("Mostrar información", key="line"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.line_chart).")

st.divider()

st.subheader("Gráfico de dispersión (scatter chart)")
#Crea un dataframe de datos random y grafícalo en un scatter chart
if st.button("Mostrar información", key="scatter"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart).")

st.warning("*Ejercicio*: Crea un gráfico de dispersión sobre el dataset iris sobre dos ejes que el usuario seleccione")
######## Inicio de zona de ejercicio


######## Final de zona de ejercicio

st.divider()

st.subheader("Mapas!")
st.write("streamlit también permite gráficos de dispersión sobre mapas de forma 'nativa'")
#Crea un dataset de datos random con las coordenadas de león, y columnas lat y lon, para posteriormente mostrar un mapa
if st.button("Mostrar información", key="map"):
    st.info("La documentación de la función se encuentra en este [link](https://docs.streamlit.io/develop/api-reference/charts/st.map).")

st.header("Gráficos con plotly!")

st.write("Finalmente, intentemos agregar unos gráficos con plotly usando los datos de iris.")

st.success("Finalizado del día 1!")