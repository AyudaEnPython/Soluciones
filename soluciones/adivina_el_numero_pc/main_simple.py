"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

MENSAJE = "Tu número es"
inicio = 1
fin = 100

print(" Adivino tu número ".center(50, "-"))
print("Instrucciones:")
print("- Piensa en un número del 1 al 100 y lo adivinaré.")
print("- Responde con 'si' o 'no' a mis preguntas.")
print("-"*50)

while inicio <= fin:
    medio = (inicio + fin) // 2
    respuesta = input(f"¿{MENSAJE} {medio}?\n> ").lower()
    if respuesta == "si":
        print(f"¡Genial, lo adiviné! {MENSAJE} {medio}.")
        break
    respuesta = input(f"¿{MENSAJE} mayor que {medio}?\n> ").lower()
    if respuesta == "si":
        inicio = medio + 1
    else:
        fin = medio - 1

if inicio > fin:
    print("Parece que hay contradicciones en tus respuestas.")

print("¡Fin del juego!")
