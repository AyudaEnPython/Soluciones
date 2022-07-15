"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Érase una vez en Namekusei, habitada por gente feliz y próspera. La
gente pagaba impuestos, por supuesto, su felicidad tenía límites. El
impuesto tenía que pagarse una vez al año y se evaluó utilizando la
siguiente regla:

Si el ingreso del ciudadano no era superior a 35000 dólares, el
impuesto era igual al 12% del ingreso menos 399 dólares y 2 centavos
(esta fue la llamada exención fiscal).
Si el ingreso era superior a esta cantidad, el impuesto era igual a
3500 dólares y 2 centavos, más el 24% del excedente sobre 35000
dólares.

Tu tarea es escribir una calculadora de impuestos.
Debe aceptar un valor de punto flotante: el ingreso.

A continuación, debe imprimir el imprimir el impuesto calculado,
redondeado a dólares totales. Hay una función llamada round() que hará
el redondeo por ti.

Nota: Este país Namekusei nunca devuelve dinero a sus ciudadanos. Si el
impuesto calculado es menor que cero, solo significa que no hay
impuesto. Ten en cuenta durante tus cálculos.

Datos de prueba
Entrada de muestra: 10000
Resultado esperado: El impuesto es: 801.0 dólares

Entrada de muestra: 100000
Resultado esperado: El impuesto es: 19100.0 dólares

Entrada de muestra: 1000
Resultado esperado: El impuesto es: 0.0 dólares

Nota: el sistema debe tener las validaciones correspondientes en la
entrada de datos.
"""
# pip install prototools
from prototools import float_input

monto = float_input("Ingrese el monto: ", min=0)
if monto <= 35000:
    impuesto = round((monto * 0.12) -399.2)
else:
    impuesto = round(3500.2 + ((monto-35000) * 0.24))
print(f"El impuesto es: {impuesto if impuesto > 0 else 0:.1f} dólares")
