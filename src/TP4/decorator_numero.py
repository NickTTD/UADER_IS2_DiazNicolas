# Base Componente
class NumeroComponente:
    """Clase base que representa un número."""

    def __init__(self, valor):
        self._valor = valor

    def obtener_valor(self):
        """Retorna el valor actual."""
        return self._valor


# Decoradores Concretos
class SumarDosDecorador:
    """Decorador para sumar 2 al número."""

    def __init__(self, envuelto):
        self._envuelto = envuelto

    def obtener_valor(self):
        """Obtiene el valor del objeto envuelto y le suma 2."""
        return self._envuelto.obtener_valor() + 2


class MultiplicarDosDecorador:
    """Decorador para multiplicar el número por 2."""

    def __init__(self, envuelto):
        self._envuelto = envuelto

    def obtener_valor(self):
        """Obtiene el valor del objeto envuelto y lo multiplica por 2."""
        return self._envuelto.obtener_valor() * 2


class DividirPorTresDecorador:
    """Decorador para dividir el número por 3."""

    def __init__(self, envuelto):
        self._envuelto = envuelto

    def obtener_valor(self):
        """Obtiene el valor del objeto envuelto y lo divide por 3."""
        valor = self._envuelto.obtener_valor()
        # Manejo básico para evitar división por cero.
        return valor / 3 if valor != 0 else 0.0


# Demostración
valor_inicial = 10

# 1. Objeto base sin agregados
numero_base = NumeroComponente(valor_inicial)
print(f"Valor inicial: {numero_base.obtener_valor()}")

# 2. Agregar Sumar 2
numero_sumar_dos = SumarDosDecorador(numero_base)
print(f"Después de sumar 2: {numero_sumar_dos.obtener_valor()}")

# 3. Agregar Multiplicar por 2 (anidando sobre el anterior)
numero_sumar_dos_multiplicar_dos = MultiplicarDosDecorador(numero_sumar_dos)
print(
    f"Después de sumar 2 y multiplicar por 2: {numero_sumar_dos_multiplicar_dos.obtener_valor()}"
)

# 4. Agregar Dividir por 3 (anidando sobre el anterior)
numero_completo_decorado = DividirPorTresDecorador(numero_sumar_dos_multiplicar_dos)
print(
    f"Después de sumar 2, multiplicar por 2 y dividir por 3: {numero_completo_decorado.obtener_valor()}"
)

# tests

# Valor inicial -> Multiplicar por 2 -> Sumar 2 -> Dividir por 3
numero_mult_dos = MultiplicarDosDecorador(NumeroComponente(valor_inicial))
numero_mult_dos_sumar_dos = SumarDosDecorador(numero_mult_dos)
numero_alt_completo_decorado = DividirPorTresDecorador(numero_mult_dos_sumar_dos)

print(f"Valor inicial: {NumeroComponente(valor_inicial).obtener_valor()}")
print(f"*2: {numero_mult_dos.obtener_valor()}")
print(f"*2 y +2: {numero_mult_dos_sumar_dos.obtener_valor()}")
print(f"*2, +2 y /3: {numero_alt_completo_decorado.obtener_valor()}")
