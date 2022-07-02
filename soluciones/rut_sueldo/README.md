# Enunciado Original

## Descripción de las clases:

## Clase: Rut
- Atributos: rut y dv (dígito verificador)
- Métodos: mostrarRut() que devuelva el rut en el siguiente formato:
  12345678-9

## Clase: Fecha
- Atributos: dd, mm y aa (dd:día, mm:mes, y aa: año)
- Métodos: mostrarFecha() que devuelva la fecha en el siguiente formato:
  dd/mm/aaaa
- Importante: Este dato corresponde a la fecha de ingreso del empleado a
  la empresa.

## Clase: Empleado(Padre)
- Atributos: id, rut, apellidos, nombres, género (M o F) y fecha
- Métodos:
  - mostrarEmpleado()
  - mostrarGenero() > Masculino o Femenino, según corresponda
- Importante: los atributos rut y fecha son "instancias" a las clases
  correspondientes

## Clase: Sueldo(Hija)
- Atributos: id, nombreHaber, montoHaber
- Métodos: mostrarSueldo()

## Desde el main:
- Crear un lista con objetos de tipo Sueldo
- Debes crear a lo menos cinco(5) objetos iniciales (inventados por ti)

> __**NOTE**__: Lo planteado por el enunciado no sigue PEP8 y las clases
> están mal diseñadas. Se opta por rediseñar.
