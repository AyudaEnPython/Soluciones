"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

# Pregunta 1
def mcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1


# Pregunta 2
def exponente(n):
    i, e = 1, 0
    while i < n:
        i *= 2
        e += 1
    return e - 1


# Pregunta 3
def es_primo(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


# Pregunta 3
def pandigitales(n):
    return len(set(str(n))) == 10


# Pregunta 3
def panprimo(n):
    return pandigitales(n) and es_primo(n % 1e3)


if __name__ == "__main__":
    assert mcd(10, 15) == 5
    assert exponente(65) == 6
    assert panprimo(2424643) == False
    assert panprimo(1234567890) == False
    assert panprimo(10123485769) == True
