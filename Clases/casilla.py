import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Casillas:
    """_summary_
    """    
    def __init__(self, numero, tipoCasilla, xinicio, yinicio, largo, alto, fila, grosor=2, color = "white", final = False, fontsize = 8): 
        self.numero = numero
        self.tipoCasilla = tipoCasilla
        self.largo = largo
        self.alto = alto
        self.grosor = grosor
        self.xinicio = xinicio
        self.yinicio = yinicio
        self.fila = fila
        self.color = color
        self.final = final
        self.fontsize = fontsize
        self.xCentro = xinicio + largo/2
        self.yCentro = yinicio + alto/2

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
        if self.final:
            ax.text(self.xinicio + self.largo/2,
                    self.yinicio + self.alto/2,
                    str("META"), color='white', ha='center', va='center', fontsize=16+0.2*(80-self.numero) )
        else:
            ax.text(self.xinicio+0.1*self.largo + MarcoNumero_Alto / 2,
                    self.yinicio+0.9*self.alto  - MarcoNumero_Alto / 2,
                    str(self.numero), color='black', ha='center', va='center', fontsize = self.fontsize)
