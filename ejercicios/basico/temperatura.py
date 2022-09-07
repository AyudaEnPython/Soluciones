"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En Python, elabora un programa que dé solución a lo siguiente:

El sistema meteorológico local requiere un sistema para capturar la
temperatura promedio de cada día de la semana e imprimir el nombre del
día y un mensaje de la percepción de la temperatura de acuerdo con el
valor capturado según la siguiente tabla (Pista: Se solicita al usuario
día y temperatura).

    +-----------------------------+--------------+
    | Temperatura                 | Mensaje      |
    +-----------------------------+--------------+
    | Menor o igual a 0           | Congelante   |
    | 1 a 10 grados C             | Muy frío     |
    | 11 a 20 grados C            | Frio         |
    | 21 a 24 grados C            | Templado     |
    | 25 a 29 grados C            | Agradable    |
    | 30 a 35 grados C            | Caliente     |
    | Mayor o igual a 36 grados C | Muy Caliente |
    +-----------------------------+--------------+

NOTE: el enunciado menciona la temperatura promedio de cada día de la
    semana pero no especifica la cantidad de muestras de temperaturas a
    capturar.
"""

dia = input("Día de la semana: ")
temperatura = int(input("Temperatura: "))

if temperatura <= 0:
    mensaje = "congelante"
elif temperatura <= 10:
    mensaje = "muy frío"
elif temperatura <= 20:
    mensaje = "frio"
elif temperatura <= 24:
    mensaje = "templado"
elif temperatura <= 29:
    mensaje = "agradable"
elif temperatura <= 35:
    mensaje = "caliente"
else:
    mensaje = "muy caliente"

print(f"El día {dia} se siente {mensaje}")
