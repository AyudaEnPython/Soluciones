"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
temp = "Viña del Mar:9:26,Valparaiso:10:24,Quilpe:7:30,Olmue:5:29,Limache:9:23,Villa Alemana:9:22"

temp = temp.split(",")
for dato in temp:
    dato = dato.split(":")
    if int(dato[2]) > 25:
        print(f"{dato[0]}: min {dato[1]}, max {dato[2]}")