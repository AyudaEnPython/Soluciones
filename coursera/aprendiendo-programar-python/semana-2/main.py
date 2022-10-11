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


if __name__ == "__main__":
    assert imc(80, 1.80) == 24.691358024691358
    assert velocidad(0.01, 1) == "La velocidad es 36.0 km/h o 10.0 m/s"
    assert xor(True, True) is False
    assert xor(False, True) is True
    assert xor(True, False) is True
    assert xor(False, False) is False
