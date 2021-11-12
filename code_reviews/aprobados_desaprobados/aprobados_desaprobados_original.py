"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solución completa en:
https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/aprobados_desaprobados.py
"""

#Escribir un programa que solicite ingresar la nota de 10 alumnos, el programa, debe
# informar de cuantos han aprobado, cuantos han reprobado, nota promedio, la mayor y la menor
# faltan realizar comprobaciones del tipo de dato ingresado 
print("Escriba 0 para terminar el programa")
notas = []
while True:
    nota = float(input("Ingrese nota: "))
    if nota == 0:
        print("Saliendo... ")
        break
    #comprobar q la nota este en el rango 1-10
    if not nota > 10:
        notas.append(nota)
    else: 
        # si no lo esta vuelve a pedir la nota
        print("Asegurate que la nota este en rango (1-10)")
        continue
    #cuando la lista tenga ya 10 notas dejara de pedir nota
    if len(notas) == 10:
        break
aplazados = 0
aprobados = 0
notables = 0
for nota in notas:
    if nota < 4:
        aplazados += 1
    elif nota <= 4 or nota <= 7:
        aprobados += 1
    elif nota > 7: 
        notables += 1 
print(f"""
Aplazados: {aplazados}
Aprobados: {aprobados}
Notables: {notables}
""")