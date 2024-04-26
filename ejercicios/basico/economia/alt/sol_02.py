"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

multa = 0
mensaje = ""

velocidad = float(input("Velocidad: "))

if velocidad < 60:
    mensaje = "Velocidad permitida"
elif 60 <= velocidad < 65:
    mensaje = "Peligor en el límite de velocidad"
else:
    mensaje = "Ha superado el límite de velocidad"

if 65 <= velocidad < 75:
    multa = 300
elif 75 <= velocidad < 85:
    multa = 750
if 85 <= velocidad < 100:
    multa = 1500
else:
    multa = 3700

print(mensaje)
print(f"Multa: S/. {multa}.00")
