"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa en lenguaje Python que permita calcular la nota
del primer parcial de una asignatura en el ISTG. Se deben solicitar
las 3 calificaciones sobre 10: Exámen, Práctica y Formativa. El
exámen corresponde al 40% del parcial, las notas de Práctica es el 30%
y Formativo el 30%. La suma de las ponderaciones es la nota final del
parcial. Mostrar los resultados.
"""

examen = int(input("Examen: "))
practica = int(input("Práctica: "))
formativa = int(input("Formativa: "))

promedio = (examen * 0.4) + (practica * 0.3) + (formativa * 0.3)
print("Nota final:", promedio)
