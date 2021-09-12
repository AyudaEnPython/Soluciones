"""
sample:
1030
output:
ca

TODO: add description of the exercise, testcases and more solutions.
"""

analizador = {
    "30": "a",
    "55": "b",
    "10": "c",
}

fuente = "1030"
salida = ""

for impar, par in zip(fuente[::2], fuente[1::2]):
    if impar + par in analizador.keys():
        salida += analizador[impar + par]

print(salida)
