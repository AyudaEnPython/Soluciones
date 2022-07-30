"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. Construya un programa en Python tal que, dado como datos la base y
la altura de un rectángulo, calcule el perímetro y la superficie de
este.

2. Elaborar un algoritmo que permita ingresar el número de partidos
ganados, perdidos y empatadas, por ABC club en el torneo apertura, se
debe mostrar su puntaje total, teniendo en cuenta que por cada partido
ganado obtendrá 3 puntos, empatado 1 y perdido 0 puntos.

3. Dado el sueldo de un trabajador, aplique un aumento del 15% si su
sueldo es inferior a $1000. Imprima el sueldo que percibirá.

4. Se desea leer por teclado un número comprendido entre 0 y 10 (
inclusive) y se desea visualizar si el número es par o impar.

5. Modifique el programa anterior para que se puedan ingresar varios
números diciendo si cada uno de ellos es par o no. La ejecución del
programa finalizará cuando se ingrese un 0 (cero).

6. Modifique el punto 5 para que aparte de hacer lo que ya hace, me
informe al final del proceso cuántos números fueron pares, cuántos
impares y cuántos números se ingresaron en total.

7. Ingresar por teclado 100 números enteros y calcular cúantos de ellos
son pares. Se debe imprimir el resultado de la suma de los pares y el
resultado de la suma de los impares.

8. Escribir un programa que imprima los 10 primeros números pares
comenzando por el 2 e imprima también sus respectivos valores elevados
al cuadrado y al cubo. Por ejemplo: valor: 2, cuadrado: 4, cubo. 8;
valor: 5, cuadrado: 16, cubo: 64...
"""
# --------------------------------------------------------- Ejercicio 1
b = float(input("Base del rectángulo: "))
h = float(input("Altura del rectángulo: "))
print(f"Perímetro del rectángulo: {(b + h) * 2}")
print(f"Superficie del rectángulo: {b * h}")

# --------------------------------------------------------- Ejercicio 2
ganados = int(input("Ingrese el número de partidos ganados: "))
_ = int(input("Ingrese el número de partidos perdidos: "))
empatados = int(input("Ingrese el número de partidos empatados: "))
print(f"Puntaje total: {(ganados * 3) + (empatados * 1)}")

# --------------------------------------------------------- Ejercicio 3
sueldo = float(input("Sueldo base: "))
if sueldo < 1000:
    sueldo *= 1.15
print(f"Sueldo a percibir: {sueldo}")

# --------------------------------------------------------- Ejercicio 4
while True:
    n = int(input("Ingrese un número entero entre 0 y 10: "))
    if 0 < n <= 10:
        if n % 2 == 0:
            print(f"{n} es par.")
        else:
            print(f"{n} es impar.")
        break

# --------------------------------------------------------- Ejercicio 5
while True:
    n = int(input("Ingresar un número: "))
    if n == 0:
        break
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")

# --------------------------------------------------------- Ejercicio 6
pares = 0
impares = 0
total = 0
while True:
    n = int(input("Ingresar un número: "))
    if n == 0:
        break
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1
    total += 1
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Total: {total}")

# --------------------------------------------------------- Ejercicio 7
pares = 0
impares = 0
i = 0
for i in range(100):
    n = int(input(f"[{i+1}] Ingresar un número: "))
    if n % 2 == 0:
        i += 1
        pares += n
    else:
        impares += n
print(f"Cantidad de pares: {i}")
print(f"Suma de pares: {pares}")
print(f"Suma de impares: {impares}")

# --------------------------------------------------------- Ejercicio 8
for i in range(1, 11):
    print(f"valor: {i * 2}, cuadrado: {(i * 2) ** 2}, cubo: {(i * 2) ** 3}")
