"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar N números por teclado e imprimir solo los números mayores al
último ingresado.
"""


def main():
    cantidad = int(input("Cantidad de números: "))
    numeros = []
    i = 0
    while i < cantidad:
        numeros.append(int(input(f"[{i+1}]> ")))
        i += 1
    i = 0
    while i < len(numeros):
        if numeros[i] > numeros[-1]:
            print(numeros[i])
        i += 1


if __name__ == '__main__':
    main()
