"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar S nuevo usuario o N quieren para de ingresar nombre
Edad > 80 año si o si para de ingresar usuarios

NOTE: la persona que solicitó ayuda dejo solo ese enunciado.
"""
usuarios = []

while True:
    print("Ingresar 'S' para añadir un nuevo usuario o 'N' para detener: ")
    opcion = input("Opcion > ").lower()
    if opcion == "n":
        break
    elif opcion == "s":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        if edad > 80 or edad < 0:
            break
        else:
            usuarios.append((nombre, edad))
            print("Usuario añadido")
    else:
        print("Opcion no valida")

print("Usuarios registrados:")
for nombre, edad in usuarios:
    print(f"Nombre: {nombre} | Edad: {edad} años")
