"""
Escriba el código utilizando find () y rebanado de cadenas (consulte
la sección 6.10) para extraer el número al final de la línea de
abajo. Convierta el valor extraído en un número de coma flotante e
imprímalo.

    +--------+
    | 0.8475 |
    +--------+

"""
texto = "X-DSPAM-Confidence:    0.8475"
print(float(texto[texto.find(":")+1:]))