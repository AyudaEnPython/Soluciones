"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ejercicios usando list comprehension
"""

# Imprimir "par" o "impar" para los números 1 al 10, usando list comprehension
# NOTA: El enunciado del ejercicio NO ES CLARO!
print(*[f"{n} es par" if n % 2 == 0 else f"{n} es impar" for n in range(1, 11)], sep=", ")

# Del 1 al 100 imprimir solo los números divisibles entre 5, usando list comprehension
print(*[n for n in range(1, 101) if n % 5 == 0], sep=" - ")

# De la frase de abajo extraer mayúsculas y minúsculas y eliminar los duplicados
# frase: "Existen algunas MAYÚSCULAS, no es cierto?"
# NOTA: El enunciado del ejercicio NO ES CLARO!
print(set([c for c in "Existen algunas MAYÚSCULAS, no es cierto?" if c.isupper()]))