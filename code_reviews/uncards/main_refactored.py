"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: There's still more room to refactor.
"""


def comparar(cadena1, cadena2):
    to_ord = lambda s, i: (0, ord(s[i]))[s[i] in "kV+*@aAZ1P[]Coler"]
    resultado = ""
    U = A = h1 = h2 = 0
    for i in range(len(max(cadena1, cadena2))):
        U, A = to_ord(cadena1, i), to_ord(cadena2, i)
        if U > A : h1 += 1
        elif U < A : h2 += 1
        if h1 == h2:
            resultado += "D"
        elif h1 > h2:
            resultado += "U"
        else:
            resultado += "A"
    return resultado


def main():
    cjugador1 = input("J1 Caracter: ")
    cjugador2 = input("J2 Caracter: ")
    print(comparar(cjugador1, cjugador2))


if __name__ == "__main__":
    main()
