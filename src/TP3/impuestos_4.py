# Clase base Factura
class Factura:
    def __init__(self, importe_base):
        self.importe_base = importe_base

    def calcular_total(self):
        raise NotImplementedError(
            "Método calcular_total() debe ser implementado en la subclase"
        )


# Subclase para IVA Responsable
class FacturaResponsableIVA(Factura):
    def calcular_total(self):
        return self.importe_base * 1.21  # IVA del 21%


# Subclase para IVA No Inscripto
class FacturaNoInscriptoIVA(Factura):
    def calcular_total(self):
        return self.importe_base  # No se aplica IVA


# Subclase para IVA Exento
class FacturaExentoIVA(Factura):
    def calcular_total(self):
        return self.importe_base  # No se aplica IVA


# Factory para crear las facturas
class FacturaFactory:
    @staticmethod
    def crear_factura(tipo_iva, importe_base):
        if tipo_iva == "responsable":
            return FacturaResponsableIVA(importe_base)
        elif tipo_iva == "no Inscripto":
            return FacturaNoInscriptoIVA(importe_base)
        elif tipo_iva == "exento":
            return FacturaExentoIVA(importe_base)
        else:
            raise ValueError("Tipo de IVA no válido")


# Uso del código
importe_base = float(input("Ingrese la base imponible: "))
tipo_iva = input(
    "Ingrese tipo IVA, Puede ser 'Responsable', 'No Inscripto' o 'Exento': "
).lower()
factura = FacturaFactory.crear_factura(tipo_iva, importe_base)
total = factura.calcular_total()
print(f"Total de la factura: {total}")
