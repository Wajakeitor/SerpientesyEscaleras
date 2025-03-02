import numpy as np
import matplotlib.patches as patches

from Clases.casilla import Casillas

def estrella(x, y, largo, alto, color, ax):
    """Dibuja una estrella de 5 puntas dentro del rectángulo definido"""
    puntos = [
        (x + largo * 0.5, y + alto * 1.0),  # Punta superior
        (x + largo * 0.61, y + alto * 0.65),
        (x + largo * 1.0, y + alto * 0.65),
        (x + largo * 0.68, y + alto * 0.40),
        (x + largo * 0.79, y + alto * 0.0),
        (x + largo * 0.5, y + alto * 0.25),
        (x + largo * 0.21, y + alto * 0.0),
        (x + largo * 0.32, y + alto * 0.40),
        (x + largo * 0.0, y + alto * 0.65),
        (x + largo * 0.39, y + alto * 0.65),
    ]
    star = patches.Polygon(puntos, closed=True, color=color)
    ax.add_patch(star)

def pentagono(x, y, largo, alto, color, ax):
    """Dibuja un pentágono regular"""
    angulos = np.linspace(0, 2 * np.pi, 6)[:-1]  # 5 lados
    puntos = [(x + largo * 0.5 + largo * 0.4 * np.cos(a), y + alto * 0.5 + alto * 0.4 * np.sin(a)) for a in angulos]
    ax.add_patch(patches.Polygon(puntos, closed=True, color=color))

def triangulo(x, y, largo, alto, color, ax):
    """Dibuja un triángulo equilátero"""
    puntos = [
        (x + largo * 0.5, y + alto),  # Vértice superior
        (x, y),  # Esquina inferior izquierda
        (x + largo, y)  # Esquina inferior derecha
    ]
    ax.add_patch(patches.Polygon(puntos, closed=True, color=color))

def rombo(x, y, largo, alto, color, ax):
    """Dibuja un rombo"""
    puntos = [
        (x + largo * 0.5, y + alto),  # Arriba
        (x + largo, y + alto * 0.5),  # Derecha
        (x + largo * 0.5, y),  # Abajo
        (x, y + alto * 0.5)  # Izquierda
    ]
    ax.add_patch(patches.Polygon(puntos, closed=True, color=color))

def hexagono(x, y, largo, alto, color, ax):
    """Dibuja un hexágono regular"""
    angulos = np.linspace(0, 2 * np.pi, 7)[:-1]  # 6 lados
    puntos = [(x + largo * 0.5 + largo * 0.4 * np.cos(a), y + alto * 0.5 + alto * 0.4 * np.sin(a)) for a in angulos]
    ax.add_patch(patches.Polygon(puntos, closed=True, color=color))


class Piezas:
    def __init__(self, CasillaPos: Casillas, NumeroFigura):
        self.casilla: Casillas = CasillaPos
        self.Figura = NumeroFigura

    def graficar(self, ax):
        ancho = self.casilla.alto/3

        if self.Figura == 1:
            estrella(self.casilla.xinicio+0.1*self.casilla.largo,
                     self.casilla.yinicio+0.1*self.casilla.alto,
                     ancho, ancho, "gold", ax)

        if self.Figura == 2:
            pentagono(self.casilla.xinicio+0.9*self.casilla.largo-ancho,
                      self.casilla.yinicio+0.1*self.casilla.alto,
                      ancho, ancho, "blue", ax)
            
        if self.Figura == 3:
            triangulo(self.casilla.xinicio+0.1*self.casilla.largo,
                      self.casilla.yinicio+0.9*self.casilla.alto-ancho,
                      ancho, ancho, "red", ax)
            
        if self.Figura == 4:
            rombo(self.casilla.xinicio+0.9*self.casilla.largo-ancho,
                  self.casilla.yinicio+0.9*self.casilla.alto-ancho,
                  ancho, ancho, "green", ax)

        if self.Figura == 5:
            hexagono(self.casilla.xinicio+0.5*self.casilla.largo-ancho/2,
                     self.casilla.yinicio+0.5*self.casilla.alto-ancho/2,
                     ancho, ancho, "purple", ax)