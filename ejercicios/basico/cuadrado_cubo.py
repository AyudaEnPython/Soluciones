"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Genere y visualice los 15 primeros números naturales, además de sus
cuadrados y cubos, exceptuando el 0.

Ejemplo:

#    NÚMERO  CUADRADO    CUBO
#      1        1          1
#      2        4          8
#      3        9         27
#      .        .          .
#      .        .          .
#      .        .          .
#      15       225     3375
"""

print(f"{'Número'} {'Cuadrado':>10} {'Cubo':>6}")
for n in range(1, 16):
    print(f"{n:>6} {n**2:>8} {n**3:>8}")
