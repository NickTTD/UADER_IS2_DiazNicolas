"""
singleton.py

Este módulo define un decorador `@singleton` que convierte cualquier clase en un singleton,
garantizando que solo se cree una única instancia de dicha clase durante el ciclo de vida del programa.

Uso:
    from singleton import singleton

    @singleton
    class MiClase:
        ...

    obj1 = MiClase()
    obj2 = MiClase()
    assert obj1 is obj2  # Siempre True
"""


def singleton(cls):
    """
    Decorador para convertir una clase en un singleton.

    Args:
        cls (type): La clase que se quiere convertir en singleton.

    Returns:
        function: Una función que devuelve siempre la misma instancia de la clase decorada.
    """
    instancias = {}

    def get_instance(*args, **kwargs):
        # Si no existe una instancia guardada, la crea y la almacena
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        # Devuelve siempre la misma instancia
        return instancias[cls]

    return get_instance
