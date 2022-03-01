"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una expresión regular que encuentre los nombres de archivos txt
en la cadena:

- Nombre de archivo txt siempre inicia al principio de la cadena
- Siempre comienzan con una secuencia de 2 o 3 vocales mayúsculas o
    minúsculas (a, e, i, o, u).
- Ellos siempre terminan con el final del txt.

NOTE: El enunciado no esta bien redactado.
"""
import re

ficheros = [
    "aArchivo.txt", "aaa.txt", "123rchivo.txt", "Archivo.txt", "/rchivo.txt",
    "123.txt", "ou24.txt", "aaa.py", "1a2.txt", "ae.txt", "AE.txt", "aE.txt",
]

exp = re.compile(r'^[aeiouAEIOU]{2,3}(.*).txt$')
encontrados = [fichero for fichero in ficheros if exp.match(fichero)]

print(encontrados)
