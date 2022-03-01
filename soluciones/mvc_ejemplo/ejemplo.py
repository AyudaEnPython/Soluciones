"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from controllers import Controlador
from models import Modelo
from views import Vista


def main():
    app = Controlador(Modelo(), Vista())
    print("Numeros: ")
    app.numeros()
    print("Pares: ")
    app.pares()
    print("Impares: ")
    app.impares()


if __name__ == '__main__':
    main()
