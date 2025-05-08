from abc import ABC, abstractmethod


# --- IMPLEMENTACIÓN DEL PATRÓN BRIDGE ---
# No había entendido del todo este patrón así que el comment ratio subio a 0.9
# === Implementor: define la interfaz para los trenes laminadores ===
class TrenLaminador(ABC):
    """
    Interfaz abstracta que representa un tren laminador.
    Define la operación 'laminar', que será implementada por las clases concretas.

    El patrón Bridge separa esta parte (implementación) de la abstracción (lámina de acero).
    """

    @abstractmethod
    def laminar(self, ancho: float, espesor: float):
        """
        Realiza la laminación de una plancha con el ancho y espesor especificados.
        """
        pass


# === ConcreteImplementors: trenes laminadores específicos ===


class TrenLaminador5m(TrenLaminador):
    """
    Implementación concreta del tren laminador que produce planchas de 5 metros de largo.
    """

    def laminar(self, ancho: float, espesor: float):
        print(
            f'[Tren 5m] Laminando plancha de 5 metros, {ancho}m de ancho y {espesor}" de espesor.'
        )


class TrenLaminador10m(TrenLaminador):
    """
    Implementación concreta del tren laminador que produce planchas de 10 metros de largo.
    """

    def laminar(self, ancho: float, espesor: float):
        print(
            f'[Tren 10m] Laminando plancha de 10 metros, {ancho}m de ancho y {espesor}" de espesor.'
        )


# === Abstraction: la lámina de acero ===


class LaminaAcero:
    """
    Clase abstracta que representa una lámina de acero.

    Esta clase actúa como la 'Abstraction' del patrón Bridge. No sabe cómo se realiza
    la laminación, solo delega esa tarea a un 'TrenLaminador' (la implementación).

    """

    def __init__(self, tren: TrenLaminador):
        """
        Constructor que recibe un objeto TrenLaminador (implementación del Bridge).

        Args:
            tren (TrenLaminador): Instancia de un tren laminador concreto (5m o 10m).
        """
        self.ancho = 1.5  # metros
        self.espesor = 0.5  # pulgadas
        self.tren = tren  # Implementor: el tren responsable de la producción

    def producir(self):
        """
        Realiza la producción (laminación) de la lámina usando el tren asignado.
        """
        self.tren.laminar(self.ancho, self.espesor)


# test
if __name__ == "__main__":
    # Crear instancias concretas de trenes laminadores
    tren5 = TrenLaminador5m()
    tren10 = TrenLaminador10m()

    # Crear láminas de acero asignadas a diferentes trenes
    lamina1 = LaminaAcero(tren5)  # Esta lámina se produce en el tren de 5m
    lamina2 = LaminaAcero(tren10)  # Esta lámina se produce en el tren de 10m

    # Producir las láminas (Bridge en acción)
    lamina1.producir()
    lamina2.producir()
