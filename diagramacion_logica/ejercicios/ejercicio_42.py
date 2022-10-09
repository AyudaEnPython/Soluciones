"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


while True:
    try:
        numero = int(input("Ingresar un numero: "))
    except ValueError:
        print("El valor ingresado no es un numero")
        continue
    primo = True
    if numero == 2 or numero == 3:
        primo = True
    elif numero % 2 == 0 or numero < 2:
        primo = False
    else:
        i = 3
        while i <= int(numero**0.5) + 1:
            if numero % i == 0:
                primo = False
                break
            i += 2
    if primo:
        print("El numero es primo")
    else:
        print("El numero no es primo")
    opcion = input(
        "Ingrese 's' para salir, para continuar presione cualquier tecla: "
    )
    if opcion == 's':
        break
