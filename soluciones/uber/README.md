# Enunciado Original

Se desea construir un objeto tipo **`Uber`** con los siguientes atributos:
- Número de placa
- Marca
- Año
- Estado del vehículo (libre, ocupado, reparación)
- Tipo de vehículo (económico, premium)
- Cantidad de viajes realizados
- Monto de viaje (el actual)
- Acumulado de monto por viajes
- Calificación (de 0 a 5 estrellas). Inicialmente, los conductores empiezan
  con 5 estrellas.

Los métodos a implementar son:
- `mostrar()`, que imprime todos los atributos del objeto
- `reset()`, que pone en cero la cantidad de viajes realizados
- `enviar_reparación()`, que actualiza el estado del camión a _reparación_
- `recibir_reparación()`, que actualiza el estado del camión a _libre_
- `viaje(kilometros)`, que aumenta en 1 la cantidad de viajes realizados y
  calcula el monto a pagar por el viaje, de acuerdo a la cantidad de kilómetros
  de viaje. Considere que los viajes económicos se pagan a 300 por kilómetro y
  los premium a 500 por kilómetro.
- `set_calificación(calificacion)`, que calcula el **`promedio`** de estrellas que tiene el
  objeto basado en la calificación actual y la nueva calificación recibida.
- Además, debe existir los métodos `get_tipo()`, `get_estado()` y `get_viajes()`
  que retornan los datos correspondientes

> _**Nota**_: El diseño no es el correcto, se opta por realizar cambios.