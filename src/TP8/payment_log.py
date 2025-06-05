"""
Implementa el patrón Iterator para recorrer los pagos realizados por
las distintas cuentas (handlers)
"""


class PaymentIterator:
    """
    Iterador para recorrer pagos realizados en orden cronológico.
    Ordena pagos según el número de pedido y provee
    métodos para iterar sobre ellos
    """

    def __init__(self, payment_records):
        self._payments = sorted(payment_records, key=lambda r: r.order_number)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._payments):
            record = self._payments[self._index]
            self._index += 1
            return record
        raise StopIteration


class PaymentLog:
    """
    Consolida los pagos realizados por todos los handlers y proporciona un iterador.
    """

    def __init__(self, handlers):
        """
        :param handlers: Lista de instancias de Handler.
        """
        self.handlers = handlers

    def get_iterator(self):
        """
        Devuelve un iterador sobre todos los pagos realizados.

        :return: Instancia de PaymentIterator.
        """
        all_payments = []
        for handler in self.handlers:
            all_payments.extend(handler.get_payments())
        return PaymentIterator(all_payments)
