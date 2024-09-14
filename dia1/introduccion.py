import streamlit as st
from PIL import Image

# Título del taller
st.title("Taller: Conceptos Básicos de Streamlit")

# Sección de Introducción
st.header("1. ¿Qué es Streamlit?")
st.write("""
Streamlit es una biblioteca de Python de código abierto que permite crear aplicaciones web interactivas con solo unas pocas líneas de código. Es ideal para crear dashboards, visualizar datos y construir herramientas de machine learning rápidamente.
""")

# Imagen ilustrativa de un dashboard creado con Streamlit
image1 = Image.open('images/dashboard_example.png')  # Asegúrate de tener la imagen en el directorio correcto
st.image(image1, caption="Ejemplo de un dashboard creado con Streamlit")

st.write("""
### Beneficios:
- **Fácil**: Construcción rápida de aplicaciones con Python.
- **Interactividad**: Widgets y controles interactivos sin necesidad de manejar complejidad adicional.
- **Despliegue sencillo**: Publica tu aplicación en la web en cuestión de minutos.
""")

# Casos de uso breves y visuales
st.header("2. Casos de Uso")
st.write("### Algunos casos en los que Streamlit es ideal:")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Dashboards**")
    image_dashboard = Image.open('images/dashboard.png')  # Imagen de un dashboard
    st.image(image_dashboard)

with col2:
    st.write("**Aplicaciones de Machine Learning**")
    image_ml = Image.open('images/machine_learning_app.png')  # Imagen de aplicación de ML
    st.image(image_ml)

with col3:
    st.write("**Visualización de Datos**")
    image_viz = Image.open('images/data_viz.png')  # Imagen de una visualización de datos
    st.image(image_viz)

st.write("""
Estas aplicaciones son rápidas de construir y se pueden desplegar fácilmente, lo que las convierte en una excelente herramienta para ciencia de datos, análisis de negocios y proyectos de aprendizaje automático.
""")

# Cómo funciona
st.header("3. ¿Cómo usar esta página?")
st.write("""
Esto está escrito para que pueda ser usado como consulta, aún cuando no esté yo. El texto en azul te da detalles técnicos de las funciones que se usan, como este ⬇
""")

st.info("Este texto sirve para dar información técnica")

st.text("También habrá zonas llamadas *Zonas de código* hechas para que puedas practicar el tema que se esté viendo! Siempre vienen acompañadas de un enunciado de ejercicio en rojo")

st.warning("*Ejercicio*: Ve a la siguiente página")

st.success("Para la siguiente sección, ir al apartado de `Conceptos basicos` en el menú de la izquierda ⬅")

