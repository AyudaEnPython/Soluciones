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

    Salida deseada
    +-----------------------------------------+
    | Average spam confidence: 0.750718518519 |
    +-----------------------------------------+

No uses la función sum() o una variable llamada "sum" en tu solución.

En http://es.py4e.com/code3/mbox-short.txt puedes descargar los datos
muestra para probar la función, ingrese mbox-short.txt como el nombre
del archivo.
"""

resultado = 0
cantidad = 0
archivo = input("Nombre de archivo: ") # py4e/data/mbox-short.txt
f = open(archivo)
for linea in f:
    if linea.startswith("X-DSPAM-Confidence:"):
        cantidad += 1
        resultado += float(linea[linea.find(":")+1:])
f.close()
print("Average spam confidence:", resultado/cantidad)