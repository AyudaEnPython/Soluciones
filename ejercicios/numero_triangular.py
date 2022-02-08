"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Considere la secuencia de números triangulares: 1, 3, 6, 10, ... cuyo
nombre refleja su ley de formación:
#                                        *
#                            *          * *
#                  *        * *        * * *
#          *      * *      * * *      * * ...
#    *    * *    * * *    * * * *    * * ... *
#    1     3       6        10      sum(n(n+1)/2)

Escriba un programa que reciba como entrada un número natural t y
determine si es un número triangular.
"""

t = int(input("Ingrese un número natural: "))

s = (1 + 8 * t) ** 0.5

if s.is_integer():
    print("El número es triangular.")
else:
    print("El número no es triangular.")