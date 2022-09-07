"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada la temperatura en grados Fahrenheit, convertirla a grados Celsius
y luego mostrar un mensaje según la tabla:

+------------------------------------+------------------------------+
|           Grados Celsius           |      Mensaje a mostrar       |
+------------------------------------+------------------------------+
|Menos de 12 grados                  |"X grados... Hace mucho frio" |
|Desde 12 grados y menos de 16 grados|"X grados... Está fresco"     |
|Desde 16 grados y menos de 26 grados|"X grados... Está templado"   |
|Desde 26 grados a más               |"X grados... Hace mucho calor"|
+------------------------------------+------------------------------+

Se sabe que: t(°C) = (t(°F) - 32) / 1.8

Ejemplo: Si se ingresa 98.6 grados Fahrenheit, el programa mostrará:
37 grados... Hace mucho calor
"""

f = float(input("Ingrese la temperatura en grados Fahrenheit: "))
c = (f - 32) / 1.8
if c < 12:
    print(f"{c} grados... Hace mucho frio")
elif c < 16:
    print(f"{c} grados... Está fresco")
elif c < 26:
    print(f"{c} grados... Está templado")
else:
    print(f"{c} grados... Hace mucho calor")
