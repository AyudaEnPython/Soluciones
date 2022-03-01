"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Frederick y tú son buenos amigos. Ayer, Frederick recibió N tarjetas de
crédito de ABCD Bank. Frederick requiere verificar si los números de su
tarjeta de crédito son válidos o no. Resulta que eres excelente en
expresiones regulares, ¡así que él está pidiendo ty ayuda!

Una tarjeta de crédito es válida de ABCD Bank tiene las siguientes
características:

- Los números de tarjetas deben iniciar con 4, 5 o 6.
- La cantidad de dígitos deben ser 16.
- Debene ser dígitos entre [0 - 9].
- Pueden tener dígitos en grupos de 4, separados por un guión "-".
- No deben contener ningún otro separador como "", "_", etc.
- No deben tener 4 o más dígitos repetidos consecutivos.
"""
import re

tarjetas = [
    "4123456789012346", "5123-4567-8901-2346", "5555216789012345",
    "4123 4567 8901 2346", "5123_4567_8901_2346", "1123/4567/8901/2345",
    "9349582034828349", "8123-4567-8901-2345", "5123456789012345",
]

exp = re.compile(r'(^[456]\d{3})-?(\d{4})-?(\d{4})-?(\d{4}$)')
val = re.compile(r'((\d)-?(?!(-?\2){3})){16}')
encontrados = [
    tarjeta for tarjeta in tarjetas
    if exp.match(tarjeta) and val.match(tarjeta)
]
print(encontrados)
