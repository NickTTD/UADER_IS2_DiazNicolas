import os

# *--------------------------------------------------------------------
# * Ejemplo de design pattern de tipo state con memorias de AM y FM
# *--------------------------------------------------------------------
"""State class: Base State class"""


class State:
    """
    Clase base que define el comportamiento común de las estaciones.
    Barrerá las estaciones y memorias en cada ciclo de sintonización.
    """

    def scan(self):
        """
        Barrido de estaciones, incluyendo memorias.
        """
        if self.pos < len(self.stations):
            # Barrer estaciones
            print(f"Sintonizando... Estación {self.stations[self.pos]} {self.name}")
        else:
            # Barrer memorias
            memory_pos = self.pos - len(self.stations)
            print(
                f"Sintonizando... Memoria M{memory_pos+1} {self.radio.memories[self.name][memory_pos]} {self.name}"
            )

        # Avanzar a la siguiente posición (estación o memoria)
        self.pos += 1
        if self.pos == len(self.stations) + len(self.radio.memories[self.name]):
            self.pos = 0


# *------- Implementa como barrer las estaciones de AM
class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]  # Estaciones AM
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


# *------- Implementa como barrer las estaciones de FM
class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]  # Estaciones FM
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate


# *--------- Construye la radio con todas sus formas de sintonía y memorias
class Radio:

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)

        # Inicialmente en FM
        self.state = self.fmstate

        # Memorizar frecuencias AM y FM
        self.memories = {
            "AM": ["1200", "1300", "1400", "1450"],  # M1, M2, M3, M4 para AM
            "FM": ["90.5", "95.7", "100.3", "106.1"],  # M1, M2, M3, M4 para FM
        }

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


# *---------------------

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    # Recorre las acciones ejecutando la acción
    print(
        "Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado"
    )
    for action in actions:
        action()
