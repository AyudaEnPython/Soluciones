"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import float_input, text_align


def mostrar(s, x):
    text_align(f"Área de {s}: {x:.2f}")


def main():
    P, C, S, M = .25, .4, .2, .15
    d = float_input("Ingresar donación: ", min=0, lang="es")
    p = d * P
    s = d * S
    m = (p + s) * M
    c = (m + s) * C
    r = d - (p + c + m + s)
    mostrar("Producción", p)
    mostrar("Contabilidad", c)
    mostrar("Marketing", m)
    mostrar("Soporte", s)
    mostrar("Recursos Humanos", r)


if __name__ == "__main__":
    main()
