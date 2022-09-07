"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calcular el tamaño de la cadena "Esta es una cadena" sin usar la
función len.

TODO: add docstring and tests.
"""


def len_(ss, i=0):
    for _ in ss:
        i += 1
    return i


def len_alt(ss):
    return sum(1 for _ in ss)


print(len_("Esta es una cadena"))  # output 18
print(len_("trabajando.pe"))  # output 13
