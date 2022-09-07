"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El costo de una póliza de seguros para automóviles se calcula de la
siguiente forma:

    Ctotal = 3%VA + CM + CEP + CAP

Diseñe un programa que lea el nombre y la edad del propietario, el
valor del automóvil (VA), el modelo y el número de accidentes que ha
tenido; e imprima el nombre del propietario seguido del costo de la
póliza. Utilice los siguientes datos para determinar los cargos:

#+--------------------------+ +--------------------------------------+
#|  Cargo por modelo (CM)   | | Cargo por edad del propietario (CEP) |
#+--------------------------+ +--------------------------------------+
#|    90 o anterior  | 0.1% | |      18 a 23 años     |    $350      |
#|        91-97      | 0.3% | |      24 a 55 años     |    $200      |
#| 98 o más reciente | 0.5% | |      56 a 65 años     |    $400      |
#+--------------------------+ +--------------------------------------+
"""

cm = lambda m: {m <= 90: 0.001, 91 <= m <= 97: 0.003, 98 <= m: 0.005}[1]  # noqa: E731, E501
cep = lambda e: {18 <= e <= 23: 350, 24 <= e <= 55: 200, 56 <= e <= 65: 400}[1]  # noqa: E731, E501
cap = lambda a: {a <= 3: 15, a > 3: 15 + (a-3)*20}[1]  # noqa: E731, E501

nombre = input("Nombre del propietario: ")
edad = int(input("Edad del propietario: "))
va = int(input("Valor del automóvil: "))
modelo = int(input("Modelo del automóvil: "))
accidentes = int(input("Número de accidentes: "))

total = 0.03*va + cm(modelo)*va + cep(edad) + cap(accidentes)

print(f"{nombre} tiene una póliza de seguros por ${total:.2f}")
