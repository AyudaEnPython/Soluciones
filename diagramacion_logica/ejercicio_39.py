"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

mayor = 0
for _ in range(10):
    temperatura = float(input("Introduce la temperatura: "))
    if temperatura >= mayor:
        mayor = temperatura

print(f"La temperatura más alta es {mayor}")