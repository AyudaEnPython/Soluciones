"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

from random import randint

N = randint(1, 1000)

if N % 5 == 0 and 5 <= N <= 5*25:
    print("Correcto")
else:
    print("Incorrecto")