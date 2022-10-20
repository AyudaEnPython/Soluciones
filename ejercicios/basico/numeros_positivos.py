"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solicita "n" datos por el usuario e introducelos en la lista "a", los
números negativos no tomarlo en cuenta.
Al final imprime la lista pero en orden ascendente.

NOTE: Se modifca "n" por "cantidad" y "a" por "numeros".
"""

numeros = []
cantidad = int(input("n: "))
for i in range(cantidad):
    numero = int(input(f"N°{i+1:02} -> "))
    if numero > 0:
        numeros.append(numero)
print(sorted(numeros))
