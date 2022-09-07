"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
N = 10
numeros = []

i = 1
while i <= N:
    try:
        n = int(input(f"[{i}] Ingrese un número: "))
        if 0 <= n <= 36:
            numeros.append(n)
            i += 1
        else:
            print("El número debe estar entre 1 y 36")
    except ValueError:
        print("El valor ingresado no es un número")
        continue

pares = [n for n in numeros if n % 2 == 0 and n != 0]

print(f"Impares: {len([n for n in numeros if n % 2 != 0])}")
print(f"Promedio de pares: {sum(pares) / len(pares)}")
print(f"Numeros entre 13 y 24: {len([n for n in numeros if 13 <= n <= 24])}")
print(f"Mayor: {max(numeros)}")
