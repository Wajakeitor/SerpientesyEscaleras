from Clases.casilla import Casillas
import matplotlib.pyplot as plt
import math

class Tableros:
    def __init__(self, numeroCasillas=30):
        self.CantidadCasillas = numeroCasillas + 1
        self.CasillasPorFila = math.ceil((numeroCasillas+1)**(1/2))
        self.crear_casillas()

    def crear_casillas(self):
        # Calcular el ancho total ocupado y el tamaño de cada casilla
        TamañoCasilla = 100 / self.CasillasPorFila

        # Calcular el largo de la primer y última casilla
        salto1, salto2 = 0,0
        PrimerLargo, SegundoLargo = 0, 0
        if self.CantidadCasillas < self.CasillasPorFila**2:
            relleno = self.CasillasPorFila**2 - self.CantidadCasillas
            PrimerLargo = math.floor(relleno/2) * TamañoCasilla
            SegundoLargo = math.ceil(relleno/2) * TamañoCasilla
            print(relleno, PrimerLargo, SegundoLargo)

        # Plotear la Primer Casilla
        self.casillas = []
        casilla = Casillas(tipoCasilla=0,
                            numero = 0,
                            xinicio= 0,
                            yinicio= 0,
                            largo= PrimerLargo + TamañoCasilla,
                            alto= TamañoCasilla,
                            color="black")
        self.casillas.append(casilla)

        # Plotear Casillas
        NumeroCasilla = 1
        yindice = 0 if PrimerLargo + TamañoCasilla < 100 else 1
        xpos = PrimerLargo + TamañoCasilla if PrimerLargo + TamañoCasilla < 100 else 100 - TamañoCasilla
        while(NumeroCasilla < self.CantidadCasillas-1):
            casilla = Casillas(tipoCasilla=0,
                                numero = NumeroCasilla,
                                xinicio= xpos,
                                yinicio= yindice*TamañoCasilla,
                                largo=TamañoCasilla, alto=TamañoCasilla)
            self.casillas.append(casilla)

            if xpos + TamañoCasilla*(-1)**(yindice) < 99 and xpos + TamañoCasilla*(-1)**(yindice) > -1: # Previniendo un error de redondeo
                xpos += TamañoCasilla*(-1)**(yindice)
            else:
                yindice +=1
            
            NumeroCasilla+=1
        
        # Plotear la Última Casilla
        if (-1)**yindice == -1:
            xpos = xpos + (SegundoLargo)*(-1)**(yindice)
        casilla = Casillas(tipoCasilla=0,
                            numero = NumeroCasilla,
                            xinicio= xpos,
                            yinicio= yindice*TamañoCasilla,
                            largo= SegundoLargo + TamañoCasilla,
                            alto= TamañoCasilla,
                            color="black")
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