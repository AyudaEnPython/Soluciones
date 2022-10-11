"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    Qt,
)
from PySide2.QtGui import (
    QFont,
    QFormLayout,
    QGroupBox,
    QPixmap,
    QStatusBar,
    QTextBrowser,
)
from PySide2.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(582, 530)
        MainWindow.setStyleSheet(
            u"QPushButton {\n"
            "  background-color: \"orange\";\n"
            "  color: \"white\";\n"
            "}\n"
            "QPushButton:hover {\n"
            "  background-color:\"white\";\n"
            "  color: \"orange\";\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 20, 271, 141))
        self.formulario = QFormLayout(self.formLayoutWidget)
        self.formulario.setObjectName(u"formulario")
        self.formulario.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.formulario.setFormAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.formulario.setContentsMargins(0, 0, 0, 0)
        self.lbl_codigo = QLabel(self.formLayoutWidget)
        self.lbl_codigo.setObjectName(u"lbl_codigo")
        font = QFont()
        font.setFamily(u"Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        self.lbl_codigo.setFont(font)

        self.formulario.setWidget(0, QFormLayout.LabelRole, self.lbl_codigo)

        self.lbl_cliente = QLabel(self.formLayoutWidget)
        self.lbl_cliente.setObjectName(u"lbl_cliente")
        self.lbl_cliente.setFont(font)

        self.formulario.setWidget(1, QFormLayout.LabelRole, self.lbl_cliente)

        self.lbl_producto = QLabel(self.formLayoutWidget)
        self.lbl_producto.setObjectName(u"lbl_producto")
        self.lbl_producto.setFont(font)
        self.lbl_producto.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.formulario.setWidget(2, QFormLayout.LabelRole, self.lbl_producto)

        self.lbl_precio = QLabel(self.formLayoutWidget)
        self.lbl_precio.setObjectName(u"lbl_precio")
        self.lbl_precio.setFont(font)
        self.lbl_precio.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.formulario.setWidget(3, QFormLayout.LabelRole, self.lbl_precio)

        self.lbl_cantidad = QLabel(self.formLayoutWidget)
        self.lbl_cantidad.setObjectName(u"lbl_cantidad")
        self.lbl_cantidad.setFont(font)

        self.formulario.setWidget(4, QFormLayout.LabelRole, self.lbl_cantidad)

        self.ent_codigo = QLineEdit(self.formLayoutWidget)
        self.ent_codigo.setObjectName(u"ent_codigo")
        self.ent_codigo.setFont(font)
        self.ent_codigo.setAlignment(Qt.AlignCenter)

        self.formulario.setWidget(0, QFormLayout.FieldRole, self.ent_codigo)

        self.ent_cliente = QLineEdit(self.formLayoutWidget)
        self.ent_cliente.setObjectName(u"ent_cliente")
        self.ent_cliente.setFont(font)
        self.ent_cliente.setAlignment(Qt.AlignCenter)

        self.formulario.setWidget(1, QFormLayout.FieldRole, self.ent_cliente)

        self.ent_producto = QLineEdit(self.formLayoutWidget)
        self.ent_producto.setObjectName(u"ent_producto")
        self.ent_producto.setFont(font)
        self.ent_producto.setAlignment(Qt.AlignCenter)

        self.formulario.setWidget(2, QFormLayout.FieldRole, self.ent_producto)

        self.ent_precio = QLineEdit(self.formLayoutWidget)
        self.ent_precio.setObjectName(u"ent_precio")
        self.ent_precio.setFont(font)
        self.ent_precio.setAlignment(Qt.AlignCenter)

        self.formulario.setWidget(3, QFormLayout.FieldRole, self.ent_precio)

        self.sbx_cantidad = QSpinBox(self.formLayoutWidget)
        self.sbx_cantidad.setObjectName(u"sbx_cantidad")
        self.sbx_cantidad.setFont(font)
        self.sbx_cantidad.setAlignment(Qt.AlignCenter)

        self.formulario.setWidget(4, QFormLayout.FieldRole, self.sbx_cantidad)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 370, 121, 91))
        self.layout_botones = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_botones.setObjectName(u"layout_botones")
        self.layout_botones.setContentsMargins(0, 0, 0, 0)
        self.btn_calcular = QPushButton(self.verticalLayoutWidget)
        self.btn_calcular.setObjectName(u"btn_calcular")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light SemiCondensed")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.btn_calcular.setFont(font1)
        self.btn_calcular.setAutoFillBackground(False)
        self.btn_calcular.setStyleSheet(u"")

        self.layout_botones.addWidget(self.btn_calcular)

        self.btn_limpiar = QPushButton(self.verticalLayoutWidget)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setFont(font1)

        self.layout_botones.addWidget(self.btn_limpiar)

        self.btn_salir = QPushButton(self.verticalLayoutWidget)
        self.btn_salir.setObjectName(u"btn_salir")
        self.btn_salir.setFont(font1)
        self.btn_salir.setStyleSheet(u"")

        self.layout_botones.addWidget(self.btn_salir)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(30, 210, 171, 111))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light Condensed")
        self.formLayoutWidget_2.setFont(font2)
        self.resultados = QFormLayout(self.formLayoutWidget_2)
        self.resultados.setObjectName(u"resultados")
        self.resultados.setLabelAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.resultados.setContentsMargins(0, 0, 0, 0)
        self.lbl_importe = QLabel(self.formLayoutWidget_2)
        self.lbl_importe.setObjectName(u"lbl_importe")
        self.lbl_importe.setFont(font)

        self.resultados.setWidget(0, QFormLayout.LabelRole, self.lbl_importe)

        self.lbl_descuentos = QLabel(self.formLayoutWidget_2)
        self.lbl_descuentos.setObjectName(u"lbl_descuentos")
        self.lbl_descuentos.setFont(font)

        self.resultados.setWidget(
            1, QFormLayout.LabelRole, self.lbl_descuentos
        )

        self.lbl_interes = QLabel(self.formLayoutWidget_2)
        self.lbl_interes.setObjectName(u"lbl_interes")
        self.lbl_interes.setFont(font)

        self.resultados.setWidget(2, QFormLayout.LabelRole, self.lbl_interes)

        self.lbl_total = QLabel(self.formLayoutWidget_2)
        self.lbl_total.setObjectName(u"lbl_total")
        self.lbl_total.setFont(font)

        self.resultados.setWidget(3, QFormLayout.LabelRole, self.lbl_total)

        self.show_importe = QLineEdit(self.formLayoutWidget_2)
        self.show_importe.setObjectName(u"show_importe")
        self.show_importe.setEnabled(False)
        self.show_importe.setFont(font)
        self.show_importe.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.resultados.setWidget(0, QFormLayout.FieldRole, self.show_importe)

        self.show_descuento = QLineEdit(self.formLayoutWidget_2)
        self.show_descuento.setObjectName(u"show_descuento")
        self.show_descuento.setEnabled(False)
        self.show_descuento.setFont(font)
        self.show_descuento.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.resultados.setWidget(
            1, QFormLayout.FieldRole, self.show_descuento
        )

        self.show_interes = QLineEdit(self.formLayoutWidget_2)
        self.show_interes.setObjectName(u"show_interes")
        self.show_interes.setEnabled(False)
        self.show_interes.setFont(font)
        self.show_interes.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.resultados.setWidget(2, QFormLayout.FieldRole, self.show_interes)

        self.show_total = QLineEdit(self.formLayoutWidget_2)
        self.show_total.setObjectName(u"show_total")
        self.show_total.setEnabled(False)
        self.show_total.setFont(font)
        self.show_total.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.resultados.setWidget(3, QFormLayout.FieldRole, self.show_total)

        self.gbox_interes = QGroupBox(self.centralwidget)
        self.gbox_interes.setObjectName(u"gbox_interes")
        self.gbox_interes.setGeometry(QRect(230, 170, 151, 101))
        self.gbox_interes.setFont(font)
        self.gbox_interes.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_2 = QWidget(self.gbox_interes)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(40, 20, 81, 74))
        self.layout_interes = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_interes.setObjectName(u"layout_interes")
        self.layout_interes.setContentsMargins(0, 0, 0, 0)
        self.rbn_interes_0 = QRadioButton(self.verticalLayoutWidget_2)
        self.rbn_interes_0.setObjectName(u"rbn_interes_0")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light Condensed")
        font3.setPointSize(8)
        self.rbn_interes_0.setFont(font3)

        self.layout_interes.addWidget(self.rbn_interes_0)

        self.rbn_interes_15 = QRadioButton(self.verticalLayoutWidget_2)
        self.rbn_interes_15.setObjectName(u"rbn_interes_15")
        self.rbn_interes_15.setFont(font3)

        self.layout_interes.addWidget(self.rbn_interes_15)

        self.rbn_interes_30 = QRadioButton(self.verticalLayoutWidget_2)
        self.rbn_interes_30.setObjectName(u"rbn_interes_30")
        self.rbn_interes_30.setFont(font3)

        self.layout_interes.addWidget(self.rbn_interes_30)

        self.gbox_descuento = QGroupBox(self.centralwidget)
        self.gbox_descuento.setObjectName(u"gbox_descuento")
        self.gbox_descuento.setGeometry(QRect(390, 170, 171, 101))
        self.gbox_descuento.setFont(font)
        self.gbox_descuento.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_3 = QWidget(self.gbox_descuento)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(40, 30, 91, 48))
        self.layout_descuento = QVBoxLayout(self.verticalLayoutWidget_3)
        self.layout_descuento.setObjectName(u"layout_descuento")
        self.layout_descuento.setContentsMargins(0, 0, 0, 0)
        self.rbn_mayorista = QRadioButton(self.verticalLayoutWidget_3)
        self.rbn_mayorista.setObjectName(u"rbn_mayorista")
        self.rbn_mayorista.setFont(font3)

        self.layout_descuento.addWidget(self.rbn_mayorista)

        self.rbn_minorista = QRadioButton(self.verticalLayoutWidget_3)
        self.rbn_minorista.setObjectName(u"rbn_minorista")
        self.rbn_minorista.setFont(font3)

        self.layout_descuento.addWidget(self.rbn_minorista)

        self.text_display = QTextBrowser(self.centralwidget)
        self.text_display.setObjectName(u"text_display")
        self.text_display.setGeometry(QRect(230, 280, 331, 221))
        font4 = QFont()
        font4.setFamily(u"Consolas")
        self.text_display.setFont(font4)
        self.img = QLabel(self.centralwidget)
        self.img.setObjectName(u"img")
        self.img.setGeometry(QRect(320, 40, 241, 81))
        self.img.setPixmap(QPixmap(u"ayuda_en_python.png"))
        self.img.setScaledContents(True)
        self.img.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.lbl_codigo.setText(
            QCoreApplication.translate(
                "MainWindow", u"CODIGO DEL CLIENTE", None
            )
        )
        self.lbl_cliente.setText(
            QCoreApplication.translate(
                "MainWindow", u"NOMBRE DEL CLIENTE", None
            )
        )
        self.lbl_producto.setText(
            QCoreApplication.translate("MainWindow", u"PPRODUCTO", None)
        )
        self.lbl_precio.setText(
            QCoreApplication.translate("MainWindow", u"PRECIO", None)
        )
        self.lbl_cantidad.setText(
            QCoreApplication.translate("MainWindow", u"CANTIDAD", None)
        )
        self.btn_calcular.setText(
            QCoreApplication.translate("MainWindow", u"CALCULAR", None)
        )
        self.btn_limpiar.setText(
            QCoreApplication.translate("MainWindow", u"LIMPIAR", None)
        )
        self.btn_salir.setText(
            QCoreApplication.translate("MainWindow", u"SALIR", None)
        )
        self.lbl_importe.setText(
            QCoreApplication.translate("MainWindow", u"IMPORTE", None)
        )
        self.lbl_descuentos.setText(
            QCoreApplication.translate("MainWindow", u"DESCUENTOS", None)
        )
        self.lbl_interes.setText(
            QCoreApplication.translate("MainWindow", u"INTER\u00c9S", None)
        )
        self.lbl_total.setText(
            QCoreApplication.translate("MainWindow", u"TOTAL", None)
        )
        self.gbox_interes.setTitle(
            QCoreApplication.translate(
                "MainWindow", u"TIPO DE CR\u00c9DITO INTER\u00c9S", None
            )
        )
        self.rbn_interes_0.setText(
            QCoreApplication.translate("MainWindow", u"0 D\u00cdAS 0%", None)
        )
        self.rbn_interes_15.setText(
            QCoreApplication.translate(
                "MainWindow", u"15 D\u00cdAS 8.5%", None
            )
        )
        self.rbn_interes_30.setText(
            QCoreApplication.translate(
                "MainWindow", u"30 D\u00cdAS 12.5%", None
            )
        )
        self.gbox_descuento.setTitle(
            QCoreApplication.translate(
                "MainWindow", u"TIPO DE CLIENTE DESCUENTO", None
            )
        )
        self.rbn_mayorista.setText(
            QCoreApplication.translate("MainWindow", u"MAYORISTA 4.5%", None)
        )
        self.rbn_minorista.setText(
            QCoreApplication.translate("MainWindow", u"MINORISTA 1.9%", None)
        )
        self.img.setText("")
