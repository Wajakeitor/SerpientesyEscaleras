from Clases.casilla import Casillas
import matplotlib.pyplot as plt
import math

class Tableros:
    def __init__(self, numeroCasillas=30):
        self.CantidadCasillas = numeroCasillas
        self.CasillasPorFila = int(math.ceil(numeroCasillas**(1/2)))
        self.crear_casillas()

    def crear_casillas(self):
        # Calcular el ancho total ocupado y el tamaño de cada casilla
        TamañoCasilla = 100 / self.CasillasPorFila

        # Calcular el largo de la primer y última casilla
        salto1, salto2 = 0,0
        if self.CantidadCasillas < self.CasillasPorFila**2:
            relleno = self.CasillasPorFila**2 - self.CantidadCasillas
            PrimerLargo = math.floor(relleno/2)
            SegundoLargo = math.ceil(relleno/2)

            salto1, salto2 = PrimerLargo, SegundoLargo

        self.casillas = []
        for i in range(self.CasillasPorFila):
            for j in range(self.CasillasPorFila):
                casilla = Casillas(tipoCasilla=0,
                                   numero=i+1 + j*self.CasillasPorFila,
                                   xinicio= 0 + i * TamañoCasilla,
                                   yinicio= 0 + j * TamañoCasilla,
                                   largo=TamañoCasilla, alto=TamañoCasilla)
                self.casillas.append(casilla)

    def graficar(self):
        fig, ax = plt.subplots(figsize=(9, 9))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xticks([])
        ax.set_yticks([])

        for casilla in self.casillas:
            casilla.graficar(ax)

        self.fig = fig