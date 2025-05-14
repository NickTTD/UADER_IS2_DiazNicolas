class Subject:
    """
    Clase que representa al sujeto observado (publisher).
    Notifica a todos los observadores cuando se emite un ID.
    """

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        Agrega un observador a la lista de suscriptores.
        """
        self._observers.append(observer)

    def notify(self, emitted_id):
        """
        Notifica a todos los observadores con el ID emitido.
        """
        print(f"\nEmitiendo ID: {emitted_id}")
        for observer in self._observers:
            observer.update(emitted_id)


class Observer:
    """
    Clase base para observadores. Define la interfaz común.
    """

    def __init__(self, observer_id, label):
        self._id = observer_id
        self._label = label

    def update(self, emitted_id):
        """
        Verifica si el ID emitido coincide con el suyo.
        """
        if emitted_id == self._id:
            print(f"Observador {self._label} recibió su ID y responde.")


# Clases concretas con ID específicos
class ObserverA(Observer):
    def __init__(self):
        super().__init__("AAAA", "A")


class ObserverB(Observer):
    def __init__(self):
        super().__init__("BBBB", "B")


class ObserverC(Observer):
    def __init__(self):
        super().__init__("CCCC", "C")


class ObserverD(Observer):
    def __init__(self):
        super().__init__("DDDD", "D")


# === Ejemplo de uso ===

# Crear sujeto
subject = Subject()

# Crear y registrar observadores
a = ObserverA()
b = ObserverB()
c = ObserverC()
d = ObserverD()

subject.attach(a)
subject.attach(b)
subject.attach(c)
subject.attach(d)

# Emitir 8 IDs (al menos 4 deben coincidir)
ids = ["32AD", "AAAA", "CCCC", "C789", "BBBB", "D311", "Q123", "DDDD"]

for id_em in ids:
    subject.notify(id_em)
