# Enunciado Original

Un NIF, es un NÚMERO DE IDENTIFICACIÓN FISCAL (NIF) otorgado por la Unión Europea
a los ciudadanos mayores de 15 años. Es el equivalente al Rut o número de identificación
chileno. Este NIF tiene ciertos beneficios para quien lo obtiene.

La estructura del NIF en España, es la siguiente:
- 99999999-RTX
- 03034567-XXY
- 12312345-CCU
- 00000001-03F

En el registro de ciudadanos pertenecientes a la Unión Europea de España, del pueblo del
sur de Andalucía, se requiere construir un programa con un menú que contenga las siguientes
opciones:

Opción 1 Grabar:
- Corresponde a guardar ciertos datos de una persona, entre ellos: NIF, nombre, año de
  nacimiento, estado conyugal y si pertenece a la Unión Europea o no.
- Debe verificar que el NIF sea correcto, que el nombre tenga mínimo 8 caracteres y que la
  edad sea mayor igual a 15 (considerar año actual).

Opción 2 Buscar:
- Corresponde a buscar a una persona por su NIF y mostrar toda su información almacenada.
- Además, debe mostrar si la persona pertenece o no a la Unión Europea.

Opción 3 Imprimir certificados:
- Esta opción permite imprimir los certificados de año de nacimiento, estado conyugal,
  pertenencia a la Unión Europea. Estos deben ser previamente ingresados desde el teclado.
  Al imprimir el certificado, debe mostrar el nombre del certificado, el NIF respectivo y
  nombre de la persona con sus datos.
- El precio por cobrar por este documento es aleatorio y el rango de valores va desde los
  10 euros hasta los 100 euros.

Opción 4:
- Salir. Corresponde a salir del programa emitiendo un mensaje de salida. Considere, además,
  su nombre y apellido y la versión del programa.

## Instrucciones Generales:

Escribir un programa que contenga dos archivos:

- Principal, en el cual, debe contener un menú con las opciones para acceder a cada función
  requerida. Sólo, considere el ingreso de datos y el despliegue de información.
- Funciones: Debe contener todos los procesos y validaciones de los requerimientos. Crearlos
  en otro archivo e importarlos.
- Crear un arreglo que permita almacenar los valores solicitados.
- Usar Try except en caso de requerirlo.

## Datos de prueba para testear programa:

|Nro Caso | NIF      | Nombre | Año  | Estado Conyugal | Pertenece a la UE |
|---------|----------|--------|------|-----------------|-------------------|
| 1       | 12344321 | Juan   | 2000 | Soltero         | Si                |
| 2       | 12345678 | Ana    | 2010 | Soltero         | No                |
| 3       | 87654321 | Adams  | 1990 | Casado          | Si                |
