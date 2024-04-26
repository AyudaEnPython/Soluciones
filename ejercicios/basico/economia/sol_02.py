"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import RangeDict, float_input, textbox

T = RangeDict({
    (0, 59): "Velocidad permitida",
    (60, 65): "Peligro en el límite de velocidad",
    (66, 1000): "Ha superado el límite de velocidad",
})
M = RangeDict({
    (65, 75): 300,
    (76, 85): 750,
    (86, 100): 1500,
    (100, 1000): 3700,
})


def main():
    velocidad = float_input("Velocidad: ", min=0, lang="es")
    textbox(T[velocidad])
    textbox(f"S/. {M[velocidad]}.00")


if __name__ == "__main__":
    main()
