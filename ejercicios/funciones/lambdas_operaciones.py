"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realiza lo siguiente:

- Codifica una función anónima o lambda que sume, reste, multiplique y
    divida 2 números introducidos por el usuario en consola. Deberá
    tener el siguiente comportamiento:

    PROGRAMA QUE REALIZA OPERACIONES CON 2 NÚMEROS

    Entrada:

    Ingresa el primer número: 5
    Ingresa el segundo número: 2

    Salida:

    La suma es: 7
    La resta es: 3
    La multiplicación es: 10
    La división es: 2.5

Nota: Recuerda que la división entre 0 está indeterminada, y esa
    condición la debes de considerar a la hora de resolver el
    problema.
"""

f = lambda x, y: (  # noqa: E731
    ("suma", x + y),
    ("resta", x - y),
    ("multiplicación", x * y),
    ("división", x / y),
)

x = int(input("Ingresa el primer número: "))
y = int(input("Ingresa el segundo número: "))

try:
    for s, v in f(x, y):
        print(f"La {s} es: {v}")
except ZeroDivisionError:
    print("La división entre cero está indefinida")
