"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

print("Ingrese los lados del triángulo:")
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a == b == c:
    print("Equilatero")
elif a == b or b == c or a == c:
    print("Isósceles")
else:
    print("Escaleno")