"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

PRODUCCION = 0.25
CONTABILIDAD = 0.4
SOPORTE = 0.2
MARKETING = 0.15

donacion = float(input("Ingresar donación"))

produccion = donacion * PRODUCCION
soporte = donacion * SOPORTE
marketing = (produccion + soporte) * MARKETING
contabilidad = (marketing + soporte) * CONTABILIDAD
recursos_humanos = donacion - (produccion + contabilidad + marketing + soporte)

print(f"Área de Producción: {produccion}")
print(f"Área de Contabilidad: {contabilidad}")
print(f"Área de Marketing: {marketing}")
print(f"Área de Soporte: {soporte}")
print(f"Área de Recursos Humanos: {recursos_humanos}")
