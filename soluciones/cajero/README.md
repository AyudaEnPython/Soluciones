# Contenido

Se pide desarrollar en Python un programa para la siguiten situación:
Se trata de desarrollar un sistema que emule el funcionamiento de un
cajero automático con las siguientes funciones:

1. Al inicio el usuario introduce su número de cuenta (o tarjeta) y el
    NIP, el sistema debe validar que el NIP sea correcto.
2. El usuario tiene las siguientes opciones que el cajero muestra como
    menú:
    a. Hacer un retiro, en este caso se introduce la cantidad a retirar
        se debe validar que el saldo de la cuenta tenga suficiente
        dinero, si no se rechaza la operación.
    b. Hacer un depósito en efectivo, esto se agrega al saldo actual.
    c. Depositar un cheque a la cuenta (es un cajero moderno, puede
        recibir cheques) en este caso también se introduce el monto del
        cheque y se incrementa el saldo.
3. El usuario puede pedir consultar el saldo en cualquier momento.
4. El usuario puede pedir ver los últimos 5 movimientos (un movimiento
    es una operación sobre la cuenta) y el promedio de estos
    movimientos.
5. El usuario puede pedir saber cuál fue el movimiento más importante
    (en monto) de sus últimos 5 moviemientos (toma en cuenta el caso
    que haya menos de 5 movimientos o ninguno).
6. Al terminar una operación, el sistema regresa al menú principal
    donde haya una opción de salir del sistema, en este caso el sistema
    se despide del cliente.