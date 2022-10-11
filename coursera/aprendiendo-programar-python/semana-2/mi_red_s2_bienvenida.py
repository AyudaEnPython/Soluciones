"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

## Ejercicio 1

Escribe 3 solicitudes de datos al usuario, por ejemplo, género, número
de teléfono, ciudad donde vive, país de nacimiento y dirección. Guarda
estos datos en variables del tipo correspondiente y finalmente
escríbelos por pantalla utilizando la función "print". Puedes agregar
tantas líneas de código como creas necesario.

NOTE: refactored.
"""
# flake8: noqa

CURRENT_YEAR = 2022
SIZE = 70
TITULO = """
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/
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

print("Ahora vamos a publicar tu primer mensaje.\n")
mensaje = input("¿Qué piensas hoy?\n> ")
print()
print("-"*SIZE)
print(f"{nombre} dice: {mensaje}")
print("-"*SIZE)

print("\nCuéntame más de ti, para seguir agregándolo a tu perfil.\n")

pais = input("¿En qué país naciste?\n> ")
ciudad = input("¿En qué ciudad vives?\n> ")
telefono = input("¿Cual es tu número de teléfono?\n> ")

print()
print("Nuevos datos agregados en tu perfil.")
print("-"*SIZE)
print(f"País: {pais}")
print(f"Ciudad: {ciudad}")
print(f"Teléfono: {telefono}")
print("-"*SIZE)
