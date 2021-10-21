"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solución completa en:
https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/palabras_largas.py
"""

# cadena = input("Ingrese una cadena: ")
cadena = "uno dos tres cuatro   cinco"
entero = 6
respuesta = "No hay palabras largas"
cadena = cadena.strip()
lista_cadena = cadena.split(" ")
lista_largo = []
largo = 0

for i in lista_cadena:
    largo = len(i.strip())
    if largo != 0:
        lista_largo.append(largo)

for i in lista_largo:
    if entero < i:
        respuesta = "Hay palabras largas"

print("respuesta: {}".format(respuesta))