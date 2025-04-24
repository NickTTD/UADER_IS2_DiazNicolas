from factory_decorator import factory


class Hamburguesa:
    """
    Representa una hamburguesa con un tipo específico de entrega.
    """

    def __init__(self, tipo_entrega):
        self.tipo_entrega = tipo_entrega

    def entregar(self):
        print(f"🍔 Entrega de hamburguesa por: {self.tipo_entrega}")

    def __str__(self):
        return f"Hamburguesa ({self.tipo_entrega})"


# Esto y factory_decorator.py no son muy buenas ideas, pero lo dejo, después lo resolví reusando código de factory.py original
# Factories usando el decorador genérico
@factory(expected_type=Hamburguesa)
def crear_hamburguesa_mostrador():
    return Hamburguesa("mostrador")


@factory(expected_type=Hamburguesa)
def crear_hamburguesa_retirar():
    return Hamburguesa("retiro en local")


@factory(expected_type=Hamburguesa)
def crear_hamburguesa_delivery():
    return Hamburguesa("delivery")


h1 = crear_hamburguesa_mostrador()
h2 = crear_hamburguesa_retirar()
h3 = crear_hamburguesa_delivery()

h1.entregar()
h2.entregar()
h3.entregar()
