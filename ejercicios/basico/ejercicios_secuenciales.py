"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

----------------------- Ejercicios Secuenciales -----------------------

1. Jardines La Paz vende parcelas a crédito, donde el cliente da una
    inicial y el resto lo paga en 24 cuotas, pero con un incremento del
    20% sobre lo que quedó debiendo. Teniendo como dato de entrada el
    precio de la parcela determine el monto de cada cuota y el precio
    final de la parcela.

2. El Diario de Valera cobra por un aviso clasificado un monto que
    depende del número de palabras, tamaño en centímetros y número de
    colores. Cada palabra tiene un costo de $100, cada centímetro tiene
    un costo de $150 y cada color tiene un costo de $250. Realice un
    algoritmo que determine el monto a pagar por un aviso clasificado.

3. CADELA requiere de la lectura anterior en kilovatios y la lectura
    actual en kilovatios de un medidor de luz para determinar el
    consumo de electricidad de una vivienda. Teninedo como datos de
    entrada la lectura inicial y la lectura final en kilovatios de un
    medidor, determine el consumo el kilovatio y el monto a pagar por
    dicho consumo sabiendo que cada kilovatio tiene un valor de $1.200.
    Adicionalmente cobran el 10% del monto del consumo por concepto de
    aseo urbano, determine el monto total a pagar.

4. El Banco del Pueblo da microdréditos a empresarios para ser
    cancelados en un lapso de 2 años (24 meses). Al monto del préstamo
    se le cobra un interés del 24%. El empresario debe pagar la mitad
    del préstamo en 4 cuotas especiales y la otra mitad en 20 cuotas
    ordinarias. Realice un algoritmo que teniendo como dato de entrada
    el monto del préstamo, determine el monto total a pagar por el
    préstamo, el monto de las cuotas especiales y el monto de las
    cuotas ordinarias.

5. Una Agencia de Viajes cobra por un Tour a Margarita $800.000 diario
    por persona. Realice un algoritmo que determine el monto a pagar
    por una familia que desee realizar dicho Tour sabiendo que también
    cobran el 12% de IVA.
"""
# --------------------------------------------------------- Ejercicio 1
inicial = float(input("Ingrese la inicial: "))
precio = float(input("Ingrese el precio de la parcela: "))
cuotas = (precio - inicial) * 1.2
print(f"El monto de cada cuota es: {cuotas / 24:.2f}")
print(f"El precio final de la parcela es: {inicial + cuotas:.2f}")

# --------------------------------------------------------- Ejercicio 2
palabra = int(input("Número de palabras: ")) * 100
tamaño = int(input("Tamaño en centímetros: ")) * 150
colores = int(input("Número de colores: ")) * 250
print(f"El monto a pagar es: ${palabra + tamaño + colores}")

# --------------------------------------------------------- Ejercicio 3
inicial = float(input("Lectura inicial: "))
final = float(input("Lectura final: "))
pago = (final - inicial) * 1.2
aseo_urbano = pago * 0.1
print(f"Monot a pagar: {pago + aseo_urbano:.2f}")

# --------------------------------------------------------- Ejercicio 4
prestamo = float(input("Ingrese el monto del préstamo: "))
total = prestamo * 1.24
especiales = (total * 0.5) / 4
ordinarias = (total * 0.5) / 20
print(f"Monto total a pagar: {total:.2f}")
print(f"Monto de las cuotas especiales: {especiales:.2f}")
print(f"Monto de las cuotas ordinarias: {ordinarias:.2f}")

# --------------------------------------------------------- Ejercicio 5
personas = int(input("Número de personas: "))
total = (personas * 800) * 1.12
print(f"El monto a pagar es: ${total:.2f}")
