# Enunciado Original

El curso de Análisis y Diseño Orientado a Objetos (ADOO) en el centro de entrenamiento
_Singular Tech_ se califica de la siguiente manera:

- Se toma 4 evaluaciones continuas los cuales se califican entre 0 y 20.
- La nota final se calcula como el promedio de las 3 mejores evaluaciones continuas.
- Para aprobar se requiere una nota final mayor o igual a 15.

Se pide desarrollar un sismta en Python que realice lo siguiente:

- Mostrar un menú con las siguientes opciones:
  - [1] Registra califciaciones
  - [2] Reporte de calificaciones
  - [3] Estadísticas de calificaciones
  - [4] Salir

- Ingresar las calificaciones de un grupo de alumnos matriculados en ADOO. La información
  que se pide registrar para cada alumno es la siguiente:

  | Campo                       | Validación                                         |
  |-----------------------------|----------------------------------------------------|
  | Código de alumno            | Debe ser diferente de vacío y no se puede repetir  |
  | Nombre completo del alumno  | Debe ser diferente de vacío y no se puede repetir  |
  | Evaluación Continua 1 (EC1) | Debe ser un número de 0 a 20 con decimales         |
  | Evaluación Continua 2 (EC2) | Debe ser un número de 0 a 20 con decimales         |
  | Evaluación Continua 3 (EC3) | Debe ser un número de 0 a 20 con decimales         |
  | Evaluación Continua 4 (EC4) | Debe ser un número de 0 a 20 con decimales         |

- Listar el reporte de calificaciones en el cual debe figurar a parte de la información
  registrada, cúal de las evaluaciones continuas no fue considerada y la situación final
  del alumno (Aprobado o Desaprobado).

- Estadísticas de la nota final: Nota Máxima, Nota Mínima, Nota Promedio, Cantidad de
  aprobados, Cantidad de desaprobados.
