import streamlit as st
import math
from Clases.tablero import Tableros

# Configurar el ancho de la página
st.set_page_config(layout="wide")

st.title("Serpientes y Escaleras")

columnas = st.columns(5)

with columnas[0]:
    casillas = st.number_input("Cantidad de Casillas en el juego.", min_value=12, max_value=80, value=30, step=1)

# La cantidad de escaleras y serpientes se limita a piso(casillas / 6)
max_escaleras_serpientes = math.floor(casillas / 6)

with columnas[1]:
    escaleras = st.number_input("Cantidad de Escaleras", min_value=0, max_value=max_escaleras_serpientes,
                                value=min(st.session_state.get("escaleras", 1), max_escaleras_serpientes),
                                step=1, key="escaleras")

with columnas[2]:
    serpientes = st.number_input("Cantidad de Serpientes", min_value=0, max_value=max_escaleras_serpientes,
                                 value=min(st.session_state.get("serpientes", 1), max_escaleras_serpientes),
                                 step=1, key="serpientes")

with columnas[3]:
    personajes = st.number_input("Cantidad de Personajes", min_value=1, max_value=5, value=4, step=1)

with columnas[4]:
    personajes_humanos = st.number_input("Cantidad de Personajes Humanos", min_value=1, max_value=personajes,
                                         value=min(st.session_state.get("personajes_humanos", 1), personajes),
                                         step=1, key="personajes_humanos")

columnas = st.columns((1,3))

with columnas[0]:

    # Mostrar los valores seleccionados
    st.markdown(f"Cantidad de Casillas: {casillas}")
    st.markdown(f"Cantidad de Escaleras: {escaleras}")
    st.markdown(f"Cantidad de Serpientes: {serpientes}")
    st.markdown(f"Cantidad de Personajes: {personajes}")
    st.markdown(f"Cantidad de Personajes Humanos: {personajes_humanos}")

with columnas[1]:
    st.markdown(f"# ¡Bienvenido al Juego de Serpientes y Escaleras!\n\
En este juego clásico, los jugadores deben avanzar a través de un tablero de casillas, evitando las **serpientes** que los harán retroceder y aprovechando las **escaleras** que los impulsarán hacia adelante.\n\
## Reglas Básicas:\n\
- **Casillas**: El tablero consta de {casillas} de casillas que los jugadores deben recorrer.\n\
- **Escaleras**: Las escaleras te permiten avanzar rápidamente a una casilla más alta.\n\
- **Serpientes**: Si caes en una casilla con una serpiente, retrocederás y perderás tiempo.")

columnas = st.columns((1,4,4,1))
with columnas[1]:
    st.markdown(f"# Menú de opciones")

with columnas[2]:
    st.markdown(f"# Tablero de Juego")
    tablero = Tableros(numeroCasillas=casillas, numeroEscaleras=escaleras, numeroSerpientes=serpientes)
    tablero.graficar()
    st.pyplot(tablero.fig)
