"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import int_input, menu_input, banner, text_align

ADICIONAL = 1.5
IVA = 0.12
PRECIOS = {"pequeña": 6.5, "mediana": 12.35, "familiar": 22.5}

iva = lambda precio: precio * IVA
precio_con_iva = lambda precio, iva: precio + iva
precio_sin_iva = lambda t, c, i: PRECIOS[t] * c + (ADICIONAL * i)


def datos():
    t = menu_input(tuple(PRECIOS.keys()), numbers=True, lang="es")
    c = int_input("Cantidad: ", min=1, max=25)
    i = int_input("Adicionales: ", min=0, max=5)
    return t, c, i


@banner("Boleta", 48)
def mostrar(t, c, i):
    precio = precio_sin_iva(t, c, i)
    return (
        f"{c} unidades {t}\t- {PRECIOS[t]:{5}.2f} c/u\t"
        f"$ {PRECIOS[t] * c:{6}.2f}\n"
        f"{i} ingredientes\t\t- {ADICIONAL:{5}.2f} c/u\t"
        f"$ {i * ADICIONAL:{6}.2f}\n\n"
        f"\t\t\tPrecio sin IVA\t$ "
        f"{precio:{6}.2f}\n"
        f"\t\t\tIVA 12%\t\t$ "
        f"{iva(precio):{6}.2f}\n"
        f"\t\t\tPrecio Final\t$ "
        f"{precio_con_iva(precio, iva(precio)):{6}.2f}"
    )


def main():
    text_align("Ingresar Pedido", 48, align="center")
    t, c, i = datos()
    print(mostrar(t, c, i))


if __name__ == "__main__":
    main()
