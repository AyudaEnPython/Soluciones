"""
Abra el archivo romeo.txt y léalo línea por línea. Para cada línea,
divídala en una lista de palabras usando el método split (). El
programa debe construir una lista de palabras. Para cada palabra en
cada línea, verifique si la palabra ya está en la lista y, si no,
añádala a la lista. Cuando el programa se complete, ordene e imprima
las palabras resultantes en orden alfabético.
"""
resultado = []
with open("Soluciones/py4e/romeo.txt") as f:
    for linea in f:
        for palabra in linea.split():
            if palabra not in resultado:
                resultado.append(palabra)

print(sorted(resultado))