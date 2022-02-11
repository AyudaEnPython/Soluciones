"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Contributor: Carolina Morán
Source:
https://github.com/CarolinaMoran03/Juego-de-ahorcado-con-frase/blob/main/Juego%20de%20ahorcado%20con%20frase
"""
participante=input("Ingrese nombre del participante: ")
print(participante.upper())

def run():
    frases = ["Vive tu momento",
              "Nunca subestimes el poder de la musica",
              "Nunca olvides lo mucho que te ame tu familia", "Amo mi locura", "Que nadie te diga que no","Carlos Rivera", "No me ponga cero inge", "La fuerza estara contigo"]
    cantidad = len(frases)
    numero = 0

    while numero < 1 or numero > cantidad:
        numero = int(input("Ingrese el numero de frase que desea revelar (1 al {c}): ".format(c=cantidad)))

    frase = frases[numero-1]

    patron = ""
    for i in frase:
        if i == " ":
            patron += " "
        else:
            patron += "_"

    patron = list(patron)
    presentar(patron)
    vidas = 5
    cont = 0
    a = 10
    while vidas > 0:
        letra = input("Ingrese letra: ")
        x = 0
        for i in frase:
            if letra.lower() == i.lower():
                patron[x] = letra
            x += 1
        if letra in patron:
            print("Felicitaciones ganaste", a, " puntos")
            cont += a
            presentar(patron)
        if "_" not in patron:
            print("FELICIDADES",participante.upper(), "Acabas De Adivinar La Frase")
            print("Obtuvistes:", cont, " Puntos")
            break
        if letra not in patron:
            vidas -= 1
            print("Te Equivocaste, Te Quedan", +vidas, "Intentos")
            presentar(patron)

    else:
        print("Chale",participante.upper(), "Acabas de Perder, Como Cuando La Perdistes A Ella")
        print("Tienes:", cont, " Puntos, Gracias Por Participar")


def presentar(patron):
    p = ""
    for i in patron:
        p = p + i
    print(p)


if __name__ == "__main__":
    run()