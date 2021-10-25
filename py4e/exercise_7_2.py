"""
Escribir un programa que solicita un nombre de archivo, a continuación,
abre el archivo y lee a través del archivo, en busca de líneas de la
forma:

    +-------------------------------+
    | X-DSPAM-Confidence:    0.8475 |
    +-------------------------------+

Cuenta estas líneas y extrae los valores de coma flotante de cada una
de las líneas y calcula el promedio de esos valores y produce una
salida como se muestra a continuación:

    +-----------------------------------------+
    | Average spam confidence: 0.750718518519 |
    +-----------------------------------------+

No uses la función sum() o una variable llamada "sum" en tu solución.

En http://es.py4e.com/code3/mbox-short.txt puedes descargar los datos
muestra para probar la función, ingrese mbox-short.txt como el nombre
del archivo.
"""
with open("py4e/mbox-short.txt") as f:
    print(f)