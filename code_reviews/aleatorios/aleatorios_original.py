"""Solución completa en:
https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/generar_aleatorios.py
"""

import random
def aleat(datos):
    suma=0
    for n in datos:
        suma +=n
    return suma
datos=[]
felo= random.randint(1, 20)
print("El tamaño de la lista es: ",felo )
for n in range(felo):
    crew= random.randint(1, 100)
    datos.append(crew)
#datos= tuple(datos)
print(datos)
SumaT= aleat(datos)
print("La suma  total e s: ", SumaT)