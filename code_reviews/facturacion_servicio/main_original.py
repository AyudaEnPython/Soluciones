"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# facturacion servicio de electricidad

print("Menú")
print("opcion 1: tarifa residencial")
print("opcion 2: tarifa comercial")
print("opcion 3: salir del programa")

opcion = int(input("ingrese una opcion del menu (en numero): "))

if opcion == 1:
    print("tarifa residencial")
    Cargo_fijo = 299.37
    Precio_kw = 3.37
    lectura_anterior = int(input("ingrese lectura anterior: "))
    lectura_actual = int(input("ingrese lectura actual: "))
    consumo = lectura_actual - lectura_anterior
    
    subtotal = Precio_kw*consumo+Cargo_fijo
    print(f"subtotal: {subtotal}")
    Impuesto = 1.21
    print("impuesto: iva 21%")
    
    total = subtotal * Impuesto

    while consumo < 250:
        descuento = 150
        bonif = total - descuento
        print(f"""su consumo es de {consumo}kw, su monto es de ${total}
           recibe bonificacion de ${descuento} y debe abonar ${bonif}""")
        break
    else:
        print(f"su consumo es {consumo}kw, esta excedido y debera abonar ${total}")
    
elif opcion == 2:
    print("tarifa comercial")
    Cargo_fijo = 315.25
    Precio_kw = 4.55
    lectura_anterior = int(input("ingrese lectura anterior: "))
    lectura_actual = int(input("ingrese lectura actual: "))
    consumo = lectura_actual - lectura_anterior
    
    subtotal = Precio_kw*consumo+Cargo_fijo
    print(f"subtotal: {subtotal}")
    Impuesto = 1.26
    print("impuesto: iva 21% , ing. brutos 5%")
    
    total = subtotal * Impuesto

    while consumo < 150:
        descuento = 20
        bonif = total - descuento
        print(f"""su consumo es de {consumo}kw, su monto es de ${total}
        recibe bonificacion de ${descuento} y debe abonar ${bonif}""")
        break
    else:
        print(f"su consumo es {consumo}kw, esta excedido y debera abonar ${total}")
    
elif opcion == 3:
    print("ha decidido salir. gracias por utilizar el programa")
    
else:
    print("error. intente de nuevo ingresando una opcion valida del menu")