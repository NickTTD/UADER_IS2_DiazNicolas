"""
chat_gemini.py
Este script inicializa un modelo de lenguaje de Gemini utilizando la API de Google,
establece un contexto inicial con información local (hora y ubicación), e inicia
un bucle interactivo donde el usuario puede hacer preguntas al modelo.
- Utiliza módulos separados (`config_gemini.py` y `context_gemini.py`) para mejorar
  la organización del código.
- Permite mantener una sesión de chat persistente con el modelo.
- Soporta recuperación de entradas previas gracias al módulo `readline`.
- Maneja errores comunes y señales del sistema como Ctrl+C y Ctrl+D.
"""

# Habilita historial ↑ aunque no se use directamente
import readline  # noqa: F401  # pylint: disable=unused-import # pyright: ignore[reportUnusedImport]

# Error handling
import except_gemini

# Configuración del modelo desde archivo externo
from config_gemini import configurar_modelo
from context_gemini import generar_contexto  # Generación del contexto inicial
from google.api_core import exceptions as google_exceptions

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN Y CONTEXTO
# ──────────────────────────────────────────────────────────────────────────────
# Nombre del modelo a utilizar (puede cambiar según disponibilidad)
CHAT = None  # Variable que contendrá la sesión de chat persistente
try:
    # Crear instancia del modelo usando configuración externa
    model = configurar_modelo()
    # Generar contexto inicial (con hora y ubicación)
    CONTEXTO_INICIAL = generar_contexto()
    # Iniciar sesión de chat con el contexto inicial
    CHAT = model.start_chat(history=[{"role": "user", "parts": [CONTEXTO_INICIAL]}])
except google_exceptions.InvalidArgument as e:
    except_gemini.manejar_error_inicializacion(e)
except google_exceptions.PermissionDenied as e:
    except_gemini.manejar_error_inicializacion(e)
except google_exceptions.ResourceExhausted as e:
    except_gemini.manejar_error_inicializacion(e)
except google_exceptions.GoogleAPIError as e:
    except_gemini.manejar_error_inicializacion(e)
except ConnectionError as e:
    except_gemini.manejar_error_inicializacion(e)
except Exception as e:  # Mantenemos esto como último recurso
    except_gemini.manejar_error_inicializacion(e)

# ──────────────────────────────────────────────────────────────────────────────
# BUCLE INTERACTIVO DE CONSULTA AL MODELO
# ──────────────────────────────────────────────────────────────────────────────
while True:
    try:
        # Leer entrada del usuario (↑ permite recuperar y editar la anterior)
        user_query = input("Ingresa tu consulta (o 'salir' para terminar): ")
        if user_query.lower() == "salir":
            break  # Salir del bucle si el usuario escribe 'salir'
        if user_query.strip():  # Verificar que no sea una entrada vacía
            print(f"You: {user_query}")
            print("------------------")
            try:
                # Enviar la consulta al modelo dentro de la sesión activa
                response = CHAT.send_message(user_query)
                # Imprimir respuesta generada por el modelo
                print(f"Gemini: {response.text}")
                print("------------------")
            except (
                google_exceptions.InvalidArgument
            ) as e:  # Odio todos estos excepts pero no se muy bien como hacerlo de otra manera.
                except_gemini.manejar_error_api(e)
            except google_exceptions.PermissionDenied as e:
                except_gemini.manejar_error_api(e)
            except google_exceptions.ResourceExhausted as e:
                except_gemini.manejar_error_api(e)
            except google_exceptions.GoogleAPIError as e:
                except_gemini.manejar_error_api(e)
            except ConnectionError as e:
                except_gemini.manejar_error_api(e)
            except Exception as e:  # Mantenemos esto como último recurso
                except_gemini.manejar_error_api(e)
        else:
            print("La consulta del usuario está vacía.")
    # Manejo de interrupción con Ctrl+C
    except KeyboardInterrupt:
        except_gemini.manejar_interrupcion()
        break
    # Manejo de fin de entrada (Ctrl+D en UNIX)
    except EOFError:
        except_gemini.manejar_entrada_finalizada()
        break
    # Errores específicos durante la entrada
    except (ValueError, TypeError) as e:
        except_gemini.manejar_error_entrada(e)
    # Cualquier otro error inesperado durante la entrada
    except Exception as e:
        except_gemini.manejar_error_entrada(e)
# ──────────────────────────────────────────────────────────────────────────────
# FIN DEL PROGRAMA
# ──────────────────────────────────────────────────────────────────────────────
print("Programa terminado.")
