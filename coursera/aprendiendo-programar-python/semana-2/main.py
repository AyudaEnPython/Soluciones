"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

# Pregunta 1
def imc(masa, estatura):
    return masa / (estatura ** 2)


# Pregunta 2
def velocidad(distancia, tiempo):
    return (
        f"La velocidad es {distancia/tiempo*3600} km/h o "
        f"{distancia*1000/tiempo} m/s"
    )


# Pregunta 3
def xor(a, b):
    return a and not b or not a and b
