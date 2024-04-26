# UNAC

## Facultad de Economía

1. (4 puntos) Una empresa ha recibido una donación en dinero que lo repartirá entre cinco áreas. Cada área recibirá una parte de la donación equivalente a:

   - Área de producción: 25% del monto de la donación.
   - Área de contabilidad: 40% del monto total recibio entre las áreas de marketing y soporte.
   - Área de marketing: 15% del monto total recibido entre las áreas de producción y soporte.
   - Área de soporte: 20% del monto de la donación.
   - Área de recursos humanos: lo que queda del monto de la donación.

   Dado el importe de la donación, diseñe un algoritmo que determine el monto de dinero que recibirá cada área.

   > [Ir a la solución](./sol_01.py)

2. (4 puntos) En una provincia los límites de velocidad son los siguientes:

   - Menos de 60 Km/h - Velocidad permitida
   - De 60 a 65 Km/h - Peligro en el límite de velocidad
   - Más de 65 Km/h - Ha superado el límite de velocidad

   Desarrolle un pseudocódigo en Python que lea la velocidad y escriba un mensaje en cada caso de la velocida y la multa.

   Debe tener en cuenta que, si la velocidad es mayor a 65 Km/h, se aplicará una multa de:

   - 65 a 75 Km/h - S/.300.00
   - 76 a 85 Km/h - S/.750.00
   - 86 a 100 Km/h - S/.1500.00
   - Más de 100 Km/h - S/.3700.00

   > [Ir a la solución](./sol_02.py)

3. (7 puntos) Una empresa evalúa a sus empleados bajo dos criterios: puntualidad y rendimieno. En cada caso el empleado recibe un puntaje que va de 1 a 10, de acuerdo a los siguientes criterios:

   **Puntaje por puntualidad**: - está en función de los minutos de tardanza de acuerdo a la siguiente tabla:

   | Minutos de tardanza | Puntaje |
   | :-----------------: | :-----: |
   |          0          |   10    |
   |        1 a 2        |    8    |
   |        3 a 5        |    6    |
   |        6 a 9        |    4    |
   |      Más de 9       |    0    |

   **Puntaje por rendimiento**: - está en función de la cantidad de observaciones efectuadas al empleado por no cumplir sus obligaciones de acuerdo con la siguiente tabla:

   | Número de observaciones | Puntaje |
   | :---------------------: | :-----: |
   |            0            |   10    |
   |            1            |    8    |
   |            2            |    5    |
   |            3            |    1    |
   |        Más de 3         |    0    |

   El puntaje total del empleado es la suma del puntaje por puntualidad más el puntaje por rendimiento. Basándose en el puntaje total, el empleado recibe una bonificación anual de acuerdo con la siguiente tabla:

   |   Puntaje   |    Bonificación    |
   | :---------: | :----------------: |
   | Menos de 11 | S/. 2.5 por punto  |
   |   11 a 13   | S/. 5.0 por punto  |
   |   14 a 16   | S/. 7.5 por punto  |
   |   17 a 19   | S/. 10.0 por punto |
   |     20      | S/. 12.5 por punto |

   Dados los minutos de tardanza y el número de observaciones de un empleado, diseñe un programa que determine el puntaje por puntualidad, el puntaje por rendimiento, el puntaje total y la bonificación que le corresponde.

   > [Ir a la solución](./sol_03.py)

4. (5 puntos) Diseñe un programa que imprima y sume n términos de la siguiente serie. Los términos serán mostrados en una columna a razón de un término por fila.

   1/2, 4/4, 7/6, 10/8, ...

   > [Ir a la solución](./sol_04.py)

---

> \***\*NOTA\*\***: En el ejericio 2 hay un error en el enunciado.
