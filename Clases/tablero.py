from Clases.casilla import Casillas
from Clases.serpienteEscalera import SerpientesEscaleras
from Clases.pieza import Piezas

import matplotlib.pyplot as plt
import random
import math

import time

class Tableros:
    def __init__(self, numeroCasillas, numeroSerpientes, numeroEscaleras, numeroPiezas):
        self.CantidadCasillas = numeroCasillas + 1
        self.CantidadSerpientes = numeroSerpientes
        self.CantidadEscaleras = numeroEscaleras
        self.CantidadPiezas = numeroPiezas

        self.casillas: list[Casillas] = []
        self.serpientes: list[SerpientesEscaleras] = []
        self.escaleras: list[SerpientesEscaleras] = []
        self.piezas: list[Piezas] = []

        self.CasillasOcupadas: list[int] = []
        self.CasillasPorFila = math.ceil((numeroCasillas+1)**(1/2))
        self.crear_casillas()
        self.crear_serpientes_escaleras()
        self.crear_piezas()

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

        # Plotear la Primer Casilla
        casilla = Casillas(tipoCasilla=0,
                            numero = 0,
                            xinicio= 0,
                            yinicio= 0,
                            largo= PrimerLargo + TamañoCasilla,
                            alto= TamañoCasilla,
                            fila=0,
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
                                largo=TamañoCasilla,
                                alto=TamañoCasilla,
                                fila=yindice,
                                fontsize=20 + 12/(9-4)*(4-self.CasillasPorFila))
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
                            fila= yindice,
                            color="black",
                            final = True)
        self.casillas.append(casilla)

    def CasillasAleatorias(self, minimo, maximo):
        CasillasNoValidas = True
        while CasillasNoValidas:
            final = random.randint(minimo,maximo)
            inicio = random.randint(minimo,maximo)
            if final in self.CasillasOcupadas or inicio in self.CasillasOcupadas:
                continue
            if inicio==final:
                continue
            if final < inicio:
                final, inicio = inicio, final
            if (final-minimo)//self.CasillasPorFila != (inicio-minimo)//self.CasillasPorFila:
                CasillasNoValidas = False
        
        self.CasillasOcupadas.append(final)
        self.CasillasOcupadas.append(inicio)
        
        return final, inicio

    def crear_serpientes_escaleras(self):
        maximo =  self.CantidadCasillas - (self.CasillasPorFila - (math.ceil( (self.CasillasPorFila**2-self.CantidadCasillas)/2)) + 1)
        minimo =  self.CasillasPorFila - (math.floor( (self.CasillasPorFila**2-self.CantidadCasillas)/2) + 1) + 1

        for _ in range(self.CantidadEscaleras):
            final, inicio = self.CasillasAleatorias(minimo, maximo)
            self.escaleras.append(SerpientesEscaleras(1, Casillafinal=self.casillas[final], Casillainicio=self.casillas[inicio]))
        
        for _ in range(self.CantidadSerpientes):
            final, inicio = self.CasillasAleatorias(minimo, maximo)
            self.serpientes.append(SerpientesEscaleras(-1, Casillafinal=self.casillas[inicio], Casillainicio=self.casillas[final]))
        
    def crear_piezas(self):
        for i in range(self.CantidadPiezas):
            self.piezas.append(Piezas(self.casillas[0], i+1))
    
    def avanzar_pieza(self, numeroPieza, avance):
        pieza = self.piezas[numeroPieza]
        posicion_actual = pieza.casilla.numero
        nueva_posicion = min(posicion_actual + avance, self.CantidadCasillas - 1)
        pieza.casilla = self.casillas[nueva_posicion]
        if pieza.casilla.tipoCasilla !=0:
            pieza.casilla = pieza.casilla.tipoCasilla

    def graficar(self):
        fig, ax = plt.subplots(figsize=(9, 9))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xticks([])
        ax.set_yticks([])

        for casilla in self.casillas:
            casilla.graficar(ax)

        for serpiente in self.serpientes:
            serpiente.graficar(ax)

        for escalera in self.escaleras:
            escalera.graficar(ax)

        for pieza in self.piezas:
            pieza.graficar(ax)


        self.fig = fig