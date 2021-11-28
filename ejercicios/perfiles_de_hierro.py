"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una fabrica dedicada a la producción de perfiles de hierro posee una linea 
de producción donde se deben garantizar la calidad de los perfiles, una 
forma de garantizar la calidad es el uso de sensores tipo barrera que
permiten medir la distancia de cada perfil de hierro, para la empresa cada
perfil debe tener entre 1.2 y 1.5 metros y el poceso permite seleccionar la 
cantidad de perfiles que se desean.

Confeccionar un programa que pida ingresar por teclado la cantidad de piezas
a procesar y luego ingrese la longitud de cada perfil; sabiendo que la pieza
cuya longitud esté comprendida en el rango de 1.20 y 1.50 son aptas. Imprimir
por pantalla la cantidad de piezas aptas que hay en el lote.
"""

aptas: int = 0
MINIMO: float = 1.2
MAXIMO: float = 1.5

piezas: int = int(input("Ingresar cantidad de piezas: "))

for n in range(piezas):
    pieza = float(input(f"[Perfil N° {n+1}] Ingresar longitud: "))
    if MINIMO < pieza <= MAXIMO:
        aptas += 1

print(f"En el lote hay {aptas} pieza(s) aptas.")