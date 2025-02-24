import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Casillas:
    """_summary_
    """    
    def __init__(self, numero, tipoCasilla, xinicio, yinicio, largo, alto, fila, grosor=2, color = "white"):
        
        self.numero = numero
        self.tipoCasilla = tipoCasilla
        self.largo = largo
        self.alto = alto
        self.grosor = grosor
        self.xinicio = xinicio
        self.yinicio = yinicio
        self.fila = fila
        self.color = color

    def graficar(self, ax):
        MarcoCasilla = patches.Rectangle(
            (self.xinicio+0.1*self.largo, self.yinicio+0.1*self.alto),                               # Coordenas de inicio
            self.largo*0.8, self.alto*0.8,                                      # Largo y alto de la casilla
            edgecolor='black', facecolor=self.color, linewidth=self.grosor # Otras propiedades: Color de borde, fondo y grosor del borde
        )
        ax.add_patch(MarcoCasilla)

        MarcoNumero_Alto = self.alto / 4  # Una ___ parte de la altura de la casilla
        MarcoNumero = patches.Rectangle(
            (self.xinicio+0.1*self.largo, self.yinicio+0.9*self.alto - MarcoNumero_Alto),
            MarcoNumero_Alto, MarcoNumero_Alto, 
            edgecolor='black', facecolor=self.color, linewidth=2
        )
        ax.add_patch(MarcoNumero)

        # Colocar el número de la casilla en la esquina superior izquierda
        ax.text(self.xinicio+0.1*self.largo + MarcoNumero_Alto / 2,
                self.yinicio+0.9*self.alto  - MarcoNumero_Alto / 2,
                str(self.numero), color='black', ha='center', va='center')
