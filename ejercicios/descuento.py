"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar una función que utilice dos parámetros: cantidad comprada y
precio unitario y retorne una tupla con: (monto antes del descuento, 
descuento, monto después del descuento). Para el descuento se considera
una promoción de 5 x 2, es decir por cada 5 unidades de compra, dos
unidades no se pagan (descuento):

En el programa principal, se deberá ingresar por teclado la cantidad
comprada y el precio unitario, utilizar la función y mostrar lo que
retorna la función, según ejemplo de corrida.

Ejemplo de corrida:

Ingresar cantidad comprada: 19
Ingrese precio unitario: 3.5

(66.5, 21.0, 45.5)
"""

def calcular(cantidad: int, precio: float) -> tuple:
    """Calcula el descuento y el monto final.

    :param cantidad: Cantidad comprada.
    :cantidad type: int
    :param precio: Precio unitario.
    :precio type: float
    :return: Tupla con (monto antes del descuento, descuento, monto
    después del descuento).
    :rtype: tuple
    """
    monto_antes = cantidad * precio
    descuento = ((cantidad // 5) * 2) * precio
    monto_despues = monto_antes - descuento
    return monto_antes, descuento, monto_despues


def main():
    cantidad = int(input('Ingrese cantidad comprada: '))
    precio_unitario = float(input('Ingrese precio unitario: '))
    resultado = calcular(cantidad, precio_unitario)
    print(resultado)


if __name__ == '__main__':
    main()