import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from ultralytics import YOLO
import cv2

# Título y descripción de la app
st.title("Aplicación de muestra de Streamlit")
st.write("Esta aplicación demuestra las capacidades principales de Streamlit, como texto, gráficos, interactividad y visualización de datos.")

# Sección de texto
st.header("Texto y Markdown")
st.write("Puedes usar Streamlit para escribir texto y mostrarlo en diferentes formatos.")
st.markdown("""
### Este es un ejemplo de Markdown
Puedes incluir **negritas**, *cursivas*, listas, [enlaces](https://streamlit.io/), y mucho más.
""")

# Sección de interactividad: Widgets
st.header("Interactividad con Widgets")
name = st.text_input("¿Cuál es tu nombre?")
if name:
    st.write(f"Hola, {name}! Bienvenido a esta aplicación de Streamlit.")

age = st.slider("¿Cuántos años tienes?", 0, 100, 25)
st.write(f"Tienes {age} años.")

# Sección de visualización de gráficos
st.header("Visualización de Gráficos")
st.write("Streamlit te permite mostrar gráficos de manera sencilla usando diferentes bibliotecas como Matplotlib, Plotly, etc.")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

st.line_chart(chart_data)

# Visualización de datos: Tabla y Gráficos
st.header("Visualización de Datos con DataFrames")
st.write("A continuación mostramos un DataFrame de ejemplo:")

# Generar datos aleatorios
data = pd.DataFrame({
    "Categoría": ["A", "B", "C", "D"],
    "Valores": np.random.randint(1, 100, 4)
})
st.write(data)

# Visualización de gráfico de barras
st.subheader("Gráfico de matplotlib ⬇")
fig, ax = plt.subplots()
ax.bar(data["Categoría"], data["Valores"])
st.pyplot(fig)

# Sección de carga de archivos
st.header("Carga de Archivos")
st.write("Puedes subir archivos para trabajar con ellos en Streamlit.")
uploaded_file = st.file_uploader("Elige un archivo de imagen")
cols = st.columns(2)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Mostrar la imagen en la app
    cols[0].image(image, caption="Imagen subida", use_column_width=True)
    
    # Mostrar información de la imagen
    cols[0].write(f"Dimensiones de la imagen: {image.size}")

    with st.spinner('Haciendo magia.... ⚙'):
        if cols[0].button("Presiona para ver magia"):
            model = YOLO('yolov8n.pt')
            result = model(image)
            open_cv_image = np.array(image)
            open_cv_image = open_cv_image[:, :, ::-1].copy()
            for detection in result[0].boxes.data:
                        x0, y0 = (int(detection[0]), int(detection[1]))
                        x1, y1 = (int(detection[2]), int(detection[3]))
                        score = round(float(detection[4]), 2)
                        cls = int(detection[5])
                        object_name =  model.names[cls]
                        label = f'{object_name} {score}'
                        
                        cv2.rectangle(open_cv_image, (x0, y0), (x1, y1), (255, 150, 0), 10)
                        cv2.putText(open_cv_image, label, (x0, y0 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 150, 0), 3)

            cols[1].image(open_cv_image[:, :, ::-1],caption="Imagen procesada")

# Control de ejecución de código condicional
st.header("Ejecutar Bloques de Código")
if st.button("Presiona para mostrar más información"):
    st.write("¡Streamlit permite ejecutar código condicional basado en la interacción del usuario!")

# Final
st.write("Eso es todo por ahora. ¡Experimenta con Streamlit y sus características!")
