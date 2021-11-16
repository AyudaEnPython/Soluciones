## Banco de materiales para alumnos

Los alumnos de la universidad están buscando la manera de crear un
programa que les permita intercambiar materiales de las distintas
materias.

Para ello, le piden programar en Python un programa que almacene todos
los materiales disponibles.

El programa deberá además mantener información de alumnos registrados,
las carreras que existen y las materias por cada carrera para poder
clasificar los materiales.

De cada alumno se conoce el número de estudiante, cédula, nombre, fecha
de ingreso a la universidad y si está recibido o no.

De los materiales a compartir, se conoce un código alfanumércio,
título, el contenido (que en este caso siempre será texto), la materia
a la que pertenece, el alumno que lo publicó y la clasificación del
material.

De las carreras se conoce el código, nombre y facultada a la que
pertenecen.

De las materias se conoce el código, nombre, semestre y carrera a la
que pertenece.

### Requerimientos funcionales:

1. Registrar un alumno. Se deberá validar que no exista otro alumno con
    esa misma cédula.

2. Registrar material. Se deberá validar que no exista otro material
    con ese mismo código. El alumno que lo publica deberá estar
    previamente registrado.

3. Dada una materia, listar todos sus materiales. Deberá mostrar
    unicamente el código y el título del material.

4. Ver documento. Se ingresa el código de documento y se muestra la
    siguiente información:

       CARRERA:
       MATERIA:
       CALIFICACIÓN:
       TÍTULO:
       CONTENIDO:

5. Mostrar la cantidad de materiales por carrera.

6. Dada una calificación, listar los materiales que obtuvieron una
    calificación mayor o igual a ésta. Deberá mostrar únicamente el
    código, el título del material, la materia y la carrera.

7. Listar los alumnos que aportaron materiales. Si un mismo alumno
    aportó más de un material, deberá aparecer una sola vez.

8. Mostrar el/los alumnos que aportaron más materiales (requerimiento
    opcional).

9. El programa deberá ofrecer un menú de opciones para acceder a toas
    las funcionalidades y una opción adicional que permita salir del
    programa.

10. Deberá persistir los datos mediante serialización binaria.