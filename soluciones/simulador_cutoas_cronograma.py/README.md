# Problema Planteado

## Descripción

Un banco les ha encargado que generen un simulador de cuotas y
cronogramas de pago de préstamos personales para los clientes. Para
ello se han establecido las siguientes condiciones:

- El programa termina cuando el cliente no quiere hacer más 
  soluciones.
- La primera vez el cliente debe ingresar sus apellidos, nombres y DNI.
- Luego iniciará la simulación y el programa solicitará:
    - Monto del préstamo, el cual debe estar entre 5000 y 3000 soles
    - Los días de pago, que pueden ser los 15 o 25 de cada mes, a
      partir del mes siguiente al desembolso.
    - La fecha de desembolsos se asumirá como la fecha del día.

La relación entre los montos, cuotas y tasas se muestra en el
siguiente cuadro:

| Monto del préstamo | Cuotas | Tasa Efectiva Anual|
|--------------------|--------|--------------------|
|   [5000 - 10000]   |   12   |        26%         |
|  ]10000 - 15000]   |   18   |        24%         |
|  ]15000 - 20000]   |   24   |        22%         |
|  ]20000 - 25000]   |   30   |        20%         |
|  ]25000 - 30000]   |   36   |        18%         |


## Generación del cronograma de pagos

El factor se calcula de la siguiente manera:


| Tasa     |     18% |
|----------|---------|
| Cuotas   |      12 |
| Préstamo |10,000.00|
| Cuota    |  909.84 |


| periodo | fecha_pago | fecha_vencimiento | dias | capital | amortizacion | interes | cuota |
|---------|------------|-------------------|------|---------|--------------|---------|-------|
|   01    | 2020-05-15 |        2020-06-25 |   31 |  9254.4 |        745.6 |   200.0 | 945.6 |
|   02    | 2020-05-15 |        2020-07-25 |   30 | 8493.89 |       760.51 |  185.09 | 945.6 |
|   03    | 2020-05-15 |        2020-08-25 |   31 | 7718.17 |       775.72 |  169.88 | 945.6 |
|   04    | 2020-05-15 |        2020-09-25 |   31 | 6926.93 |       791.24 |  154.36 | 945.6 |
|   05    | 2020-05-15 |        2020-10-25 |   30 | 6119.87 |       807.06 |  138.54 | 945.6 |
|   06    | 2020-05-15 |        2020-11-25 |   31 | 5296.67 |        823.2 |   122.4 | 945.6 |
|   07    | 2020-05-15 |        2020-12-25 |   30 |  4457.0 |       839.67 |  105.93 | 945.6 |
|   08    | 2020-05-15 |        2021-01-25 |   31 | 3600.54 |       856.46 |   89.14 | 945.6 |
|   09    | 2020-05-15 |        2021-02-25 |   31 | 2726.95 |       873.59 |   72.01 | 945.6 |
|   10    | 2020-05-15 |        2021-03-25 |   28 | 1835.89 |       891.06 |   54.54 | 945.6 |
|   11    | 2020-05-15 |        2021-04-25 |   31 |  927.01 |       908.88 |   36.72 | 945.6 |
|   12    | 2020-05-15 |        2021-05-25 |   30 |     0.0 |       927.01 |   18.54 | 945.6 |


La columna d1 se calcula de la siguiente manera:

- Para la primera cuota es la diferencia de días entre la fecha de
  vencimiento de la primera cuota y la fecha de desembolso.
- A partir de la segunda es la diferencia entre fechas de vencimiento.

Por ejemplo, para la segunda cuota es la:

    fecha_vto_cuota2 - fecha_vto_cuota1

El cáculo para las siguientes cuotas es de la misma forma. Los
intereses de la cuota se calculan como:

    capital * factor_cuota

El capital en la primera cuota es el monto del préstamo:

    amortizacion = cuota - intereses de la cuota

Desde la segunda cuota:

    capital = capital de cuota anterior - amortizacion de cuota anterior


> **NOTA** 
> 
> El enunciado original no presenta una clara descripción sobre
> la generación de cronogramas.