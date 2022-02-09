"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Un restaurante ofrece tipos de comida, éstas pueden ser: dieta cruda,
dieta vegana, dieta vegetariana y dieta no vegetariana. Escribir un
programa que pregunte al cliente el tipo de comida que desea y en
función de su respuesta le muestre un menú de platillos referente a
esa dieta. Solo puede elegir un platillo. Al final el programa debe
mostrar qué tipo de comida el cliente solicitó y el nombre del plato
elegido (usar condicionales).
"""

tipos = [
    "dieta cruda",
    "dieta vegana",
    "dieta vegetariana",
    "dieta no vegetariana"
]
platillos = {
    0: ["A01", "A02", "A03", "A04"],
    1: ["B01", "B02", "B03", "B04"],
    2: ["C01", "C02", "C03", "C04"],
    3: ["D01", "D02", "D03", "D04"],
}

print("¿Qué tipo de comida desea? ")
for i, tipo in enumerate(tipos):
    print(f"{i+1}.- {tipo}")
tipo = int(input("Ingresar tipo: "))

print("Seleccionar un platillo: ")
for i, platillo in enumerate(platillos[tipo-1]):
    print(f"{i+1}.- {platillo}")
platillo = int(input("Ingresar platillo: "))

print(f"Tipo de comida: {tipos[tipo-1]}")
print(f"Platillo elegido: {platillos[tipo-1][platillo-1]}")
