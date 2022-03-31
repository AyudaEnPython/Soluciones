"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sys
from PySide2 import QtWidgets

from ui_proforma import Ui_MainWindow
from logic import Cliente, Producto, Proforma


def _f(n: float) -> str:
    return f"S/. {n:.2f}"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_salir.clicked.connect(self.salir)
        self.btn_limpiar.clicked.connect(self.limpiar)

    def encontrar_interes(self) -> str:
        for item in (
            self.rbn_interes_0, self.rbn_interes_15, self.rbn_interes_30
        ):
            if item.isChecked():
                return item.text()

    def encontrar_descuento(self) -> str:
        for item in (self.rbn_mayorista, self.rbn_minorista):
            if item.isChecked():
                return item.text()

    def calcular(self) -> None:
        cliente = Cliente(self.ent_codigo.text(), self.ent_cliente.text())
        producto = Producto(
            self.ent_producto.text(),
            float(self.ent_precio.text()),
            int(self.sbx_cantidad.value()),
            self.encontrar_interes(),
            self.encontrar_descuento()
        )
        proforma = Proforma(cliente, producto)
        self.text_display.setText(str(proforma))
        self.show_importe.setText(_f(proforma.producto.total))
        self.show_descuento.setText(_f(proforma.producto.descuento))
        self.show_interes.setText(_f(proforma.producto.interes))
        self.show_total.setText(_f(proforma.producto.calcular_precio()))

    def limpiar(self) -> None:
        self.text_display.clear()
        self.ent_codigo.setText("")
        self.ent_cliente.setText("")
        self.ent_producto.setText("")
        self.ent_precio.setText("")
        self.sbx_cantidad.setValue(0)
        self.rbn_interes_0.setChecked(True)
        self.rbn_mayorista.setChecked(True)
        self.show_importe.setText("")
        self.show_descuento.setText("")
        self.show_interes.setText("")
        self.show_total.setText("")

    def salir(self) -> None:
        sys.exit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
