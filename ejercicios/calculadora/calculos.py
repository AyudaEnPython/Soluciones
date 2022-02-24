"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from operaciones import suma, resta, multiplicacion, division

OPERADORES = {"+": suma, "-": resta, "*": multiplicacion, "/": division}


def ingresar_numero():
    while True:
        try:
            return float(input("Ingrese un número: "))
        except ValueError:
            print("Error: Tipo de dato no válido")


def ingresar_operador():
    while True:
        operador = input("Ingrese un operador (+, -, *, /): ")
        if operador in OPERADORES:
            return operador
        print("Error: Operador no válido")


def calcular():
    x = ingresar_numero()
    operador = ingresar_operador()
    y = ingresar_numero()
    try:
        resultado = OPERADORES[operador](x, y)
        print(f"{x} {operador} {y} = {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")


def main():
    while True:
        calcular()
        if input("¿Continuar? (s/n): ").lower() == "n":
            break


if __name__ == "__main__":
    main()
