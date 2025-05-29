"""
copyright UADER-FCyT-IS2©2024
todos los derechos reservados
Generador de números primos con patrón Singleton y validación robusta.
Implementa branching by abstraction para convergencia entre versiones.
"""

import os
import sys

MAX_RANGO = 65535
NUEVO = True
VERSION = "1.1"


class GeneradorPrimosSingleton:
    """
    Singleton para generar números primos con validación robusta de argumentos.
    Implementa branching by abstraction para convergencia con código original.
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GeneradorPrimosSingleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.max_rango = MAX_RANGO
            GeneradorPrimosSingleton._initialized = True

    def es_primo(self, n):
        """Retorna True si n es un número primo, False en caso contrario."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def obtener_primos_en_rango(self, inf, sup):
        """Devuelve una lista de números primos entre inf y sup (inclusive)."""
        return [n for n in range(inf, sup + 1) if self.es_primo(n)]

    def limpiar_pantalla(self):
        """Limpia la pantalla en forma multiplataforma."""
        os.system("cls" if os.name == "nt" else "clear")

    def print_syntax(self):
        """Muestra la sintaxis correcta del comando y termina el programa."""
        nombre_programa = os.path.basename(sys.argv[0])
        print(f"Sintaxis: {nombre_programa} <limite_inferior> <limite_superior>")
        print(f"         {nombre_programa} -v")
        print("  - Ambos límites deben ser números enteros")
        print("  - El límite inferior debe ser >= 0")
        print(f"  - El límite superior debe ser <= {self.max_rango}")
        print("  - El límite inferior debe ser <= límite superior")
        print(f"Ejemplo: {nombre_programa} 10 50")
        print(f"         {nombre_programa} -v")
        sys.exit(1)

    def validate_args(self, args):
        """
        Validación robusta de argumentos con control total de errores.
        Nunca permite que el programa termine con excepción del sistema.
        Incluye soporte para argumento de versión -v.
        """
        # Verificar si se solicita la versión
        if len(args) == 2 and args[1] == "-v":
            print(f"versión {VERSION}")
            sys.exit(0)

        # Verificar cantidad de argumentos
        if len(args) != 3:
            print("Error: Número incorrecto de argumentos.")
            self.print_syntax()

        # Intentar convertir a enteros con manejo robusto
        try:
            inf = int(args[1])
        except ValueError as exc:
            print(
                f"Error: El límite inferior '{args[1]}' no es un número "
                f"entero válido: {exc}"
            )
            self.print_syntax()

        try:
            sup = int(args[2])
        except ValueError as exc:
            print(
                f"Error: El límite superior '{args[2]}' no es un número "
                f"entero válido: {exc}"
            )
            self.print_syntax()

        # Validaciones de rango y lógica
        if inf < 0:
            print(f"Error: El límite inferior ({inf}) no puede ser negativo.")
            self.print_syntax()

        if sup > self.max_rango:
            print(
                f"Error: El límite superior ({sup}) no puede exceder "
                f"{self.max_rango}."
            )
            self.print_syntax()

        if inf > sup:
            print(
                f"Error: El límite inferior ({inf}) no puede ser mayor que "
                f"el superior ({sup})."
            )
            self.print_syntax()

        return inf, sup

    def ejecutar(self, args):
        """Método principal de ejecución del singleton."""
        inf, sup = self.validate_args(args)
        self.limpiar_pantalla()
        print(f"Números primos entre {inf} y {sup} son:\n")
        primos = self.obtener_primos_en_rango(inf, sup)
        print(" ".join(map(str, primos)))
        return True


# ------Horizonte De Eventos TM----------------------------------------------------#


def es_primo(n):
    """Retorna True si n es un número primo, False en caso contrario."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Optimización: hasta raíz cuadrada de n
        if n % i == 0:
            return False
    return True


def obtener_primos_en_rango(inf, sup):
    """Devuelve una lista de números primos entre inf y sup (inclusive)."""
    return [n for n in range(inf, sup + 1) if es_primo(n)]


def limpiar_pantalla():
    """Limpia la pantalla en forma multiplataforma."""
    os.system("cls" if os.name == "nt" else "clear")


def validar_argumentos(args):
    """
    Valida que los argumentos de línea de comando sean enteros correctos
    y estén dentro del rango permitido. Incluye soporte para -v.
    """
    # Verificar si se solicita la versión
    if len(args) == 2 and args[1] == "-v":
        print(f"versión {VERSION}")
        sys.exit(0)

    if len(args) != 3:
        raise ValueError(
            "Debe proporcionar exactamente dos argumentos: inicio y fin del rango."
        )
    try:
        inf = int(args[1])
        sup = int(args[2])
    except ValueError as exc:
        raise ValueError("Ambos argumentos deben ser números enteros válidos.") from exc

    if inf > sup:
        raise ValueError("El límite inferior no puede ser mayor que el superior.")
    if sup > MAX_RANGO:
        raise ValueError(f"El límite superior no puede exceder {MAX_RANGO}.")
    if inf < 0:
        raise ValueError("El límite inferior no puede ser negativo.")

    return inf, sup


def main():
    """Función principal que implementa branching by abstraction."""
    # Branching by abstraction: usar nueva implementación si NUEVO = True
    if NUEVO:
        generador = GeneradorPrimosSingleton()
        generador.ejecutar(sys.argv)
    else:
        # Código original preservado
        try:
            inf, sup = validar_argumentos(sys.argv)
            limpiar_pantalla()
            print(f"Números primos entre {inf} y {sup} son:\n")
            primos = obtener_primos_en_rango(inf, sup)
            print(" ".join(map(str, primos)))
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
