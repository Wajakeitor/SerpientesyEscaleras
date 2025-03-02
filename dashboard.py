import streamlit as st
import math
import random


from Clases.tablero import Tableros

import time

# Configurar el ancho de la página
st.set_page_config(layout="wide")


def crear_tablero():
    st.session_state.tablero = Tableros(
        numeroCasillas=st.session_state.casillas,
        numeroEscaleras=st.session_state.escaleras,
        numeroSerpientes=st.session_state.serpientes,
        numeroPiezas=st.session_state.personajes
    )


st.title("Serpientes y Escaleras")

columnas = st.columns(5)

with columnas[0]:
    casillas = st.number_input("Cantidad de Casillas en el juego.",
                               min_value=12, max_value=80, value=30, step=1, key="casillas")

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
    personajes = st.number_input("Cantidad de Personajes", min_value=1, max_value=5, value=4, step=1, key="personajes")

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
if "turno" not in st.session_state:
    st.session_state.turno = -1
with columnas[1]:
    st.markdown(f"# Menú de opciones")

    if st.button("Generar Nuevo Tablero"):
        # Generar un nuevo tablero y guardarlo en session_state
        st.session_state.tablero = Tableros(
            numeroCasillas=st.session_state.casillas,
            numeroEscaleras=st.session_state.escaleras,
            numeroSerpientes=st.session_state.serpientes,
            numeroPiezas=st.session_state.personajes
        )
        st.session_state.turno = 0
        st.session_state.tablero.graficar()

  
    if st.button("Lanzar Dados", disabled=not (st.session_state.turno>=0 and st.session_state.turno<st.session_state.personajes_humanos)):
        avance = random.randint(1, 6) + random.randint(1, 6)
        st.session_state.tablero.avanzar_pieza(st.session_state.turno, avance)

        st.session_state.turno = (st.session_state.turno + 1)%st.session_state.tablero.CantidadPiezas
        st.session_state.tablero.graficar()

    if st.session_state.turno >= st.session_state.personajes_humanos:
        for i in range(st.session_state.personajes_humanos, st.session_state.tablero.CantidadPiezas):
            avance = random.randint(1, 6) + random.randint(1, 6)
            st.session_state.tablero.avanzar_pieza(st.session_state.turno, avance)
        # Resetear turno a los humanos
        st.session_state.turno = 0
        st.session_state.tablero.graficar()




with columnas[2]:
    st.markdown(f"# Tablero de Juego")
    try:
        st.pyplot(st.session_state.tablero.fig)
    except:
        st.markdown(f"### Crea el tablero de acuerdo a las características que desees al clickear el botón: *Generar Nuevo Tablero*")
    
    
