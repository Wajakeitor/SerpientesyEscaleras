import streamlit as st
import math


st.title("Serpientes y Escaleras")

columnas = st.columns(5)

with columnas[0]:
    casillas = st.number_input("Cantidad de Casillas en el juego.", min_value=10, value=30, step=1)

# La cantidad de escaleras y serpientes se limita a piso(casillas / 6)
max_escaleras_serpientes = math.floor(casillas / 6)

with columnas[1]:
    escaleras = st.number_input("Cantidad de Escaleras", min_value=0, max_value=max_escaleras_serpientes, value=1, step=1)

with columnas[2]:
    serpientes = st.number_input("Cantidad de Serpientes", min_value=0, max_value=max_escaleras_serpientes, value=1, step=1)

with columnas[3]:
    personajes = st.number_input("Cantidad de Personajes", min_value=1, max_value=5, value=4, step=1)

with columnas[4]:
    personajes_humanos = st.number_input("Cantidad de Personajes Humanos", min_value=1, max_value=personajes, value=2, step=1)

st.write("  ")

columnas = st.columns((1,5))
with columnas[0]:

    # Mostrar los valores seleccionados
    st.markdown(f"Cantidad de Casillas: {casillas}")
    st.markdown(f"Cantidad de Escaleras: {escaleras}")
    st.markdown(f"Cantidad de Serpientes: {serpientes}")
    st.markdown(f"Cantidad de Personajes: {personajes}")
    st.markdown(f"Cantidad de Personajes Humanos: {personajes_humanos}")

with columnas[1]:
    st.markdown(f"# ¡Bienvenido al Juego de Serpientes y Escaleras!")
    st.markdown(f"En este juego clásico, los jugadores deben avanzar a través de un tablero de casillas, evitando las **serpientes** que los harán retroceder y aprovechando las **escaleras** que los impulsarán hacia adelante.")
    st.markdown("## Reglas Básicas:")
    st.markdown("- **Casillas**: El tablero consta de un número determinado de casillas que los jugadores deben recorrer.\n\
- **Escaleras**: Las escaleras te permiten avanzar rápidamente a una casilla más alta.\n\
- **Serpientes**: Si caes en una casilla con una serpiente, retrocederás y perderás tiempo.")