"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

centimetros = int(input("Ingrese los centímetros: "))
metros = centimetros / 100
yardas = metros / 0.9144
pies = yardas / 3
pulgadas = pies / 12

print(f"{centimetros} cm = {yardas:.02f} yd")
print(f"{centimetros} cm = {metros:.02f} m")
print(f"{centimetros} cm = {pies:.02f} p")
print(f"{centimetros} cm = {pulgadas:.02f} pulgadas")
