import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Casillas:
    """_summary_
    """    
    def __init__(self, numero, tipoCasilla, xinicio, yinicio, largo, alto, grosor=2):
        
        self.numero = numero
        self.tipoCasilla = tipoCasilla
        self.largo = largo
        self.alto = alto
        self.grosor = grosor
        self.xinicio = xinicio
        self.yinicio = yinicio

    def graficar(self, ax):
        MarcoCasilla = patches.Rectangle(
            (self.xinicio, self.yinicio),                               # Coordenas de inicio
            self.largo, self.alto,                                      # Largo y alto de la casilla
            edgecolor='black', facecolor='white', linewidth=self.grosor # Otras propeidades
        )
        ax.add_patch(MarcoCasilla)

        MarcoNumero_Alto = self.alto / 4  # Una ___ parte de la altura de la casilla
        MarcoNumero = patches.Rectangle(
            (self.xinicio, self.yinicio + self.alto - MarcoNumero_Alto),
            MarcoNumero_Alto, MarcoNumero_Alto, 
            edgecolor='black', facecolor='white', linewidth=2
        )
        ax.add_patch(MarcoNumero)

        # Colocar el número de la casilla en la esquina superior izquierda
        ax.text(self.xinicio + MarcoNumero_Alto / 2,
                self.yinicio + self.alto - MarcoNumero_Alto / 2,
                str(self.numero), color='black', ha='center', va='center')
