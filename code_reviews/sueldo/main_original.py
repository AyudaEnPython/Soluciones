"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sys

def main(**args):
    
    """TODO: Docstring for main.

        Las variables tiene valor por default, puede usar los siguientes parametros
        para modificarlos

        ejem.: sueldo=3000

        :sueldo: Sueldo base del trabajador
        :ventas: Cantidad de ventas del mes
        :porcentaje: ganancias por cada venta
    
    """

    ganancia_venta = lambda cantidad: float(cantidad) / 100 * float(args["porcentaje"])

    ganancia = 0

    for x in  range(args["ventas"]):
        dinero = float(input("Cantidad de la venta {} ".format(x+1)))
        ganancia += ganancia_venta(dinero)

    print("Sueldo: {}, Comision {}, Total: {}".format(args["sueldo"],ganancia, ganancia + args["sueldo"]))


if __name__ == "__main__":
    args = sys.argv[1:]

    parametros = {}
    for arg in args:
        nombre, valor = arg.strip().split("=")
        parametros[nombre.strip()] = valor.strip()

    parametros = {"sueldo": int(8000), "ventas": int(3), "porcentaje": int(10), **parametros}
    main(sueldo = int(parametros["sueldo"]),
         ventas = int(parametros["ventas"]),
         porcentaje = float(parametros["porcentaje"]))