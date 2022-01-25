"""
Escribe un programa para leer mbox-short.txt y encuentra quién ha
enviado la mayor cantidad de mensajes de correo. El programa busca
líneas 'De' y toma la segunda palabra de esas líneas como la persona
que envió el correo. El programa crea un diccionario Python que asigna
la dirección de correo del remitente a un recuento de la cantidad de
veces que aparece en el archivo. Después de que se produce el
diccionario, el programa lee a través del diccionario utilizando un
bucle máximo para encontrar la dirección que más envíos tuvo.

    Salida deseada
    +------------------+
    | cwen@iupui.edu 5 |
    +------------------+
"""

archivo = input("Nombre de archivo: ") # data/mbox-short.txt
f = open(archivo)
correos = []
for linea in f:
    if linea.startswith("From "):
        correos.append(linea.split()[1])
f.close()
resultado = dict([(i, correos.count(i)) for i in correos])

mayor, correo = 0, None
for k, v in resultado.items():
    if v > mayor:
        correo, mayor = k, v
print(correo, mayor)