"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from unittest import main, TestCase

from models import Cliente, Cuota, Cronograma
from utils import convertir_fecha

data = [
    {'periodo': '01', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2020-12-25', 'dias': 30,
    'capital': 9254.4, 'amortizacion': 745.6,
    'interes': 200.0, 'cuota': 945.6},
    {'periodo': '02', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-01-25', 'dias': 31,
    'capital': 8493.89, 'amortizacion': 760.51,
    'interes': 185.09, 'cuota': 945.6},
    {'periodo': '03', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-02-25', 'dias': 31,
    'capital': 7718.17, 'amortizacion': 775.72,
    'interes': 169.88, 'cuota': 945.6},
    {'periodo': '04', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-03-25', 'dias': 28,
    'capital': 6926.93, 'amortizacion': 791.24,
    'interes': 154.36, 'cuota': 945.6},
    {'periodo': '05', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-04-25', 'dias': 31,
    'capital': 6119.87, 'amortizacion': 807.06,
    'interes': 138.54, 'cuota': 945.6},
    {'periodo': '06', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-05-25', 'dias': 30,
    'capital': 5296.67, 'amortizacion': 823.2,
    'interes': 122.4, 'cuota': 945.6},
    {'periodo': '07', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-06-25', 'dias': 31,
    'capital': 4457.0, 'amortizacion': 839.67,
    'interes': 105.93, 'cuota': 945.6},
    {'periodo': '08', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-07-25', 'dias': 30,
    'capital': 3600.54, 'amortizacion': 856.46,
    'interes': 89.14, 'cuota': 945.6},     
    {'periodo': '09', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-08-25', 'dias': 31,
    'capital': 2726.95, 'amortizacion': 873.59,
    'interes': 72.01, 'cuota': 945.6},     
    {'periodo': '10', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-09-25', 'dias': 31,
    'capital': 1835.89, 'amortizacion': 891.06,
    'interes': 54.54, 'cuota': 945.6},     
    {'periodo': '11', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-10-25', 'dias': 30,
    'capital': 927.01, 'amortizacion': 908.88,
    'interes': 36.72, 'cuota': 945.6},     
    {'periodo': '12', 'fecha_pago': '2020-11-05', 
    'fecha_vencimiento': '2021-11-25', 'dias': 31,
    'capital': 0.0, 'amortizacion': 927.01,
    'interes': 18.54, 'cuota': 945.6},
]

class Test(TestCase):
    
    def setUp(self) -> None:
        self.cliente = Cliente(
            apellidos="Wick",
            nombres="John",
            dni="12345678",
        )
        self.cuota = Cuota(
            monto_prestamo=10_000,
            dias_pago=25,
            fecha="2020-11-05",
        )
        self.cronograma = Cronograma(self.cliente, self.cuota)

    def test_Cliente(self):
        self.assertEqual(self.cliente.apellidos, "Wick")
        self.assertEqual(self.cliente.nombres, "John")
        self.assertEqual(self.cliente.dni, "12345678")

    def test_Cuota(self):
        self.assertEqual(self.cuota.monto_prestamo, 10_000)
        self.assertEqual(self.cuota.dias_pago, 25)
        self.assertEqual(self.cuota.fecha, "2020-11-05")

    def test_Cronograma(self):
        self.assertEqual(self.cronograma.cliente.apellidos, "Wick")
        self.assertEqual(self.cronograma.cliente.nombres, "John")
        self.assertEqual(self.cronograma.cliente.dni, "12345678")
        self.assertEqual(self.cronograma.cuota.monto_prestamo, 10_000)
        self.assertEqual(self.cronograma.cuota.dias_pago, 25)
        self.assertEqual(self.cronograma.cuota.fecha, "2020-11-05")
        
    def test_Cronograma_operaciones(self):
        self.assertEqual(self.cronograma.meses, 12)
        self.assertEqual(self.cronograma.interes, 0.26)
        self.assertEqual(self.cronograma.tem, 0.02)
        self.assertEqual(self.cronograma.cuota_mensual, 945.6)

    def test_Cronograma_data(self):
        self.assertEqual(len(self.cronograma.data), 12)
        for i in range(0, len(self.cronograma.data)):
            self.assertEqual(self.cronograma.data[i]["periodo"], data[i]["periodo"])
            self.assertEqual(self.cronograma.data[i]["fecha_pago"], data[i]["fecha_pago"])
            self.assertEqual(self.cronograma.data[i]["fecha_vencimiento"], data[i]["fecha_vencimiento"])
            self.assertEqual(self.cronograma.data[i]["dias"], data[i]["dias"])
            self.assertEqual(self.cronograma.data[i]["capital"], data[i]["capital"])
            self.assertEqual(self.cronograma.data[i]["amortizacion"], data[i]["amortizacion"])
            self.assertEqual(self.cronograma.data[i]["interes"], data[i]["interes"])
            self.assertEqual(self.cronograma.data[i]["cuota"], data[i]["cuota"])

    def test_utils_convertir_fecha(self):
        self.assertEqual(convertir_fecha("11-05-2020"), "2020-05-11")

if __name__ == '__main__':
    main()