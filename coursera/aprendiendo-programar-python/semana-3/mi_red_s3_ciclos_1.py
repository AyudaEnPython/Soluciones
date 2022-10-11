"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

## Ejercicio 1

Este programa termina cada vez que el valor de "escribir_mensaje" es
distinto a "S" o a "s". Modifica el programa para que termine
ÚNICAMENTE cuando se ingresa "N" o "n". En caso de que ingrese algo
distinto, debe solicitar al usuario una nueva opción.

## Ejercicio 2

Modifica este menú para que le permita al usuario realizar más de una
acción. Por ejemplo, puedes agregar una acción que permita al usuario
modificar su nombre en el perfil.

NOTE: refactored.
"""

CURRENT_YEAR = 2022
SIZE = 70
TITULO = """
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \\/ /  / ___/ _ \\/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \\___/\\__,_/
"""

print("Bienvenido a ...")
print(TITULO)

nombre = input("Para empezar, dime como te llamas.\n> ")
print(f"Hola {nombre}, bienvenido a Mi Red\n")
dob = int(input("Para preparar tu perfil, dime en qué año naciste.\n> "))
edad = CURRENT_YEAR - dob
print("\nCuéntame más de ti, para agregarlo a tu perfil.")
estatura = float(input("¿Cuánto mides? Dímelo en metros.\n> "))
amigos = int(input(
    "\nMuy bien. Finalmente, cuéntame cuantos amigos tienes.\n> "
))

print()
print(
    f"Muy bien, {nombre}. Entonces podemos crear un perfil con estos datos."
)
print("-"*SIZE)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(
    f"Estatura: {int(estatura)} metros y {int((estatura%1)*100)} centímetros"
)
print(f"Amigos: {amigos}")
print("-"*SIZE)
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

continuar = True
while continuar:
    escribir = input("¿Deseas escribir un escribir? (S/N)\n> ")
    if escribir == "N" or escribir == "n":
        continuar = False
    elif escribir == "S" or escribir == "s":
        print("Vamos a publicar un mensaje.")
        mensaje = input("¿Qué piensas hoy?\n> ")
        print()
        print("-"*SIZE)
        print(f"{nombre} dice: {mensaje}")
        print("-"*SIZE)
        print()

print("\nGracias por usar Mi Red. ¡Hasta pronto!\n")
