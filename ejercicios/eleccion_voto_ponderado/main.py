"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

representantes = [
    ("Ingeniería", 243),
    ("Mecánica", 389),
    ("Administración", 312),
    ("Periodismo", 165),
    ("Enfermería", 134),
]
CANDIDATOS = (
    "Alejandar Pérez",
    "Claudia Gonzáles",
    "Juan Zarate",
    "Pedro Méndez",
)


def mostrar_candidatos():
    for i, candidato in enumerate(CANDIDATOS, 1):
        print(f"{i}. {candidato}")


def procesar_voto(voto, peso, votos):
    if voto in votos:
        votos[voto] += peso
    elif not voto:
        votos["0"] += 1
    else:
        votos["-1"] += 1


def resultados(votos):
    print("-"*40)
    print("Resultados".center(40))
    print("-"*40)
    for i, candidato in enumerate(CANDIDATOS, 1):
        print(f"{candidato} obtuvo {votos[str(i)]} votos.")
    print("-"*40)
    print(f"Votos en blanco: {votos['0']}")
    print(f"Votos nulos: {votos['-1']}")


def main():
    votos = {str(i): 0 for i in range(-1, len(CANDIDATOS) + 1)}
    for representante, peso in representantes:
        print(f"Turno del representante: {representante}\n")
        mostrar_candidatos()
        print("\nElegir una opción")
        procesar_voto(input("> "), peso, votos)
    resultados(votos)


if __name__ == "__main__":
    main()
