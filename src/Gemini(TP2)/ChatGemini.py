import readline  # Permite usar la flecha ↑ para recuperar la última entrada

from ConfigGemini import configurar_modelo
from ContextGemini import generar_contexto  # Generación del contexto inicial

# Configuración del modelo desde archivo externo

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN Y CONTEXTO
# ──────────────────────────────────────────────────────────────────────────────

# Nombre del modelo a utilizar (puede cambiar según disponibilidad)
model_name = "gemini-2.5-flash-preview-04-17"
chat = None  # Variable que contendrá la sesión de chat persistente

try:
    # Crear instancia del modelo usando configuración externa
    model = configurar_modelo(model_name)

    # Generar contexto inicial (con hora y ubicación)
    contexto_inicial = generar_contexto()

    # Iniciar sesión de chat con el contexto inicial
    chat = model.start_chat(history=[{"role": "user", "parts": [contexto_inicial]}])

except Exception as e:
    print(
        f"Error al inicializar el modelo {model_name} o la sesión de chat inicial: {e}"
    )
    exit()

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
                response = chat.send_message(user_query)

                # Imprimir respuesta generada por el modelo
                print(f"Gemini: {response.text}")
                print("------------------")
            except Exception as e:
                print(f"Error al invocar la API de Gemini: {e}")
        else:
            print("La consulta del usuario está vacía.")

    # Manejo de interrupción con Ctrl+C
    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
        break

    # Manejo de fin de entrada (Ctrl+D en UNIX)
    except EOFError:
        print("\nEntrada finalizada.")
        break

    # Cualquier otro error inesperado durante la entrada
    except Exception as e:
        print(f"Error inesperado durante la entrada del usuario: {e}")

# ──────────────────────────────────────────────────────────────────────────────
# FIN DEL PROGRAMA
# ──────────────────────────────────────────────────────────────────────────────
print("Programa terminado.")
