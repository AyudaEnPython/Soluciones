"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

ciudades = (
    "Viña del Mar:9:26,Valparaiso:10:24,Quilpe:7:30,Olmue:5:29,"
    "Limache:9:23,Villa Alemana:9:22"
)

for ciudad in ciudades.split(","):
    nombre, minimo, maximo = ciudad.split(":")
    if int(maximo) > 25:
        print(f"{nombre}: min {minimo}, max {maximo}")
