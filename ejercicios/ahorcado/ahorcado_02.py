"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
FRASES = [
    "Vive tu momento",
    "Nunca subestimes el poder de la musica",
    "Nunca olvides lo mucho que tu familia te ama",
    "Porque la muerte es vida; enciende luces en otro lugar"
]
INTENTOS = 9


def presentar(patron):
    p = ""
    for i in patron:
        p += i
    print(p)


def ingresar_numero():
    cantidad = len(FRASES)
    mensaje = "Ingrese el númeor de frase que desea revelar (1 al {})"
    while True:
        numero = int(input(mensaje.format(cantidad)))
        if 0 < numero <= cantidad:
            return numero


def construir_patron(frase):
    patron = ""
    for i in frase:
        if i == " ":
            patron += " "
        else:
            patron += "_"
    return list(patron)


def run():
    numero = ingresar_numero()
    frase = FRASES[numero - 1]
    patron = construir_patron(frase)
    intentos = INTENTOS
    puntos = 0
    while True:
        if intentos == 0:
            print("Perdiste, la frase era:")
            print(frase)
            break
        presentar(patron)
        letra_ingresada = input(f"[{intentos}] Ingrese letra: ")
        intentos -= 1
        i = 0
        for letra in frase:
            if letra_ingresada.lower() == letra.lower():
                patron[i] = letra_ingresada
                puntos += 10
            i += 1
        if "_" not in patron:
            print(f"Felicidades, ganaste en {INTENTOS - intentos} intentos")
            print(f"Puntos: {puntos}")
            break


if __name__== "__main__":
    run()
