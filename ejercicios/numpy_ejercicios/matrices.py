"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear una matriz 5x5 con números aleatorios desde 0 hasta 10 en Numpy.

0) Guardala en un .txt donde cada elemento esten separado por guión y
recuperarla

Ejemplo:

1-4-6-5-6
2-4-6-5-6
1-4-6-5-6
1-4-6-5-6
1-4-6-5-6
2-1-6-5-6

1) Muestre el promedio general de toda la matriz.
2) Muestre el promedio de cada columna.
3) Muestre la mediana de cada columna.
4) Muestre la desviación estándar de cada fila.
5) Muestre la cantidad de valores mayores al promedio general.
6) Muestre todas las columnas en las que todos sus valores sean menores
    al promedio general.
"""
import numpy as np

matriz = np.random.randint(0, 10, size=(5, 5))

with open("matriz.txt", "w") as archivo:
    for fila in matriz:
        for i, columna in enumerate(fila):
            if i == 4:
                archivo.write(str(columna))
            else:
                archivo.write(str(columna) + "-")
        archivo.write("\n")

with open("matriz.txt", "r") as archivo:
    matriz = []
    for fila in archivo.readlines():
        fila = fila.replace("\n", "")
        matriz.append(list(map(int, fila.split("-"))))

matriz = np.array(matriz)

print(f"Promedio general: {np.mean(matriz)}")
print(f"Promedio por columna: {np.mean(matriz, axis=0)}")
print(f"Mediana por columna: {np.median(matriz, axis=0)}")
print(f"Desviación estándar por fila: {np.std(matriz, axis=1)}")
print(
    f"Cantidad de valores mayores al promedio general: "
    f"{np.sum(matriz > np.mean(matriz))}"
)
print(
    f"Columnas con todos menores al promedio general: "
    f"{np.where(matriz < np.mean(matriz))}"
)
