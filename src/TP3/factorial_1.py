# 1. Provea una clase que dado un número entero cualquiera retorne el factorial del
# mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma
# instancia de clase.
"""
factorial.py

Define una clase Factorial que utiliza el decorador singleton para garantizar que
solo exista una instancia de esta clase durante la ejecución del programa.
"""

from singleton import singleton  # Asegurate que este import sí se usa


@singleton
class Factorial:
    """
    Clase para calcular el factorial de un número entero no negativo.
    Utiliza el decorador @singleton para mantener una única instancia.
    """

    def calcular(self, n):
        """
        Calcula el factorial de un número entero n.

        Args:
            n (int): Número entero >= 0

        Returns:
            int: El factorial de n

        Raises:
            ValueError: Si n es negativo
        """
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
