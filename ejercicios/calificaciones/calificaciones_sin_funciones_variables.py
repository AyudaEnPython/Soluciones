"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

while True:
    practica = problemas = teoria = 0
    nombre = input("Ingrese nombre: ")
    if nombre == "":
        break
    for _ in range(3):
        try:
            practica = int(input("Ingrese nota de practicas: "))
            problemas = int(input("Ingrese nota de problemas: "))
            teoria = int(input("Ingrese nota de teoria: "))
            if ((0 <= practica <= 10) and
                (0 <= problemas <= 10) and
                (0 <= teoria <= 10)
            ):
                promedio = practica * 0.1 + problemas * 0.5 + teoria * 0.4
                print(f"{nombre} tiene una nota de {promedio}")
            else:
                print("Nota fuera de rango")
                break
        except ValueError:
            print("Nota debe ser un número")
            break