"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa que determine el valor de descuento teniendo en
cuenta el precio, la cantidad y si pertenece o no a la canasta
familiar.

precio > 10_000 -> 5%
precio < 100_000 > 3%
precio = 50_000 -> 7%

cantidad < 10 articulos -> 3%
cantidad > 10 articulos < 100 -> 2%
cantidad >= 100 articulos -> 1%

Si pertenece -> hay descuento
Si no pertenece -> no hay descuento

NOTE: El enunciado original no especifica el tipo de descuento a aplicar.
"""

precio = float(input("Ingrese precio: "))
cantidad = int(input("Ingrese cantidad: "))
canasta_familiar = input("Pertenece a la canasta familiar? (S/N): ").upper()

total = precio * cantidad
descuento = 0

if canasta_familiar == "S":
    if total > 10_000:
        descuento = total * 0.05
    elif total == 50_000:
        descuento = total * 0.07
    elif total < 100_000:
        descuento = total * 0.03

    if cantidad < 10:
        descuento += total * 0.03
    elif cantidad >= 10 and cantidad < 100:
        descuento += total * 0.02
    elif cantidad >= 100:
        descuento += total * 0.01

print(f"Descuento: {descuento}")
print(f"Total: {total - descuento}")
