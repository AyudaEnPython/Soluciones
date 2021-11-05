"""
Implementar un algoritmo que reciba números enteros hasta que se
ingrese el valor cero (0) y los guarde en una lista.

- Si el número ingresado ya existe en la lista, se deberá mostar el
    mensaje "El número ya existe".
- Se debe dividir la lista en dos listas, la primera deberá contener
    los pares, y la segunda los números impares.

Algunos ejemplos de diálogo de este programa serían:

    +------------------------------------+
    | Ingrese el número: 18              |
    | Ingrese el número: 17              |
    | Ingrese el número: 10              |
    | Ingrese el número: 8               |
    | Ingrese el número: 9               |
    | Ingrese el número: 7               |
    | Ingrese el número: 5               |
    | Ingrese el número: 14              |
    | Ingrese el número: 6               |
    | Ingrese el número: 17              |
    | El número ya existe!!              |
    | Ingrese el número: 10              |
    | El número ya existe!!              |
    | Ingrese el número: 25              |
    | Ingrese el número: 14              |
    | El número ya existe!!              |
    | Ingrese el número: 0               |
    |                                    |
    | Números pares: [18, 10, 8, 14, 6]  |
    | Números impares: [17, 9, 7, 5, 25] |
    +------------------------------------+
"""

numeros = []

while True:
    n = input("Ingrese el número: ")
    if n == "0":
        break
    try:
        n = int(n)
        if n in numeros:
            print("El número ya existe!!")
        else:
            numeros.append(n)
    except ValueError:
        print("El número debe ser un número entero")
        continue

pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")