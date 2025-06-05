# TP8 Re-ingeniería
### Díaz Nicolás Tomás
## Descripción

- Usa un archivo JSON (`sitedata.json`) para gestionar claves de tokens (bancos).
- Dos cuentas controladas por handlers que procesan pagos de forma balanceada y automática según saldo disponible.
- Patrón Cadena de Comando para seleccionar qué cuenta realiza cada pago.
- Registro cronológico de pagos realizados con un iterador.


---

## Archivos principales

- `token_reader.py`: Lee y maneja tokens desde el archivo JSON.
- `handler.py`: Define las clases `Handler`, `PaymentRequest` y `PaymentRecord` para el procesamiento de pagos.
- `payment_log.py`: Consolida y permite iterar sobre todos los pagos realizados.
- `main.py`: Punto de entrada, simula pedidos de pago y muestra resultados.

---

## Uso

Ejecutar main.py

## Pylint
pylint *.py

************* Module handler
handler.py:11:0: R0903: Too few public methods (0/2) (too-few-public-methods)
handler.py:24:0: R0903: Too few public methods (0/2) (too-few-public-methods)
************* Module payment_log
payment_log.py:29:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module token_reader
token_reader.py:10:0: R0903: Too few public methods (1/2) (too-few-public-methods)

------------------------------------------------------------------
Your code has been rated at 9.60/10 (previous run: 9.19/10, +0.40)

Como son clases pequeñas, y decidí dividir los archivos de la manera mas limpia posible,
considero aceptable que mis clases no tengan mas de 1 método.

