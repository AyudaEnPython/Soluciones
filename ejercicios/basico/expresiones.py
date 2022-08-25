"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa que despliegue el resultado de

x = (14.8^2 - 6.3^2) / (sqrt(13) + 5)^2
y = 45 * ((288/9.3) - 4.6^2) - 1065 * e^-1.5

Ejemplo de salida
x = 43.2392 y = 203.7148

NOTE: El ejercicio está mal redactado; en 14.8**2, el exponente debería
    ser 3 (14.8**3).
"""
from math import e, sqrt


def main():
    x = (14.8**3 - 6.3**2) / (sqrt(13) + 5)**2
    y = 45 * ((288/9.3) - 4.6**2) - 1065 * e**-1.5
    print(f"x = {round(x, 4)} y = {round(y, 4)}")


if __name__ == "__main__":
    main()
