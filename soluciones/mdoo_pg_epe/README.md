# Enunciado Original

## MDOO PG y EPE

Modelamiento y Diseño Orientado a Objetos es un curso abierto para
alumnos de la modalidad de Pre-Grado y EPE. Para cada alumno se
registra su código, nombre completo, modalidad de estudio y
dependiendo de este dato se le asigna un sistema de califacación.

Para los alumnos de Pre-Grado:

```
NF = 0.15 PC1 + 0.15 PC2 + 0.40 PF + 0.30 EB
```

Para alumnos de EPE:

```
NF = 0.20 PC1 + 0.20 PC2 + 0.30 TP + 0.30 TF
```

En donde:

NF: Nota final
PF: Proyecto final
TP: Trabajo Parcial
PC1 y PC2:  Prácticas calificadas
EB: Examen Final
TF: Trabajo Final

Se desea desarrollar una aplicación que controle las notas de un grupo
de estudiantes de ambas modalides.

Se pide lo siguiente:

1. Implementar la clase para manejar las calificaciones de alumnos de
  ambas modalidades.
2. Implementar una clase que controle el registro de los dos tipos de
  calificaciones. Esta clase deberá grabar la información en un archivo
  Excel.
3. Diseñar GUIs e implementar el ingreso de datos de las calificaciones.
4. Completar la aplicación realizando las siguientes validaciones y
  acciones:
  - No pueden existir alumnos con códigos duplicados.
  - Permitir ingresar notas únicamente entre 0 y 20 con decimales.
  - Emitir un listado con todos los alumnos del curso, modalidad de
    estudio y nota final.

Subir lo siguiente:

- Programa Python (NombreAlumno.ipynb)
- Archivo Excel que maneja el programa python. (Datos.xlsx)

> __**NOTA**__: No es adecuado el uso de notebooks, se opta por
> cambiar el requerimiento.
