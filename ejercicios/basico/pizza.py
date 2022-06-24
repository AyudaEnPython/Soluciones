"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que pregunte al usuario si quiere una pizza
vegetariana o no y en funcion de su respuesta le muestre un menu
con los ingredientes disponibles para que elija.

Ingredientes vegetarianos: Pimiento y Tofu.
Ingredientes no vegetarianos: Peperoni, jamon y salmon.

Solo se puede elegir un ingrediente ademas de la mozzarella y el tomate
que estan en todas las pizas.

Al final se debe mostrar por pantalla si la pizza elegida es vegetariana
o no y todos los ingredientes que lleva.
"""

eleccion = input("¿Quiere una pizza vegetariana? (s/n): ").lower()
if eleccion == "s":
    ingredientes = ("Pimiento", "Tofu")
    tipo = "vegetariana"
else:
    ingredientes = ("Peperoni", "Jamon", "Salmon")
    tipo = "no vegetariana"
for i, ingrediente in enumerate(ingredientes, 1):
    print(f"{i}.- {ingrediente}")
opcion = int(input("Seleccionar ingrediente > "))
print(f"\nPizza {tipo}")
print(f"Ingredientes: Mozzarella, Tomate, {ingredientes[opcion-1]}")
