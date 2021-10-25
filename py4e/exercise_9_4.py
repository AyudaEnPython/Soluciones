"""
Escribe un programa para leer mbox-short.txt y encuentra quién ha
enviado la mayor cantidad de mensajes de correo. El programa busca
líneas 'De' y toma la segunda palabra de esas líneas como la persona
que envió el correo. El programa crea un diccionario Python que asigna
la dirección de correo del remitente a un recuento de la cantidad de
veces que aparece en el archivo. Después de que se produce el
diccionario, el programa lee a través del diccionario utilizando un
bucle máximo para encontrar la dirección que más envíos tuvo.
"""

# archivo = input("Nombre de archivo: ")
archivo = "py4e/mbox-short.txt"

f = open(archivo)
for linea in f:
    if linea.startswith("From "):
        print(linea.split()[1])