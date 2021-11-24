"""
Abra el archivo romeo.txt y léalo línea por línea. Para cada línea,
divídala en una lista de palabras usando el método split (). El
programa debe construir una lista de palabras. Para cada palabra en
cada línea, verifique si la palabra ya está en la lista y, si no,
añádala a la lista. Cuando el programa se complete, ordene e imprima
las palabras resultantes en orden alfabético.

    Salida deseada
    +---------------------------------------------------------------+
    | ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and',     |
    | 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill',   |
    | 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the',        |
    | 'through', 'what', 'window', 'with', 'yonder']                |
    +---------------------------------------------------------------+

En http://es.py4e.com/code3/romeo.txt puedes descargar los datos de
muestra.
"""

resultado = []
archivo = input("Nombre de archivo: ") # romeo.txt
f = open(archivo)
for linea in f:
    for palabra in linea.split():
        if palabra not in resultado:
            resultado.append(palabra)
f.close()
print(sorted(resultado))