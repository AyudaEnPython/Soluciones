"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solicita al usuario un número de mes al año, e imprime:
- el nombre del mes.
- la cantidad de dias que tiene cada mes.
"""
MESES = {
    "1": ("enero", 31),
    "2": ("febrero", 28),
    "3": ("marzo", 31),
    "4": ("abril", 30),
    "5": ("mayo", 31),
    "6": ("junio", 30),
    "7": ("julio", 31),
    "8": ("agosto", 31),
    "9": ("setiembre", 30),
    "10": ("octubre", 31),
    "11": ("noviembre", 30),
    "12": ("diciembre", 30),
}
mes = input("Ingresar mes expresado en números (1-12): ")
print(f"Mes: {MESES[mes][0]}")
print(f"Dias: {MESES[mes][1]}")
