"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Leer una palabra N y dependiendo de la cantidad de letras que tenga, retornar
la palabra en un formato específico. Si la palabra tiene 5 letras o menos,
retornar la palabra en mayúsculas. Si la palabra tiene más de 5 letras,
retornar la palabra en minúsculas.

Ejemplo 1
Input
N: hola
Output
HOLA

Ejemplo 2
Input
N: Python
Output
python

"""

N = input()
print(N.upper() if len(N) <= 5 else N.lower())
