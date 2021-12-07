"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

t1, t2 = [], []
for _ in range(10):
    a = float(input("Ingresar temperatura T1: "))
    b = float(input("Ingresar temperatura T2: "))
    t1.append(a)
    t2.append(b)

print(f"Temperatura promedio de T1: {sum(t1)/len(t1)}")
print(f"Temperatura promedio de T2: {sum(t2)/len(t2)}")