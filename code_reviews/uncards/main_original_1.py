"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: doesn't solve the problem neither passes the tests.
"""
def main():

    validos = "kV+*@aAZ1P[]Coler"
    resultado, caracteres1, caracteres2 = "", "", ""

    validar = lambda caracter: caracter in validos

    while True:

        cjugador1 = str(input("J1 Caracter: ")[0])

        if cjugador1 == "x":
            break

        cjugador2 = str(input("J2 Caracter: ")[0])

        # Validamos el caracter, regresa el valor si es valido, si no regresa 0
        U = (0, ord(cjugador1)) [validar(cjugador1)]
        A = (0, ord(cjugador2)) [validar(cjugador2)]

        if U == 0 or A == 0: raise ValueError("Caracteres inválidos")

        caracteres1 += cjugador1
        caracteres2 += cjugador2

        if U == A:
            resultado += "D"
        elif U > A:
            resultado += "U"
        else:
            resultado += "A"

        print("| {:<10} | {:<10} |".format("Entrada", "Salida"))
        print("| {:<10} | {:<10} |".format(caracteres1, resultado))
        print("| {:<10} | {:>10} |".format(caracteres2, " "))

if __name__ == "__main__":
    main()