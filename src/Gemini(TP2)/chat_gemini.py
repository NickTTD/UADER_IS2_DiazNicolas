"""
chat_gemini.py
Este script inicializa un modelo de lenguaje de Gemini utilizando la API de Google,
establece un contexto inicial con información local (hora y ubicación), e inicia
un bucle interactivo donde el usuario puede hacer preguntas al modelo.
"""

# ───── IMPORTS ────────────────────────────────────────────────────────────────

# Estándar
import readline  # noqa: F401  # pylint: disable=unused-import # pyright: ignore[reportUnusedImport]

# Locales
import except_gemini
from config_gemini import configurar_modelo
from context_gemini import generar_contexto
# Terceros
from google.api_core import exceptions as google_exceptions

# ───── INICIALIZACIÓN DEL MODELO ──────────────────────────────────────────────


def inicializar_chat():
    """Inicializa el modelo Gemini y genera el contexto inicial de conversación."""
    try:
        model = configurar_modelo()
        contexto = generar_contexto()
        return model.start_chat(history=[{"role": "user", "parts": [contexto]}])
    except (
        google_exceptions.InvalidArgument,
        google_exceptions.PermissionDenied,
        google_exceptions.ResourceExhausted,
        google_exceptions.GoogleAPIError,
        ConnectionError,
    ) as e:
        except_gemini.manejar_error_inicializacion(e)
    except Exception as e:  # Catch-all final
        except_gemini.manejar_error_inicializacion(e)
    return None


# ───── PROCESAR CONSULTAS ─────────────────────────────────────────────────────


def procesar_consulta(chat, user_query):
    """Envía una consulta al modelo y muestra la respuesta."""
    try:
        response = chat.send_message(user_query)
        print(f"Gemini: {response.text}")
        print("------------------")
    except (
        google_exceptions.InvalidArgument,
        google_exceptions.PermissionDenied,
        google_exceptions.ResourceExhausted,
        google_exceptions.GoogleAPIError,
        ConnectionError,
    ) as e:
        except_gemini.manejar_error_api(e)
    except Exception as e:  # Catch-all final
        except_gemini.manejar_error_api(e)


# ───── BUCLE INTERACTIVO ──────────────────────────────────────────────────────


def bucle_interactivo(chat):
    """Inicia un bucle interactivo de entrada/salida con el modelo."""
    while True:
        try:
            user_query = input("Ingresa tu consulta (o 'salir' para terminar): ")
            if user_query.lower() == "salir":
                break
            if user_query.strip():
                print(f"You: {user_query}")
                print("------------------")
                procesar_consulta(chat, user_query)
            else:
                print("La consulta del usuario está vacía.")
        except KeyboardInterrupt:
            except_gemini.manejar_interrupcion()
            break
        except EOFError:
            except_gemini.manejar_entrada_finalizada()
            break
        except (ValueError, TypeError) as e:
            except_gemini.manejar_error_entrada(e)
        except Exception as e:  # Catch-all final
            except_gemini.manejar_error_entrada(e)


# ───── PUNTO DE ENTRADA ───────────────────────────────────────────────────────


def main():
    """Punto de entrada principal del programa."""
    chat = inicializar_chat()
    if chat is not None:
        bucle_interactivo(chat)
    print("Programa terminado.")


if __name__ == "__main__":
    main()
