# Enunciado Original

Desarrolla un programa que permita gestionar los datos de venta de pasajes,
permitiéndoles consultar, registrar, modificar, eliminar y generar la
estadística

## Especificaciones LOGIN

- El código y contraseña debe ser verificado en el json, si se logra comprobar
  los datos de forma correcta accede al menú, en caso contrario entrega un
  mensaje indicando que no coincide el código y contraseña.

## Especificaciones mantenedor de venta de pasajes

- El __*número de venta*__ debe ser verificado en la base de datos antes de registra,
  en caso de existir debe mostrar un mensaje indicando que ya existe.

- El __*número de venta*__ debe ser validado antes de poder modificar o borrar una venta,
  en caso de no encontrarse registrado el número de venta, la aplicación debe
  mostrar un mensaje indicando que no está registrado.

- El __*número de venta*__ es válido entre 1 y 50.

- El __*número de pasajero*__ es válido entre 1 y 2.

- El __*número de destino*__ es válido entre 1 y 4.

- La __*cantidad*__ es válida entre 1 y 10.

- El neto no es ingresado (precio del producto * cantidad)

- El iva no es ingresado (neto * 0.19)

- El total no es ingresado (neto + iva)

> __*Importante*__: Al momento de listar las ventas, estas no deben mostrar el número de
> pasajero y el número de destino, sino que, debe aparecer el nombre del pasajero y el
> nombre del destino seleccionado.

## Estadística especifica 1

- Presenta la cantidad de registros solo de las ventas del pasajero 1.

## Estadística especifica 2

- Presenta la cantidad de registros solo de las ventas del pasajero 2.

### Diagrama Clase

    ,----------------------.                                                                                
    |Venta                 |                                                                                
    |----------------------|                                                                                
    |-numero: int          |                                                                                
    |-pasajero: int        |                                                                                
    |-destino: int         |       ,----------------------------------------------------.                        
    |-cantidad: int        |       |Funciones                                           |                        
    |-neto: int            |       |----------------------------------------------------|                        
    |-iva: int             |       |+d: DAO                                             |                        
    |-total:int            |       |+Funciones()                                        |                        
    |+Venta()              |       |-digitarTexto(cantidad: int, texto: str)            |   ,-------------------.
    |+getNumero(): int     |       |-digitarNumero(inicio: int, termino: int, text: str)|   |Principal          |
    |+setNumero(num: int)  |       |+menu()                                             |   |-------------------|
    |+getPasajero(): int   |-------|-registrar()                                        |---|+f: Funciones      |
    |+setPasajero(pas: int)| 1..*  |-modificar()                                        |   |+ejecutarPrograma()|
    |+getDestino(): int    |       |-eliminar()                                         |   `-------------------'
    |+setDestino(des: int) |       |-listarVentas()                                     |                        
    |+getCantidad(): int   |       |-Estadistica_pasajero1()                            |                        
    |+setCantidad(can: int)|       |-Estadistica_pasajero2()                            |                        
    |+getNeto(): int       |       |-salir()                                            |                        
    |+setNeto(net: int)    |       `----------------------------------------------------'                        
    |+getIva(): int        |          |                                                                      
    |+setIva(iva: int)     |          |                                                                     
    |+getTotal(): int      |          |                                                                    
    |+setTotal(tot: int)   |          |                                                                   
    `----------------------'          |                                                                      
              |                       |                                                                       
              |                       |                                                                       
              |    ,-----------------------------------.                                                     
              |    |DAO                                |                                                     
              |    |-----------------------------------|                                                     
              |    |+DAO()                             |                                                     
              |____|-conectar()                        |                                                     
              1..* |-desconectar()                     |                                                     
                   |+comprobarNumero(num: int): boolean|                                                     
                   |+registrarVenta(p: Persona)        |                                                     
                   |+modificarVenta(p: Persona)        |                                                     
                   |+eliminarVenta(num: int)           |                                                     
                   |+obtenerVentas(): tuple            |                                                     
                   |+obtenerPasajeros(): tuple         |                                                     
                   |+obtenerDestinos(): tuple          |                                                     
                   `-----------------------------------'            


> __*NOTE*__: El enunciado original no esta bien redactado, tanto del diagrama
> UNL como el diseño propuesto por el enunciado no es correcto.
> Se opta por cambiar todo.