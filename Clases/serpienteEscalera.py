import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Clases.casilla import Casillas

class SerpientesEscaleras:
    def __init__(self, tipo, Casillainicio: Casillas, Casillafinal:Casillas):
        self.tipo = tipo
        self.CasillaInicio = Casillainicio
        self.CasillaFinal = Casillafinal
        self.CasillaInicio.tipoCasilla = Casillafinal

    def graficar(self, ax):
        color = 'green' if self.tipo == 1 else 'red'
    
        # Crear una línea como parche (para que no se dibuje encima de los rectángulos)
        linea = patches.FancyArrow(
            self.CasillaInicio.xCentro, self.CasillaInicio.yCentro,
            self.CasillaFinal.xCentro - self.CasillaInicio.xCentro,
            self.CasillaFinal.yCentro - self.CasillaInicio.yCentro,
            width=0.6, color=color, length_includes_head=True
        )
        
        ax.add_patch(linea) 