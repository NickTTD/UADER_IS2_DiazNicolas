# No tengo el código original del taller, pero hay un ejemplo similar en
# https://refactoring.guru/design-patterns/builder


# ==== Producto: el avión ====


class Avion:
    def __init__(self):
        self.cuerpo: str | None = None
        self.turbina_izquierda: str | None = None
        self.turbina_derecha: str | None = None
        self.ala_izquierda: str | None = None
        self.ala_derecha: str | None = None
        self.tren_de_aterrizaje: str | None = None

    def especificaciones(self):
        print("✈️ Especificaciones del avión:")
        print(f"  Cuerpo: {self.cuerpo}")
        print(f"  Turbina izquierda: {self.turbina_izquierda}")
        print(f"  Turbina derecha: {self.turbina_derecha}")
        print(f"  Ala izquierda: {self.ala_izquierda}")
        print(f"  Ala derecha: {self.ala_derecha}")
        print(f"  Tren de aterrizaje: {self.tren_de_aterrizaje}")


# ==== Interfaz del constructor ====


class ConstructorAvion:
    def construir_cuerpo(self):
        pass

    def construir_turbinas(self):
        pass

    def construir_alas(self):
        pass

    def construir_tren_de_aterrizaje(self):
        pass

    def obtener_avion(self) -> Avion:
        pass


# ==== Constructor concreto para avión comercial ====


class ConstructorAvionComercial(ConstructorAvion):
    def __init__(self):
        self.avion = Avion()

    def construir_cuerpo(self):
        self.avion.cuerpo = "Cuerpo de avión comercial"

    def construir_turbinas(self):
        self.avion.turbina_izquierda = "Turbina GE izquierda"
        self.avion.turbina_derecha = "Turbina GE derecha"

    def construir_alas(self):
        self.avion.ala_izquierda = "Ala izquierda extendida"
        self.avion.ala_derecha = "Ala derecha extendida"

    def construir_tren_de_aterrizaje(self):
        self.avion.tren_de_aterrizaje = "Tren de aterrizaje reforzado"

    def obtener_avion(self) -> Avion:
        return self.avion


# ==== Director: guía el proceso de construcción ====


class DirectorAvion:
    def __init__(self, constructor: ConstructorAvion):
        self.constructor = constructor

    def construir_avion_completo(self):
        self.constructor.construir_cuerpo()
        self.constructor.construir_turbinas()
        self.constructor.construir_alas()
        self.constructor.construir_tren_de_aterrizaje()


# ==== Ejecución principal ====

if __name__ == "__main__":
    constructor = ConstructorAvionComercial()
    director = DirectorAvion(constructor)

    director.construir_avion_completo()
    avion = constructor.obtener_avion()

    avion.especificaciones()
