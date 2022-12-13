"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: No se recomienda esta manera de programar.
"""

OPCIONES = "1234567"
_MENSAJES = (
    "Ingresar nuevamente",
    " ingresado ya existe!",
    " debe ser expresado en números!"
)
_ERROR = "** ERROR! {}{} **\n"
ERRORES = (
    _ERROR.format(_MENSAJES[0], "una opción válida."),
    _ERROR.format(_MENSAJES[0], "el RUC"),
    _ERROR.format(_MENSAJES[0], "el DNI"),
    _ERROR.format("El precio", _MENSAJES[2]),
    _ERROR.format("El stock", _MENSAJES[2]),
    _ERROR.format("", "retornando al menu!")
)
OK = "Datos ingresados correctamente!\n", "Operación realizada!\n"

menu_principal = (
    "Menú Principal\n"
    "1. Registrar Proveedor\n"
    "2. Registrar Cliente\n"
    "3. Registrar Producto\n"
    "4. Realizar una compra\n"
    "5. Realizar una venta\n"
    "6. Reportes\n"
    "7. Salir\n"
)
menu_reportes = (
    "Reportes\n"
    "1. Producto\n"
    "2. Clientes\n"
    "3. Proveedores\n"
    "4. Consultar produco\n"
    "5. Productos sin stock\n"
    "6. Ventas por cliente\n"
    "7. Regresar al menú principal\n"
)

rucs, proveedores = [], []
dnis, nombres, direcciones, ventas = [], [], [], []
productos, stocks, precios = [], [], []

while True:
    print(menu_principal)
    opcion = input("> ")
    if opcion == "7":
        break
    if opcion not in OPCIONES:
        print(ERRORES[0])
        continue
    if opcion == "1":
        while True:
            ruc = input("RUC: ")
            if ruc not in rucs and len(ruc) == 11 and ruc.isdigit():
                rucs.append(ruc)
                break
            print(ERRORES[1])
        proveedor = input("Proveedor: ")
        proveedores.append(proveedor)
        print(OK[0])
    elif opcion == "2":
        while True:
            dni = input("DNI: ")
            if dni not in dnis and len(dni) == 8 and dni.isdigit():
                dnis.append(dni)
                break
            print(ERRORES[2])
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        nombres.append(nombre)
        direcciones.append(direccion)
        ventas.append([])
        print(OK[0])
    elif opcion == "3":
        while True:
            producto = input("Producto: ")
            if producto not in productos:
                productos.append(producto)
                break
            print(ERRORES[2])
        while True:
            precio = input("Precio: ")
            if (
                precio.isdigit() and not precio.startswith("-")
                and precio != "0"
            ):
                precios.append(float(precio))
                break
            print(ERRORES[3])
        while True:
            stock = input("Stock: ")
            if stock.isdigit() and not stock.startswith("-") and stock != "0":
                stocks.append(int(stock))
                break
            print(ERRORES[4])
        print(OK[0])
        pass
    elif opcion == "4":
        while True:
            ruc = input("RUC: ")
            if ruc not in rucs:
                print(ERRORES[-1])
                break
            idx = rucs.index(ruc)
            print(f"Proveedor: {proveedores[idx]}")
            producto = input("Producto: ")
            if producto not in productos:
                print(ERRORES[-1])
                break
            idx = productos.index(producto)
            cantidad = input("Cantidad: ")
            if not cantidad.isdigit() or cantidad.startswith("-") or cantidad == "0":
                print(ERRORES[-1])
                break
            stocks[idx] += int(cantidad)
            print(OK[1])
            continuar = input("Desear continuar? (s/n)").lower()
            if continuar in "no":
                break
    elif opcion == "5":
        while True:
            dni = input("DNI: ")
            if dni not in dnis:
                print(ERRORES[-1])
                break
            idx_ = dnis.index(dni)
            print(f"Cliente: {nombres[idx_]}")
            producto = input("Producto: ")
            if producto not in productos:
                print(ERRORES[-1])
                break
            idx = productos.index(producto)
            print(f"Producto: {productos[idx]} | Precio: {precios[idx]}")
            cantidad = input("Cantidad: ")
            if not cantidad.isdigit() or cantidad.startswith("-") or cantidad == "0":
                print(ERRORES[-1])
                break
            if stocks[idx] <= 0 or int(cantidad) > stocks[idx]:
                print(ERRORES[-1])
                break
            stocks[idx] -= int(cantidad)
            ventas[idx_].append(int(cantidad) * precios[idx])
            print(OK[1])
            continuar = input("Desear continuar? (s/n)").lower()
            if continuar in "no":
                break
    elif opcion == "6":
        while True:
            print(menu_reportes)
            opcion = input("> ")
            if opcion == "7":
                break
            if opcion not in OPCIONES:
                print(ERRORES[0])
                continue
            if (
                len(proveedores) == 0 or
                len(dnis) == 0 or
                len(rucs) == 0
            ):
                print("No hay datos que mostrar aún!")
                continue
            if opcion == "1":
                print("Productos")
                for i, producto in enumerate(productos):
                    print(f"* {producto} - {precios[i]:.2f} - {stocks[i]}")
            elif opcion == "2":
                print("Clientes")
                for nombre in nombres:
                    print(f"- {nombre}")
            elif opcion == "3":
                print("Proveedores")
                for proveedor in proveedores:
                    print(f"- {proveedor}")
            elif opcion == "4":
                producto = input("Producto a buscar: ")
                if producto not in productos:
                    print(ERRORES[-1])
                    continue
                idx = productos.index(producto)
                print(f"Nombre: {producto}")
                print(f"Precio: {precios[idx]:.2f}")
                print(f"Stock: {stocks[idx]}")
            elif opcion == "5":
                print("Productos sin stock")
                for i, producto in enumerate(stocks):
                    if producto == 0:
                        print(f"- {productos[i]}")
            elif opcion == "6":
                dni = input("DNI: ")
                if dni not in dnis:
                    print(ERRORES[-1])
                    break
                idx = dnis.index(dni)
                print("Ventas:")
                for venta in ventas[idx]:
                    print(f"- {venta}")
                print(f"Monto total: {sum(ventas[idx])}")
print("Hasta luego!")
