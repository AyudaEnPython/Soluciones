"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Un extranjero llegó al país, escribir un programa con una lista de
productos con sus respectivos precios en dólares. El usuario debe
elegir un producto. Al final el programa debe mostrar qué producto
solicitó el usuario y cuánto cuesta en soles.
"""
CONVERSION = 3.84
PRODUCTOS = [
    ("Pizza", 12.5),
    ("Hamburguesa", 8.35),
    ("Papas fritas", 2.5),
    ("Coca-Cola", 2.5),
]

for i, producto in enumerate(PRODUCTOS):
    print(f"{i + 1} - {producto[0]}")

producto = int(input("Ingrese el número del producto: "))
print(f"Producto: {PRODUCTOS[producto - 1][0]}")
print(f"Precio: ${PRODUCTOS[producto - 1][1] * CONVERSION:.2f}")
