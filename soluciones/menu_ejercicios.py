"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1) Secuencia Fibonacci
https://github.com/.../main/soluciones/serie_fibonacci.py
2) Sumatoria primos
https://github.com/.../main/soluciones/sumatoria_primos.py
3) Números primos gemelos
https://github.com/.../main/soluciones/primos_gemelos.py
4) Máximo común divisor (MCD)
https://github.com/.../Soluci.../blob/main/soluciones/mcd.py
5) Centro meteorológico
https://github.com/.../ejercicios/promedio_temperaturas.py
"""
# pip install prototools
from prototools import Menu

import serie_fibonacci, sumatoria_primos, primos_gemelos, mcd, promedio_temperaturas


def main():
    menu = Menu()
    menu.add_options(
        ("Secuencia Fibonacci", serie_fibonacci.main_),
        ("Sumatoria primos", sumatoria_primos.main_),
        ("Primos gemelos", primos_gemelos.main_),
        ("Máximo común divisor (MCD)", mcd.main_),
        ("Centro meteorológico", promedio_temperaturas.main_),
    )
    menu.run()


if __name__ == "__main__":
    main()
