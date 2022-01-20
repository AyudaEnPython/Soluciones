"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

numeros = []

while True:
    try:
        n = int(input("Ingresar número: "))
        if sum(numeros) <= 1000:
            numeros.append(n)
        else:
            break
    except ValueError:
        print("Error: Debe ingresar un número entero")

multiplos_6 = [n for n in numeros if n % 6 == 0]
suma = sum([n for n in numeros if 1 <= n <= 10])

print(f"Números multiplos de 6: {multiplos_6}")
print(f"Suma de los números entre 1 y 10: {suma}")
