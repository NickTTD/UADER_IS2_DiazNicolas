from abc import ABC, abstractmethod


# Cada handler agrega lo consumido a un diccionario para printear al final
class Handler(ABC):
    """
    Clase base para un handler en la cadena de responsabilidad.
    """

    def __init__(self, next_handler=None):
        """
        Inicializa con el siguiente handler en la cadena.
        """
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, number, consumed_info):
        """
        Intenta manejar el número o delega al siguiente handler.
        """
        pass


class EvenHandler(Handler):
    """
    Handler de numeros pares
    """

    def handle(self, number, consumed_info):
        """
        Consume el número si es par, o lo pasa al siguiente handler.
        """
        if number % 2 == 0:
            consumed_info["even"].append(number)
        elif self.next_handler:
            self.next_handler.handle(number, consumed_info)


class PrimeHandler(Handler):
    """
    Handler de números primos.
    """

    def handle(self, number, consumed_info):
        """
        Consume el número si es primo, o lo pasa al siguiente handler.
        """
        if self._is_prime(number):
            consumed_info["prime"].append(number)
        elif self.next_handler:
            self.next_handler.handle(number, consumed_info)

    def _is_prime(self, n):
        """
        Determina si un número es primo.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


class UnconsumedHandler(Handler):
    """
    Manejador de números no consumidos por otros handlers.
    """

    def handle(self, number, consumed_info):
        """
        Registra el número como no consumido.
        """
        consumed_info["unconsumed"].append(number)


# Diccionario de resultados
consumed_info = {"even": [], "prime": [], "unconsumed": []}

# Cadena de responsabilidad: par → primo → no consumido
chain = EvenHandler(PrimeHandler(UnconsumedHandler()))

# Procesar los números del 1 al 100
for num in range(1, 101):
    chain.handle(num, consumed_info)

# Mostrar resultados
print("Números pares consumidos:", " ".join(map(str, consumed_info["even"])))
print("Números primos consumidos:", " ".join(map(str, consumed_info["prime"])))
print("Números no consumidos:", " ".join(map(str, consumed_info["unconsumed"])))
