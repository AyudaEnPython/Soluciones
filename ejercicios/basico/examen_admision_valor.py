"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñar un algoritmo que determine el importe a pagar el examen de
admisión de una universidad, cuyo valor depende del nivel
socioeconómico y el colegio de procedencia.

#                 +-----------------+
#                 |   NIVEL SOCIAL  | 
#    +------------+-----+-----+-----+
#    | Colegio    |  A  |  B  |  C  |
#    +------------+-----+-----+-----+
#    | Nacional   | 300 | 200 | 100 |
#    | Particular | 400 | 300 | 200 |
#    +------------+-----+-----+-----+

Prueba de escritorio:
Colegio = "P"
Nivel = "B"
mp = 300
"""
# ------------------------------------------------- usando if-elif-else
colegio = input("Colegio (P)articular o (N)acional? ").upper()
nivel = input("Nivel socioeconómico (A, B o C): ").upper()
if colegio == "P":
    monto = 400 if nivel == "A" else 300 if nivel == "B" else 200
elif colegio == "N":
    monto = 300 if nivel == "A" else 200 if nivel == "B" else 100
print(f"El monto a pagar es de {monto}")

# ------------------------------------------------- usando diccionarios
# tabla = {
#     "P": {"A": 400, "B": 300, "C": 200},
#     "N": {"A": 300, "B": 200, "C": 100},
# }
# colegio = input("Colegio (P)articular o (N)acional? ").upper()
# nivel = input("Nivel socioeconómico (A, B o C): ").upper()
# print(f"El monto a pagar es de {tabla[colegio][nivel]}")
