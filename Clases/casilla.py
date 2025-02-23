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
        rect = patches.Rectangle(
            (self.xinicio, self.yinicio), self.largo, self.alto, 
            edgecolor='black', facecolor='white', linewidth=self.grosor
        )
        ax.add_patch(rect)
