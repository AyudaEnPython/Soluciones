"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

while True:
    print("Tablas\nEscoger una opcion:")
    print("\n.1. Sumar\n.2. Restar\n.3. Multiplicar\n.4. Dividir\n")
    opcion = input("> ")
    if opcion == "1":
        operador = "+"
    elif opcion == "2":
        operador = "-"
    elif opcion == "3":
        operador = "*"
    elif opcion == "4":
        operador = "/"
    else:
        operador = None
        print("Opcion no valida")
    if operador:
        break

n = int(input("Número: "))
for x in range(11):
    if operador == "/" and x == 0:
        print(f"{n} {operador} {x} = No se puede dividir por cero")
    else:
        if operador == "/":
            resultado = n / x
        elif operador == "*":
            resultado = n * x
        elif operador == "-":
            resultado = n - x
        elif operador == "+":
            resultado = n + x
        print(f"{n} {operador} {x} = {resultado}")
