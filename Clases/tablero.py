from Clases.casilla import Casillas
import matplotlib.pyplot as plt

class Tableros:
    def __init__(self, numeroCasillas=5):
        self.lado_total = 12  # Tamaño del plot
        self.num_casillas = 5
        self.porcentaje_ancho = 1  # Ocupar el 90% del ancho
        self.crear_casillas()

    def crear_casillas(self):
        # Calcular el ancho total ocupado y el tamaño de cada casilla
        ancho_total = self.lado_total * self.porcentaje_ancho  # 7.2
        lado_casilla = ancho_total / self.num_casillas  # 1.44
        x_inicio = (self.lado_total - ancho_total) / 2  # 0.4 (para centrar)

        self.casillas = []
        for i in range(self.num_casillas):
            casilla = Casillas(0,0,x_inicio + i * lado_casilla, 0, lado_casilla, lado_casilla)
            self.casillas.append(casilla)

    def graficar(self):
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, self.lado_total)
        ax.set_ylim(0, self.lado_total)
        ax.set_xticks([])
        ax.set_yticks([])

        for casilla in self.casillas:
            casilla.graficar(ax)

        self.fig = fig