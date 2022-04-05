Realizar un programa que le permita emular un listado de calificaciones de estudiantes
con los cálculos que se evalúan al calificar la nota final de una materia en la
Universidad de Guayaquil, en caso de ambiguedad leer el reglamento de calificaciones o
guiarse con el SIUG.

## Detalle del programa:

El programa deberá crear un Menu que tenga lo siguiente:

1. Crear un estudiante con nombre, apellido, cedula. Estos estarán en un diccionario
  donde la llave será la cedula (int), y los valores serán dos str nombre y apellido, y
  el tercer valor será una lista con las notas que podrán agregar en el siguiente literal.

2. Agregar/Modificar notas a usuarios con nota 1P y nota 2P y notas adicionales en caso
  de ser necesarias (Mejoramiento o Recuperación) Aplicar todas las reglas que tuvimos en
  cuenta en el primer parcial.

3. Imprimir registro de notas:
    a. Si hay alumnos que no tengan sus notas enlistarlos al final

4. Eliminar estudiantes con la cedula. Si ingresan una cedula que no existe deberán decirle
  al usuario que no se encontró la cedula.

5. Salir.