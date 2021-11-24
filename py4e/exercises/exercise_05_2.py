"""
Escriba un programa que solicite repetidamente números enteros a un
usuario hasta que el usuario ingrese "hecho". Una vez que se ingrese
"hecho", imprima el más grande y el más pequeño de los números. Si el
usuario ingresa algo que no sea un número válido, atrápelo con un
try/except y envíe un mensaje apropiado e ignore el número.

Ingrese 7, 2, bob, 10 y 4 y haga coincidir la salida a continuación:

    Salida deseada
    +-------------------+
    | Valor inválido    |
    | Máximo es 10      |
    | Mínimo es 2       |
    +-------------------+
"""

numeros = []

while True:
    try:
        n = input("> ")
        if n == "hecho":
            break
        numeros.append(int(n))
    except ValueError:
        print("Valor inválido")
        continue

print("Máximo es", max(numeros))
print("Mínimo es", min(numeros))