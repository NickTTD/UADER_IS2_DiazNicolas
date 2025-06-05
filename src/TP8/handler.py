"""
handler.py

clases para manejar solicitudes de pago con cadena de responsabilidad.
Incluye la gestión de saldos y registro de pagos realizados.
"""

from token_reader import JSONTokenReader as TokenReader


class PaymentRequest:
    """
    Representa una solicitud de pago.

    :param order_number: Número de pedido.
    :param amount: Monto solicitado.
    """

    def __init__(self, order_number, amount):
        self.order_number = order_number
        self.amount = amount


class PaymentRecord:
    """
    Representa un pago realizado exitosamente.
    """

    def __init__(self, order_number, token, amount):
        self.order_number = order_number
        self.token = token
        self.amount = amount


class Handler:
    """
    Clase base para los manejadores de pago (token1, token2).
    """

    def __init__(self, token, initial_balance, token_file, next_handler=None):
        self.token = token
        self.balance = initial_balance
        self.next_handler = next_handler
        self.token_reader = TokenReader(token_file)
        self.payment_log = []

    def set_next(self, handler):
        """
        Siguiente handler en la cadena.
        """
        self.next_handler = handler

    def can_process(self, amount):
        """
        Indica si el handler tiene saldo suficiente para procesar el monto dado.

        :param amount: Monto a verificar.
        :return: True si hay saldo suficiente, False en caso contrario.
        """
        return self.balance >= amount

    def process(self, request: PaymentRequest):
        """
        Procesa un pago si tiene saldo suficiente, si no lo pasa al siguiente handler.

        :param request: Instancia de PaymentRequest.
        :return: PaymentRecord si se procesó, None si no se pudo.
        """
        if self.can_process(request.amount):
            self.balance -= request.amount
            record = PaymentRecord(
                order_number=request.order_number,
                token=self.token,
                amount=request.amount,
            )
            self.payment_log.append(record)
            return record
        if self.next_handler:
            return self.next_handler.process(request)

        print(
            f"No se pudo procesar el pedido #{request.order_number}: fondos insuficientes."
        )
        return None

    def get_payments(self):
        """
        Devuelve los pagos realizados por este handler.

        :return: Lista de PaymentRecord.
        """
        return self.payment_log

    def get_key(self):
        """
        Devuelve la clave asociada a este token (desde el singleton).

        :return: Clave del banco.
        """
        return self.token_reader.get_token(self.token)
