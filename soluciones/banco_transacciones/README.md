# Enunciado Original

Un banco desea llevar el registro de operaciones que realizan los cajeros
y luego emitir el reporte de cierre del dia.

Los tipos de transacciones que atienden los cajeros son:

|Código|Descripción  |
|------|-------------|
|D     |Depósito     |
|R     |Retiro       |
|T     |Transferencia|

La información que se registra para cada transacción es la siguiente:

|Campo                  |Validación                                         |
|-----------------------|---------------------------------------------------|
|DNI del cliente        |Se debe validar que no sea vacio                   |
|Tipo de transacción    |Se debe validar que sean los permitidos            |
|Monto de la transacción|Debe ser un número positivo mayor 0 y con decimales|

Al iniciar el programa el cajero deberá ingresar el saldo inicial del día (dato
mayor o igual a 0) y luego procederá a ingresar las operaciones hasta que decida
que ya no tiene más transacciones por ingresar.

Una vez finalizado el ingreso de datos, el sistem calculará y mostrará el saldo
final, considerando:
- Los depósitos suman al saldo
- Los retiros restan al saldo
- Las transferencias no afectan al saldo

Finalmente se debe mostrar el siguiente resumen estadístico

<table border="1">
  <tr>
    <td>Transacción</td>
    <td># Operaciones</td>
    <td>Transacción Máxima</td>
    <td>Transacción Mínima</td>
    <td>Total Transacciones</td>
  </tr>
  <tr>
    <td>Depósito</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Retiro</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Transferencia</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</table>
