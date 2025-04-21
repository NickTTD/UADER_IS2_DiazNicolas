"""
except_gemini.py
Este módulo contiene funciones para manejar las excepciones específicas
de la API de Gemini y otras excepciones comunes que pueden ocurrir durante
la ejecución del chat con el modelo.
"""

import sys
from typing import Any

# Importar excepciones específicas de la API de Google
from google.api_core import exceptions as google_exceptions


def manejar_error_inicializacion(error: Exception) -> None:
    """
    Maneja los errores que ocurren durante la inicialización del modelo.

    Args:
        error: La excepción capturada durante la inicialización.
    """
    print("\nError al inicializar el modelo de Gemini:", file=sys.stderr)

    if isinstance(error, google_exceptions.PermissionDenied):
        print(
            "El contexto inicial contiene contenido bloqueado por las políticas de seguridad.",
            file=sys.stderr,
        )
    elif isinstance(error, google_exceptions.InvalidArgument):
        print(
            "Error en los parámetros proporcionados al modelo:", error, file=sys.stderr
        )
    elif isinstance(error, google_exceptions.ResourceExhausted):
        print(
            "Se ha agotado la cuota de API o límite de tokens:", error, file=sys.stderr
        )
        print(
            "Verifica los límites de tu cuenta o espera antes de intentar nuevamente.",
            file=sys.stderr,
        )
    elif isinstance(error, google_exceptions.GoogleAPIError):
        print(f"Error de la API de Google: {error}", file=sys.stderr)
        print("Verifica tu clave API y conexión a internet.", file=sys.stderr)
    elif isinstance(error, ConnectionError):
        print("Error de conexión con la API de Gemini.", file=sys.stderr)
        print("Verifica tu conexión a internet.", file=sys.stderr)
    else:
        print(f"Error inesperado: {error}", file=sys.stderr)

    print("El programa no puede continuar sin inicializar el modelo.", file=sys.stderr)
    sys.exit(1)


def manejar_error_api(error: Exception) -> None:
    """
    Maneja los errores que ocurren durante las llamadas a la API de Gemini.

    Args:
        error: La excepción capturada durante la consulta a la API.
    """
    print("\nError al procesar la consulta:", file=sys.stderr)

    if isinstance(error, google_exceptions.PermissionDenied):
        print(
            "Tu consulta contiene contenido bloqueado por las políticas de seguridad.",
            file=sys.stderr,
        )
        print("Por favor, reformula tu pregunta.", file=sys.stderr)
    elif isinstance(error, google_exceptions.InvalidArgument):
        print(f"Error en los parámetros de la consulta: {error}", file=sys.stderr)
        print("Intenta reformular tu pregunta.", file=sys.stderr)
    elif isinstance(error, google_exceptions.ResourceExhausted):
        print(
            "Se ha agotado la cuota de API o límite de tokens:", error, file=sys.stderr
        )
        print(
            "Intenta con una consulta más corta o espera antes de intentar nuevamente.",
            file=sys.stderr,
        )
    elif isinstance(error, google_exceptions.GoogleAPIError):
        print(f"Error de la API de Google: {error}", file=sys.stderr)
        print(
            "Puede ser un problema temporal. Intenta nuevamente más tarde.",
            file=sys.stderr,
        )
    elif isinstance(error, ConnectionError):
        print("Error de conexión con la API de Gemini.", file=sys.stderr)
        print("Verifica tu conexión a internet.", file=sys.stderr)
    else:
        print(f"Error inesperado: {error}", file=sys.stderr)


def manejar_interrupcion() -> None:
    """
    Maneja la interrupción del programa mediante Ctrl+C.
    """
    print("\nPrograma interrumpido por el usuario (Ctrl+C).")


def manejar_entrada_finalizada() -> None:
    """
    Maneja la señal de fin de entrada (Ctrl+D en UNIX, Ctrl+Z en Windows).
    """
    print("\nEntrada finalizada por el usuario (Ctrl+D/Ctrl+Z).")


def manejar_error_entrada(error: Exception) -> None:
    """
    Maneja errores que ocurren durante la entrada del usuario.

    Args:
        error: La excepción capturada durante la entrada.
    """
    print(f"\nError en la entrada: {error}", file=sys.stderr)
    print("Intenta de nuevo con una entrada válida.", file=sys.stderr)
