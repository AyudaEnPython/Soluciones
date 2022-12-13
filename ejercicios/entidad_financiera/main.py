"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Simular una entidad financiera con las siguientes características:
Menu Principal
1. Registrar cliente
2. Realizar Operaciones
3. Consultas
4. Salir

Se deben guardar el nombre del cliente, nro de cuenta, total de
depositos, total de retiros.

NOTE: el enunciado es demasiado general y solo se tiene permitido usar
    variables, listas, while, for, if-elif-else (esto conlleva a varias
    partes repetidas).
"""

BANCO_ID = 560
ADMIN = "admin", "admin"
OPCIONES = "1234", "12345"
INDICACIONES = "", "Depósito: ", "Retiro: ", "Transferencia: "
_MENSAJE = "Ingresar nuevamente"
_ERROR = "** ERROR! {}{} **\n"
ERRORES = (
    _ERROR.format(_MENSAJE, "una opción válida."),
    _ERROR.format(_MENSAJE, "un PIN de 4 dígitos."),
    _ERROR.format(_MENSAJE, "el DNI"),
    _ERROR.format("", "El DNI ingresado no existe!"),
    _ERROR.format("", "El PIN ingresado es incorrecto!"),
    _ERROR.format("", "El N° de cuenta no existe!"),
    _ERROR.format("", "El monto debe ser expresado en números!"),
    _ERROR.format("", "Usuario incorrecto!"),
    _ERROR.format("", "Contraseña incorrecta!"),
    _ERROR.format("", "No hay datos que mostrar aún!"),
    _ERROR.format("", "Operación incorrecta!"),
)
OK = "Datos ingresados correctamente!\n", "Operación realizada!\n"

menu_principal = (
    "\t---- Menú Principal ----\n"
    "1. Registrar cliente\n"
    "2. Realizar operaciones\n"
    "3. Consultas\n"
    "4. Salir\n"
)
menu_operaciones = (
    "\t---- Menú de Operaciones ----\n"
    "1. Depósito\n"
    "2. Retiro\n"
    "3. Transferencia\n"
    "4. Regresar al menú principal\n"
)
menu_consultas = (
    "\t---- Menú de Consultas ----\n"
    "1. Consultar Datos\n"
    "2. Monto Total de depósitos y retiros\n"
    "3. Cliente con mayor cantidad de depósitos\n"
    "4. Cliente con mayor cantidad de retiros\n"
    "5. Regresar al menú principal\n"
)

clientes, dnis, pins = [], [], []
cuentas, saldos, movimientos = [], [], []
_id = 1

while True:
    print(menu_principal)
    opcion = input("> ")
    if opcion == "4":
        break
    if opcion not in OPCIONES[0]:
        print(ERRORES[0])
        continue
    if opcion == "1":
        cliente = input("Nombre: ")
        while True:
            dni = input("DNI: ")
            if dni not in dnis and len(dni) == 8 and dni.isdigit():
                dnis.append(dni)
                break
            print(ERRORES[2])
        while True:
            pin = input("PIN: ")
            if len(pin) == 4 and pin.isdigit():
                pins.append(pin)
                break
            print(ERRORES[1])
        clientes.append(cliente)
        cuentas.append(f"01-{BANCO_ID}-{_id:06}")
        saldos.append(0)
        movimientos.append([])
        print(OK[0])
        _id += 1
    elif opcion == "2":
        while True:
            print(menu_operaciones)
            opcion = input("> ")
            if opcion == "4":
                break
            if opcion not in OPCIONES[0]:
                print(ERRORES[0])
                continue
            if opcion in OPCIONES[0][:-1]:
                dni = input("DNI: ")
                if dni not in dnis:
                    print(ERRORES[3])
                    continue
                pin = input("PIN: ")
                if pin not in pins:
                    print(ERRORES[4])
                    continue
                monto = input(INDICACIONES[int(opcion)])
                if not monto.isdigit():
                    print(ERRORES[6])
                    continue
                monto = float(monto)
            if opcion == "1":
                if monto < 0:
                    print(ERRORES[-1])
                    continue
                saldos[dnis.index(dni)] += monto
                movimientos[dnis.index(dni)].append(monto)
                print(OK[1])
            elif opcion == "2":
                if monto > saldos[dnis.index(dni)]:
                    print(ERRORES[-1])
                    continue
                saldos[dnis.index(dni)] -= monto
                movimientos[dnis.index(dni)].append(monto * -1)
                print(OK[1])
            elif opcion == "3":
                if monto > saldos[dnis.index(dni)]:
                    print(ERRORES[-1])
                    continue
                cuenta = input("N° de cuenta: ")
                encontrado = False
                for n in cuentas:
                    if n == cuenta:
                        encontrado = True
                if not encontrado:
                    print(ERRORES[5])
                    continue
                saldos[dnis.index(dni)] -= monto
                movimientos[dnis.index(dni)].append(monto * -1)
                saldos[cuentas.index(cuenta)] += monto
                movimientos[cuentas.index(cuenta)].append(monto)
                print(OK[1])
    elif opcion == "3":
        usuario = input("Usuario: ")
        if usuario != ADMIN[0]:
            print(ERRORES[7])
            continue
        password = input("Contraseña: ")
        if password != ADMIN[1]:
            print(ERRORES[8])
            continue
        while True:
            print(menu_consultas)
            opcion = input("> ")
            if opcion == "5":
                break
            if opcion not in OPCIONES[1]:
                print(ERRORES[0])
                continue
            if opcion == "1":
                dni = input("DNI: ")
                if dni not in dnis:
                    print(ERRORES[3])
                    continue
                print(f"Nombre: {clientes[dnis.index(dni)]}")
                print(f"N° de cuenta: {cuentas[dnis.index(dni)]}")
                print(f"Saldo: {saldos[dnis.index(dni)]}")
                print(f"Movimientos:\n{movimientos[dnis.index(dni)]}")
            if len(movimientos) == 0:
                print(ERRORES[-2])
                continue
            elif opcion in OPCIONES[0][1:]:
                min_ = i_max = max_ = i_min = 0
                total_depositos = total_retiros = 0
                for i, movimiento in enumerate(movimientos):
                    k_max = k_min = 0
                    if not movimiento:
                        break
                    for monto in movimiento:
                        if monto > 0:
                            total_depositos += monto
                            k_max += 1
                        if monto < 0:
                            total_retiros +=  monto
                            k_min += 1
                    if k_max > max_:
                        max_ = k_max
                        i_max = i
                    if k_min > min_:
                        min_ = k_min
                        i_min = i
            if opcion == "2":
                print(f"Monto total de depósitos: {total_depositos}")
                print(f"Monto total de retiros: {total_retiros * -1}")
            if opcion == "3":
                print(f"Cantidad de depósitos: {max_}")
                print(f"Cliente: {clientes[i_max]}")
            if opcion == "4":
                print(f"Cantidad de retiros: {min_}")
                print(f"Cliente: {clientes[i_min]}")
print("Hasta luego!")
