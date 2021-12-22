"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1) Secuencia Fibonacci
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/serie_fibonacci.py
2) Sumatoria primos
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/sumatoria_primos.py
3) Números primos gemelos
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/primos_gemelos.py
4) Máximo común divisor (MCD)
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/mcd.py
5) Centro meteorológico
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/promedio_temperaturas.py
"""
# pip install prototools
# from prototools import Menu

import serie_fibonacci, sumatoria_primos, primos_gemelos, mcd, promedio_temperaturas


# def main():
#     menu = Menu()
#     menu.add_options(
#         ("Secuencia Fibonacci", serie_fibonacci.main_),
#         ("Sumatoria primos", sumatoria_primos.main_),
#         ("Primos gemelos", primos_gemelos.main_),
#         ("Máximo común divisor (MCD)", mcd.main_),
#         ("Centro meteorológico", promedio_temperaturas.main_),
#     )
#     menu.run()


def menu():
    print("Menu")
    print("1) Secuencia Fibonacci")
    print("2) Sumatoria primos")
    print("3) Primos gemelos")
    print("4) Máximo común divisor (MCD)")
    print("5) Centro meteorológico")
    print("6) Salir")


def main_alt():
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            serie_fibonacci.main_()
        elif opcion == "2":
            sumatoria_primos.main_()
        elif opcion == "3":
            primos_gemelos.main_()
        elif opcion == "4":
            mcd.main_()
        elif opcion == "5":
            promedio_temperaturas.main_()
        elif opcion == "6":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    # main()
    main_alt()