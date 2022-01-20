"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

temperaturas = []

while True:
    try:
        t = input("Ingresar temperaturas: ").split(",")
        t = [float(i) for i in t]
        temperaturas.extend(t)
        if t[0] == 0:
            break
    except ValueError:
        print("Ingresar solo numeros")

t = [x for x in temperaturas if 5 <= x <= 15]
print(f"Promedio de temperaturas entre 5 y 15: {sum(t) / len(t)}")