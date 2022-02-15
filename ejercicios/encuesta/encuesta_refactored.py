"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En estadística, una muestra es un conjunto de observaciones capaz de
proporcionar información similar a una población total.

CASO: La dirección de FACPyA está considerando establecer el uso de
lenguaje inclusivo de forma obligatoria, para alumnos y maestros,
siempre y cuando la mayoría esté de acuerdo.

Hay 16,420 alumnos en FACPyA, y levantar una encuesta tiene un costo
de $4.20 por persona. Esto hace que levantar la encuesta tenga un costo
total de $68,964.

La dirección desea saber cuántas encuestas debe levantar, para que los
resultados sean confiables en un 95%, con un margen de error de 3%.

Esta encuesta nunca se había hecho, por lo cual la probabilidad de los
eventos es del 50%

Para el cálculo de la muestra utilizaremos la siguiente fórmula:

n = ((Z*Z)*(p*q)*N)/((N*(E*E)+((Z*Z)*(p*q)))

Donde:

Z es el coeficiente de confianza. Lo más común es 90%=1.645, 95%=1.96,
    99%=2.576
p es la probabilidad de que ocurra un evento; si no se conoce,
    típicamente es del 50% (0.5).
q es la probabilidad de que no ocurra el evento; es (1-p)
E es el error máximo aceptado; típicamente, es el 5% (0.05)
N es el tamaño de la población.
"""
# pip install prototools
from prototools import float_input, menu_input

IC = {
    "A": 1.645,
    "B": 1.96,
    "C": 2.576
}


def main():
    n_ = float_input("Ingresar el tamaño de la población: ", min=0, lang="es")
    print("Que intervalo de confianza desea utilizar?")
    z = menu_input(tuple(IC.keys()), lang="es")
    p = float_input(
        "Ingresar la probabilidad de ocurrencia: ",
        blank=True, min=0, max=1, lang="es",
    )
    e = float_input("Ingresar el margen de error: ",
        blank=True, gt=0, lt=1, lang="es"
    )
    
    z = IC[z]
    p = 0.5 if p == "" else p
    q = 1 - p
    e = 0.05 if e == "" else e
    n = ((z**2) * (p*q) * n_) / ((n_ * (e**2) + ((z**2) * (p*q))))
    
    print(f"Para una poblacion de {n_} la muestra es {n}")


if __name__ == "__main__":
    main()
