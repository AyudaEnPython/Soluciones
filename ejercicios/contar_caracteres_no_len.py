"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calcular el tamaño de la cadena "Esta es una cadena" sin usar la
función len.
"""


def len_(ss, i=0):
    for s in ss:
        i += 1
    return i


def len_alt(ss, i=0):
    return sum(1 for s in ss)


print(len_("Esta es una cadena")) # output 18
print(len_("trabajando.pe")) # output 13