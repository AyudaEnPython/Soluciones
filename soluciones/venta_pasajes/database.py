"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sqlite3
from models import DAO


class VentaDAO(DAO):

    def __init__(self):
        self._conectar()

    def _conectar(self):
        self.conn = sqlite3.connect('ventas.db')
        self.cur = self.conn.cursor()

    def _desconectar(self):
        self.conn.close()

    def insertar(self, obj):
        self.execute(
            """
            INSERT INTO ventas(pasajero, pasaje)
            VALUES(?, ?)
            """,
            (obj.pasajero, obj.pasaje)
        )
        self.commit()

    def actualizar(self, obj):
        self.execute(
            """
            UPDATE ventas
            SET pasajero = ?, pasaje = ?
            WHERE id_venta = ?
            """,
            (obj.pasajero, obj.pasaje, obj.id_venta)
        )
        self.commit()

    def eliminar(self, obj):
        self.execute(
            """
            DELETE FROM ventas
            WHERE id_venta = ?
            """,
            (obj.id_venta,)
        )
        self.commit()

    def seleccionar(self, obj):
        self.execute(
            """
            SELECT * FROM ventas
            WHERE id_venta = ?
            """,
            (obj.id_venta,)
        )
        return self.cur.fetchone()

    def _crear_tabla(self):
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS ventas(
                id_venta INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                pasajero TEXT,
                pasaje TEXT
            )
            """
        )

    def execute(self, data):
        self.cur.execute(data)

    def commit(self):
        self.conn.commit()
