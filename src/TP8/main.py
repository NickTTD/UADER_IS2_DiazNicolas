"""
main.py

Este script coordina el sistema de pagos automatizados utilizando los patrones
de diseño Singleton(token_reader.py),
Cadena de Responsabilidad(handler.py)
e Iterador(payment_log.py).

Pasos realizados:

1. Inicializa dos handlers para los tokens 'token1' y 'token2', cada uno con
   un saldo inicial predefinido.

2. Conecta los handlers como una cadena de responsabilidad. Si un handler no
   puede procesar un pago por falta de saldo, lo pasa al siguiente.

3. Crea una serie de pedidos de pago (PaymentRequest) de $500 con diferentes
   números de pedido.

4. Procesa cada pedido automáticamente, seleccionando la cuenta adecuada con
   saldo suficiente.

5. Registra y muestra todos los pagos realizados en orden cronológico utilizando
   el patrón Iterator.

6. Muestra la versión actual
"""

from handler import Handler, PaymentRequest
from payment_log import PaymentLog

# Archivo JSON con los tokens
TOKEN_FILE = "sitedata.json"
VERSION = "1.2"
# Inicialización de los handlers
handler1 = Handler("token1", initial_balance=1000, token_file=TOKEN_FILE)
handler2 = Handler("token2", initial_balance=2000, token_file=TOKEN_FILE)
handler1.set_next(handler2)

# Procesamiento de pedidos de pago
pedidos = [
    PaymentRequest(order_number=1, amount=500),
    PaymentRequest(order_number=2, amount=500),
    PaymentRequest(order_number=3, amount=500),
    PaymentRequest(order_number=4, amount=500),
    PaymentRequest(order_number=5, amount=500),
]

for pedido in pedidos:
    handler1.process(pedido)

# Mostrar todos los pagos realizados
print("\nPagos realizados:")
log = PaymentLog([handler1, handler2])
for pago in log.get_iterator():
    print(f"Pedido #{pago.order_number} - Token: {pago.token} - Monto: ${pago.amount}")

# Versión del sistema
print(f"\nVersión del sistema: {VERSION}")
