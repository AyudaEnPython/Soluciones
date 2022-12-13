# Enunciado Original

Crear un archivo en Python y desarrollar una aplicacion, donde se debe utilizar
todas las estructuras que crea necesarias para dar solución al caso planteado.

La empresa "My Market", desea una aplicación para controlar la venta de sus
productos. Para esto solicita un menú Principal, con las siguientes opciones:

    Menu Principal
    1. Registar Proveedor.
    2. Registrar Cliente.
    3. Registar Producto.
    4. Realizar una Compra.
    5. Realizar una Venta.
    6. Reportes.
    7. Salir.

**Opción 1.** Se debe registrar al Proveedor: RUC (no se repita) y Nombre.

**Opción 2.** Se debe registrar al Cliente: DNI (no se repita), Nombre y Dirección.

**Opción 3.** Se debe registrar un nuevo producto, con los siguientes datos: Nombre
(no se repita), Precio_Venta (> 0), Stock (>= 0).

**Opción 4.** Se debe realizar una compra de la siguiente manera:
- Se debe solicitar el Ruc del Proveedor y se debe mostrar su Nombre. Si no esta
  se debe registrar.
- Se ingresarán los productos que se desean comprar, Nombre del Producto y
  Cantidad (> 0). Esta Cantidad se debe aumentar al stock del producto. Si el
  producto no está debes registrarlo.
- El ingreso de los productos se hará hasta que el usuario lo desee.

**Opción 5.** Se debe realizar una Venta de la siguiente manera:
- Se debe solicitar el DNI del cliente y se debe mostrar su Nombre y Dirección. Si no
  esta se debe registrar.
- Se ingresarán el nombre del producto que se desean Vender y mostrará el precio de
  venta, luego ingresar la Cantidad (> 0). Se debe verificar que exista stock suficiente,
  si existe se reduce el stock del producto y calcular el subtotal a pagar
  (precio * cantidad), caso contrario mostrar un mensaje. Verificar.
- El ingreso de los productos se hará hasta que el usuario lo desee. En este momento
  debe mostrar el Monto tola de la venta y almacenarlo.

**Opción 6.** Para la opción de Reportes se debe mostrar el siguiente menú:

    Reportes
    1. Listado de Productos (Nombre - Precio - Stock)
    2. Listado de clientes
    3. Listado de Proveedores
    4. Ingresar un nombre de Producto y mostrar sus datos
    5. Listado de Productos con stock cero (0).
    6. Listado de Ventas por cliente (Ingresar el DNI del cliente y mostrar
      sus ventas: Monto Total)
    7. Regresar al menú principal.
