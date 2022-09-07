"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. Escribir el código necesario para crear un vector (Array Numpy) con
    los siguientes valores:
    [1 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]
2. ¿Que biblitecas tenemos que importar para poder hacer esta operación?
3. ¿Qué tipo de datos podríamos usar? ¿Coma flotante, enteros texto?
    ¿Cualquiera de los anteriores, ninguno de los anteriores, solo
    alguno de las anteriores? Justificar las respuestas.
4. ¿Qué valores han de tomar A, B y C para que las siguientes lineas de
    código produzcan un vector similar al anterior? ¿Por qué?
    A =
    B =
    C =
    V = A + np.arange(B) * C
"""
import numpy as np  # respuesta 2

arr = np.arange(1, 2, 0.1)  # respuesta 1

# respuesta 3: Todas las anteriores, se usara un tipo específico dependiendo
#              del problema a solucionar.

# respuesta 4:
A = 1      # suma 1 a cada elemento del arreglo
B = 10     # construye el arreglo [0, 1, 2... 9]
C = 0.1    # multiplica por 0.1 a cada elemento arreglo
V = A + np.arange(B) * C

print(arr, V)
print(np.allclose(arr, V))
