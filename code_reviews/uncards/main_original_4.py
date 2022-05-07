"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Solves the problem but doesn't pass the tests.
"""
def main():

    validos = "kV+*@aAZ1P[]Coler"
    resultado, historial = "", ""


    def comparar(cadena1, cadena2):
        longitud = len(cadena1) if len(cadena1) < len(cadena2) else len(cadena2)
        resultado = ""
        U, A = 0, 0
        h1, h2 = 0, 0

        for caracter in range(longitud):
            U = (0, ord(cadena1[caracter])) [cadena1[caracter] in validos]
            A = (0, ord(cadena2[caracter])) [cadena2[caracter] in validos]

            if U > A : h1 += 1
            elif U < A : h2 += 1

            if h1 == h2:
                resultado += "D"
            elif h1 > h2:
                resultado += "U"
            else:
                resultado += "A"

        return resultado

    while True:

        cjugador1 = str(input("J1 Caracter: "))

        if cjugador1 == "x":
            break

        cjugador2 = str(input("J2 Caracter: "))

        resultado = comparar(cjugador1, cjugador2)
        historial += "------------------------------\n"
        historial += "| {:<10} | {:<10} |\n".format(cjugador1, resultado)
        historial += "| {:<10} | {:>10} |\n".format(cjugador2, " ")

        print("| {:<10} | {:<10} |\n".format("Entrada", "Salida"))
        print(historial)

if __name__ == "__main__":
    main()