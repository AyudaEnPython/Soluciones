"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: doesn't solve the problem neither passes the tests.
"""
def main():

    validos = "kV+*@aAZ1P[]Coler"
    resultado, historial = "", ""

    def validar(cadena):
        for caracter in range (len(cadena)):
            if cadena[caracter] not in validos:
                raise ValueError("Se a ingresado caracter no válido")
        return True

    def comparar(cadena1, cadena2):
        longitud = len(cadena1) if len(cadena1) < len(cadena2) else len(cadena2)
        resultado = ""
        U, A = 0, 0

        for caracter in range(longitud):
            U += ord(cadena1[caracter])
            A += ord(cadena2[caracter])

            if U == A:
                resultado += "D"
            elif U > A:
                resultado += "U"
            else:
                resultado += "A"

        return resultado

    while True:

        cjugador1 = str(input("J1 Caracter: "))

        if cjugador1 == "x":
            break

        cjugador2 = str(input("J2 Caracter: "))

        # Validamos el caracter, regresa el valor si es valido, si no regresa 0
        validar(cjugador1)
        validar(cjugador2)

        resultado = comparar(cjugador1, cjugador2)
        historial += "------------------------------\n"
        historial += "| {:<10} | {:<10} |\n".format(cjugador1, resultado)
        historial += "| {:<10} | {:>10} |\n".format(cjugador2, " ")

        print("| {:<10} | {:<10} |\n".format("Entrada", "Salida"))
        print(historial)

if __name__ == "__main__":
    main()