"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

while True:
    notas = []
    nombre = input("Ingrese nombre: ")
    if nombre == "":
        break
    for _ in range(3):
        try:
            nota = int(input("Ingrese nota: "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota fuera de rango")
                break
        except ValueError:
            print("Nota debe ser un número")
            notas = None
            break
    if notas:
        promedio = notas[0] * 0.1 + notas[1] * 0.5 + notas[2] * 0.4
        print(f"{nombre} tiene una nota de {promedio}")
