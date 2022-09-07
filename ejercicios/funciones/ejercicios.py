"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

- Escribir una función que reciba un número y determine si es un número
    primo.
- Escriba una función para sumar los cubos de los primeros n números
    naturales.
- Escriba una función recursiva para calcular la suma de los cubos de
    los primeros números naturales.
- Escriba una función recursiva para contar en cuantos intentos se puede
    adivinar el número de un dado.
- Escriba una función recursiva con el nombre para obtener el n-ésimo
    término de la secuencia de Fibonacci.
"""

# 1
f = lambda n: n > 1 and not any(n % i == 0 for i in range(2, int(n**0.5) + 1))  # noqa: E731, E501

# 2
f = lambda n: sum(i ** 3 for i in range(1, n + 1))  # noqa: E731, E501

# 3
f = lambda n: 1 if n == 1 else n ** 3 + f(n - 1)  # noqa: E731, E501

# 4
f = lambda n: 1 if n == 1 else 1 + f(n - 1)  # noqa: E731, E501

# 5
f = lambda n: n if n <= 1 else f(n-1) + f(n-2)  # noqa: E731, E501
