"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar 2 matrices por teclado, de la matriz 1 imprimir la diagonal
principal. De la matriz 2 sacar el promedio total de las filas y
columnas.

NOTE: Se opta por modificar la entrada.
"""
# ----------------------------------------- imprimir diagonal principal
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(a)):
    print(a[i][i], end=" ")
print()

# ------------------------------ promedio total de las filas y columnas
b = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
]

filas = []
columnas = []
for i in range(len(b)):
    fila_promedio = 0
    columna_promedio = 0
    for j in range(len(b[0])):
        fila_promedio += b[i][j]
        columna_promedio += b[j][i]
    filas.append(fila_promedio/len(b[0]))
    columnas.append(columna_promedio/len(b[0]))
print(filas)
print(columnas)
