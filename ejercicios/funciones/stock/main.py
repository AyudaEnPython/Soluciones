"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

ITEM = {"precio": 0, "stock": 1}


def get_data():
    return {
        "ipa": [1.4, 40],
        "pils": [1.2, 50],
        "amber": [1.1, 100],
    }


def stock_disponible(stock, variedad, cantidad):
    if stock[variedad][ITEM["stock"]] < cantidad:
        return False
    return True


def disminuir_stock(stock, variedad, cantidad):
    stock[variedad][ITEM["stock"]] -= cantidad


def obtener_precio(stock, variedad, cantidad):
    return stock[variedad][ITEM["precio"]] * cantidad


def procesar(stock):
    total = 0
    while True:
        variedad = input("Ingrese la variedad: ")
        if variedad not in stock:
            break
        cantidad = input("Ingrese la cantidad: ")
        try:
            cantidad = int(cantidad)
        except ValueError:
            print("Ingresar una cantidad válida!")
            continue
        if stock_disponible(stock, variedad, cantidad):
            disminuir_stock(stock, variedad, cantidad)
            total += obtener_precio(stock, variedad, cantidad)
        else:
            print(f"Cantidad de {variedad} no disponible")
    return total


def main():
    data = get_data()
    total = procesar(data)
    print(f"Total: {int(total)}")
    print(data)


if __name__ == "__main__":
    main()
