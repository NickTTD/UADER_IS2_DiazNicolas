"""
impuestos.py

Define una clase singleton para calcular impuestos sobre una base imponible.
Incluye IVA (21%), IIBB (5%) y contribuciones municipales (1.2%).
"""

from singleton import singleton


@singleton
class CalculadoraImpuestos:
    """
    Clase singleton que calcula el total de impuestos a aplicar sobre una base imponible.
    """

    IVA = 0.21
    IIBB = 0.05
    MUNICIPAL = 0.012

    def calcular_total(self, base_imponible):
        """
        Calcula el total de impuestos (IVA + IIBB + municipales) sobre el valor base.

        Args:
            base_imponible (float): El valor sobre el cual se calculan los impuestos.

        Returns:
            float: La suma total de los impuestos.
        """
        iva = base_imponible * self.IVA
        iibb = base_imponible * self.IIBB
        municipal = base_imponible * self.MUNICIPAL
        total = iva + iibb + municipal
        return total


base = float(input("Ingrese la base imponible: "))
Impuestos = CalculadoraImpuestos().calcular_total(base)
print(f"Los impuestos suman un total de: {Impuestos}")
print(f"Precio final: {base + Impuestos}")
