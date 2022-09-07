"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

while True:
    try:
        radio = int(input("Ingrese el radio: "))
        altura = int(input("Ingrese la altura: "))
        if radio <= 0 and altura <= 0:
            print("El radio y la altura deben ser números positivos")
        elif radio <= 0:
            print("El radio debe ser positivo")
        elif altura <= 0:
            print("La altura debe ser positiva")
        else:
            break
    except ValueError:
        print("El valor ingresado no es un número entero.")

volumen = 3.1416 * altura * (radio ** 2)
print(f"El volumen del cilindro es: {volumen}")
