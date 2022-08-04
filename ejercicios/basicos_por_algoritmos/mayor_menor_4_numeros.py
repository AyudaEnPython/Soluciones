"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Se opta por cambiar algunas cosas para seguir (PEP8).
    Las líneas 39 a 46 están escritas de esa forma para no
    superar el límite de 79 caracteres por línea.
"""

p = int(input("1° Número: "))
q = int(input("2° Número: "))
r = int(input("3° Número: "))
s = int(input("4° Número: "))

mayor = p
menor = p
posicion_mayor = 1
posicion_menor = 1

if q > mayor:
    mayor = q
    posicion_mayor = 2
if q < menor:
    menor = q
    posicion_menor = 2
if r > mayor:
    mayor = r
    posicion_mayor = 3
if r < menor:
    menor = r
    posicion_menor = 3
if s > mayor:
    mayor = s
    posicion_mayor = 4
if s < menor:
    menor = s
    posicion_menor = 4

if p == q == r == s:
    print("Todos los números son iguales.")
else:
    print(
        f"El número mayor es {mayor}"
        f" y fuel el {posicion_mayor}° número ingresado."
    )
    print(
        f"El número menor es {menor}"
        f" y fuel el {posicion_menor}° número ingresado."
    )
