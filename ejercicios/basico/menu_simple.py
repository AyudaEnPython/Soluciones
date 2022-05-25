"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Construir un programa que permita la construcción del siguiente MENU:
1. Digitar 1 para recibir 5 números enteros.
2. Digitar 2 para calcular la suma de los números ingresados
    previamente.
3. Digitar 3 para permitir que el usuario agregue un nuevo número a la
    lista.
4. Digitar 4 para salir.

NOTE: No es recomendable usar esta forma de construcción de menús.
    Lo mejor es usar funciones y/o clases. Otra opción es delegar la
    construcción del menú a una biblioteca especializada como
    prototools (pip install prototools).
"""

numeros = []

while True:
    print("1. Ingresar numeros")
    print("2. Calcular suma")
    print("3. Agregar nuevo numero")
    print("4. Salir")
    opcion = input("opcion> ")
    if opcion == "4":
        break
    elif opcion == "1":
        for i in range(1, 6):
            numeros.append(int(input(f"[{i}] numero> ")))
    elif opcion == "2":
        print(sum(numeros))
    elif opcion == "3":
        numeros.append(int(input("nuevo numero> ")))
    else:
        print("Opcion incorrecta")
