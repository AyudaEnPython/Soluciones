# flak8: noqa
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

Z es el coeficiente de confianza. Lo más común es 90%=1.645, 95%=1.96, 99%=2.576
p es la probabilidad de que ocurra un evento; si no se conoce, típicamente es del 50% (0.5).
q es la probabilidad de que no ocurra el evento; es (1-p)
E es el error máximo aceptado; típicamente, es el 5% (0.05)
N es el tamaño de la población.

"""
# Módulo para trabajar con Expresiones Regulares
import re

# Preguntar N
# Es un valor flotante, mayor a cero, no se puede omitir
while True:
    try:
        _N=input(r"Cuál es el tamaño de la población:")
        # Si se omite, toma el valor default
        if (_N==""):
            print("El dato no se puede omitir")
            continue
        # Validar que sea numérico
        N=float(_N)
        # Validar que esté en rango
        if (N<=0):
            print("El dato debe ser mayor a cero")
            continue
    except:
        print("El dato debe ser numérico")
        continue
    else:
        break

# Preguntar Z
# Voy a simular una opción A=90%, B=95%, y C=99%
print("Intervalos de confianza: A=90%, B=95%, y C=99%")
while True:
    confianza=input(r"Qué intervalo de confianza deseas [A, B o C]: ")
    if (confianza==""):
        print("La confianza no se puede omitir")
        continue
    if (not bool(re.match(r"^[ABC]{1}$",confianza))):
        print("Solo se permite A, B, o C")
        continue
    if (confianza=="A"):
        Z=1.645
    if (confianza=="B"):
        Z=1.96
    if (confianza=="C"):
        Z=2.576
    break

# Preguntar p y calcular q
# Es un valor flotante, mayor a cero pero menor a 1, no se puede omitir
while True:
    try:
        _p=input(r"Cuál es la probabilida de que ocurra el evento (omisión=50%):")
        # Si se omite, toma el valor default
        if (_p==""):
            p=0.5
            break
        # Validar que sea numérico
        p=float(_p)
        # Validar que esté en rango
        if (p<=0 or p>=1):
            print("El dato debe estar entre 0 y 1")
            continue
    except:
        print("El dato debe ser numérico")
        continue
    else:
        break

# Preguntar E
# Es un valor flotante, mayor a cero pero menor a 1, no se puede omitir

while True:
    try:
        _E=input(r"Cuál es margen de error (omisión=5%):")
        # Si se omite, toma el valor default
        if (_E==""):
            E=0.05
            break
        # Validar que sea numérico
        E=float(_E)
        # Validar que esté en rango
        if (E<=0 or E>=1):
            print("El dato debe estar entre 0 y 1")
            continue
    except:
        print("El dato debe ser numérico")
        continue
    else:
        break
# Función que calcula q, debe recibir p, que es opcional: si no se le
# proporciona valor, debe valer 0.50
def CalculaQ():
    q=(1-p)

# Función que calcula el tamaño de la muestra, y retorna el resultado.
def ValorMuestra():
    pass

# Calculamos el tamaño de la muestra
n = (((Z*Z)*(p*q)*N)/((N*(E*E))+((Z*Z)*(p*q))))
resultado="Para una población de {0} la muestra es {1}".format(N,n)

# Mostramos el resultado
print(ValorMuestra())

# Se pide:
# a) Hacer que la variable q sea global, para que no marque error.
#       Hacer uso de la variable global, en su caso.
# b) Crear un procedimiento llamado CapturaDatos(), en donde se
#       tenga toda la captura de datos. Esta función no recibe valores,
#       ni retorna valores.
# c) Codificar ValorMuestra(), que debe calcular la muestra, y retornar
#       resultado.
# d) El procedimiento CalculaQ debe tener un argumento, donde se reciba
#       p. El argumento debe ser opcional. Si no se proporciona, es igual a
#       50%.
# e) Crear un procedimiento llamado main(), que actúe como entry point.
