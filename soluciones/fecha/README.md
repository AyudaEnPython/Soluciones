# Enunciado Original

Una fecha se puede representar por un número entero de 8 dígitos en la
forma DDMMAAAA. Por ejemplo, el 25 de agosto del 2021 se representa por
el número 25082021. Para realizar las operaciones habituales con fechas
representadas de esa manera se necesita escribir un módulo (en el
archivo fecha.py) con las funciones indicadas en la siguiente tabla:

| Ejemplo 1                         | Resultado         |
|-----------------------------------|-------------------|
| diasMes(2, 2021)                  | 28                |
| esFecha(10082021)                 | True              |
| comparar(10802021, 31072021)      | 1 (1° fecha > 2°) |
| escribir(25082021) escribe línea: | 25 agosto 2021    |

| Ejemplo 2                         | Resultado          |
|-----------------------------------|--------------------|
| diasMes(2, 2020)                  | 29                 |
| esFecha(31092021)                 | False              |
| comparar(31072021, 10082021)      | -1 (1° fecha < 2°) |
| escribir(1032007) escribe línea:  | 1 marzo 2021       |

Notas. La función comparar entrega 0 si las fechas son iguales

- Escriba el módulo fecha. Todas las funciones deben tener su receta de
  diseño completa incluyendo las precondiciones que validen los parámetros
  y al menos dos pruebas a los ejemplos anteriores (salvo la función escribir
  que escribe una línea en la pantalla pero no devuelve ningún resultado).

- Escriba un programa (el archivo programaFechas.py) que use las funciones
  del módulo fecha para establecer el diálogo indicado en el siguiente ejemplo.

        Fecha1?1032007
        1 marzo 2007
        Fecha2?10082000
        10 agosto 2000
        Menor fecha:
        10 agosto 2000

Nota. Si alguna de las fechas está incorrecta, el programa termina escribiendo
el mensaje "fecha incorrecta".
