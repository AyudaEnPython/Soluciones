"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original ------------------------ 
Considerar que se desea guardar estos datos en una estructura de datos

    +--------+----------------------------------+--------+-----------+
    | Codigo | Nombre del libro                 | Precio | Categoria |
    +--------+----------------------------------+--------+-----------+
    | 001    | Aplicaciones Móviles con Android |  55.00 |     M     |
    | 002    | Aplicaciones Web con Django      |  80.00 |     W     |
    | 003    | Aplicaciones Web con ASP.NET MVC |  95.50 |     W     |
    | 004    | Aplicaciones Móviles con Xamarin |  75.00 |     M     |
    | 005    | Diseño con Photoshop             |  60.00 |     D     |
    | 006    | Diseño con Illustrator           |  72.00 |     D     |
    +--------+----------------------------------+--------+-----------+

Se desea crear funciones para:
- Actualizar el precio de los libros, se debe enviar el monto a
    incrementar y la categoría, si se desea actualizar el precio
    de todos se enviará el carácter "T".
- Impresión de reporte de libros, para lo cual se enviará la categoría
    del libro a imprimir, si se envía el carácter "T", se imprimen
    todos los libros.
- Agregar nuevos libros.

# --------------------------------------------------------------------
"""
from dataclasses import dataclass, field
from prototools import Menu, float_input


def _nuevo_libro():
    nombre = input("Ingrese el nombre del libro: ")
    precio = float_input("Ingrese el precio del libro: ")
    categoria = input("Ingrese la categoría del libro: ")
    return nombre, precio, categoria


def load_initial_data():
    return [
        ("001", "Aplicaciones Móviles con Android", 55.00, "M"),
        ("002", "Aplicaciones Web con Django", 80.00, "W"),
        ("003", "Aplicaciones Web con ASP.NET MVC", 95.50, "W"),
        ("004", "Aplicaciones Móviles con Xamarin", 75.00, "M"),
        ("005", "Diseño con Photoshop", 60.00, "D"),
        ("006", "Diseño con Illustrator", 72.00, "D"),
    ]


@dataclass
class Libro:
    codigo: str
    nombre: str
    _precio: float
    categoria: str

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio


@dataclass
class Libros:
    libros: list = field(default_factory=list)

    def __post_init__(self):
        self._load_data(load_initial_data())

    def agregar(self, libro):
        self.libros.append(libro)

    def agregar_nuevo_libro(self):
        presente, codigo = self._comprobar_codigo()
        if not presente:
            nombre, precio, categoria = _nuevo_libro()
            libro = Libro(codigo, nombre, precio, categoria)
            self.agregar(libro)

    def actualizar_precio(self, precio, categoria):
        if categoria == "T":
            for libro in self.libros:
                libro.precio += precio
        else:
            for libro in self.libros:
                if libro.categoria == categoria:
                    libro.precio += precio

    def imprimir_reporte(self, categoria):
        if categoria == "T":
            for libro in self.libros:
                print(libro)
        else:
            for libro in self.libros:
                if libro.categoria == categoria:
                    print(libro)
    
    def _comprobar_codigo(self):
        codigo = input("Ingrese el código del libro: ")
        for libro in self.libros:
            if libro.codigo == codigo:
                return True, None
        return False, codigo

    def _load_data(self, data):
        for libro in data:
            self.agregar(Libro(*libro))


def main():
    libros = Libros()
    menu = Menu("Libros")
    menu.add_options(
        ("Agregar nuevo libro", libros.agregar_nuevo_libro),
        ("Actualizar precio",
        lambda: libros.actualizar_precio(
            float_input("Ingrese el monto a incrementar: "),
            input("Ingrese la categoría: "))),
        ("Imprimir reporte",
        lambda: libros.imprimir_reporte(input("Ingrese la categoría: "))),
    )
    menu.run()


if __name__ == "__main__":
    main()