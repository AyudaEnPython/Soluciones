"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe un programa Python que acepte una cadena y calcule el número de dígitos y letras.
"""

digitos = letras = 0

cadena = input("Ingrese una cadena: ")

for caracter in cadena:
    if caracter.isdigit():
        digitos += 1
    elif caracter.isalpha():
        letras += 1

print(f"Letras {letras}")
print(f"Digitos {digitos}")
