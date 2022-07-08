# Enunciado Original

La academia preuniversitaria Cachimbo gestiona el pago semanal a sus profesores
considerando lo siguiente:
- Cada semana se debe registrar información: DNI del profesor, Nombre Completo,
  Función desempeñada y Horas trabajadas.
- Un profesor puede desempeñarse como Docente Principal (P), Docente Auxiliar (A)
  o Tutor (T).
- El número máximo de horas a trabajar por semana y la tarifa por hora depende del
  rol desempeñado por el profesor taly como se muestra en el siguiente cuadro:

  |Rol              |Número máximo de horas a trabajar|Tarifa por hora|
  |-----------------|---------------------------------|---------------|
  |Docente Principal|                              24 |         50.00 |
  |Tutor            |                              16 |         25.00 |
  |Docente Auxiliar |                              24 |         20.00 |

Se pide desarrollar un sistema en Python que realice lo siguiente:
- Registrar horas trabajadas en la semana por cada profesor
- Listar planilla de pago semanal
- Estadísticas de pagos por rol

Implementar las funcionalidades solicitadas considerando lo siguiente:
- Mostrar un menú con las acciones necesarias para controlar las acciones del sistema
- Registrar la información validando que un profesor no puede estar registrado más de
  una vez en la planilla semanal y que no puede exceder el máximo de horas asignado al
  rol que desempeña en la semana.
- La planilla de pago semanal debe listar a todos los profesores con su pago semanal
  y un resumen de pagos por rol.
- Las estadísticas de pago a considerar son: Pago Máximo, Pago Mínimo, Pago Promedio.

Usar: Funciones, Listas y Diccionarios.
