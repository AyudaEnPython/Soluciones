"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

puntualidad = 0
rendimiento = 0
puntaje = 0
bonificacion = 0

tardanzas = int(input("Número de tardanzas: "))
observaciones = int(input("Número de tardanzas: "))

if tardanzas < 1:
    puntualidad = 10
elif 1 <= tardanzas <= 2:  # elif tardanzas == 1 or tardanzas == 2:
    puntualidad = 8
elif 3 <= tardanzas <= 5:
    puntualidad = 6
elif 6 <= tardanzas < 9:
    puntualidad = 4

if observaciones == 0:
    rendimiento = 10
elif observaciones == 1:
    rendimiento = 8
elif observaciones == 2:
    rendimiento = 5
elif observaciones == 3:
    rendimiento = 1

puntaje = puntualidad + rendimiento

if puntaje < 11:
    bonificacion = 2.5
elif 11 <= puntaje <= 13:
    bonificacion = 5
elif 14 <= puntaje <= 16:
    bonificacion = 7.5
elif 17 <= puntaje <= 19:
    bonificacion = 10
else:
    bonificacion = 12.5

print(f"Puntaje por puntualidad: {puntualidad}")
print(f"Puntaje por rendimiento: {rendimiento}")
print(f"Puntaje total: {puntaje}")
print(f"Bonificación: s/. {bonificacion:.2f}")
