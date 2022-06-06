"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realice un programa en el que se ingrese por teclado el nombre y peso
de un grupo de personas, sólo en el caso de que dicho peso sea cero,
negativo o más de 230 kilogramos no se registrará a la persona y
motivará la finalización del ingreso, en ese momento visualice:
- El número de personas registradas

Nota: No contar el último ingreso.

Ejemplo:

    NOMBRE: Wilman
    PESO: 80 kg
    NOMBRE: Jorge
    PESO: 76 kg
    NOMBRE: Roxana
    PESO: 50 kg
    NOMBRE: Thalia
    PESO: -10 (finaliza)

    Personas registradas: 3
"""

registrados = 0
while True:
    nombre = input("Nombre: ")
    peso = int(input("Peso: "))
    if peso <= 0 or peso > 230:
        break
    else:
        registrados += 1
print(f"Personas registradas: {registrados}")
