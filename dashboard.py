import streamlit as st
from Clases.tablero import Tableros
import matplotlib.pyplot as plt
import math

# Configurar el ancho de la página
st.set_page_config(layout="wide")

st.title("Serpientes y Escaleras")

# Crear controles de entrada para el usuario
casillas = st.number_input("Cantidad de Casillas en el juego.", min_value=12, max_value=80, value=30, step=1)
escaleras = st.number_input("Cantidad de Escaleras", min_value=0, max_value=math.floor(casillas / 6), value=1, step=1)
serpientes = st.number_input("Cantidad de Serpientes", min_value=0, max_value=math.floor(casillas / 6), value=1, step=1)
personajes = st.number_input("Cantidad de Personajes", min_value=1, max_value=5, value=4, step=1)

# Inicializar el tablero
if 'tablero' not in st.session_state:
    st.session_state.tablero = None
    st.session_state.mensaje = "Presiona 'Empezar Juego' para comenzar."

# Botón para empezar el juego
if st.button("Empezar Juego"):
    st.session_state.tablero = Tableros(numeroCasillas=casillas, numeroSerpientes=serpientes, numeroEscaleras=escaleras, numeroPiezas=personajes)
    st.session_state.mensaje = "¡Juego iniciado! Presiona 'Tirar Dado' para jugar."

# Mostrar el tablero y los mensajes
if st.session_state.tablero:
    st.session_state.tablero.graficar()
    st.pyplot(st.session_state.tablero.fig)
    st.write(st.session_state.mensaje)

    # Botón para tirar el dado
    if st.button("Tirar Dado"):
        st.session_state.mensaje = st.session_state.tablero.jugar_turno()
        st.session_state.tablero.graficar()
        st.pyplot(st.session_state.tablero.fig)
        st.write(st.session_state.mensaje)
else:
    st.write(st.session_state.mensaje)