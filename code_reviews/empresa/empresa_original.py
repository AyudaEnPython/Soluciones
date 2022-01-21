"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
class Empresa:

    def __init__(self, ingresos, costos, salarios, personas) -> None:
        self.ingresos = float(ingresos)
        self.costos = float(costos)
        self.salarios = float(salarios)
        self.personas = float(personas)

    def myfunc(self):
        ingresos = str(self.ingresos)
        costos = str(self.costos)
        print("La empresa tiene ingresos y costos por " + ingresos + " y " + costos + " respectivamente")

    def utilidades(self):
        ingresos = self.ingresos
        costos = self.costos
        return ingresos-costos

    def salario_pp(self):
        salarios = self.salarios
        personas = self.personas
        return salarios/personas

    def utilidades_pp(self):
        utilidades = self.utilidades()
        personas = self.personas
        return utilidades/personas


ingresos = input("¿Cuál es el ingreso de la empresa?")
costos = input("¿Cuáles son los costos de la empresa?")
salarios = input("¿Cuál es el total de salarios?")
personas = input("¿Cuántas personas trabajan en la empresa?")

emp1 = Empresa(ingresos, costos, salarios, personas)

emp1.myfunc()
emp1.utilidades()
emp1.salario_pp()
emp1.utilidades_pp()