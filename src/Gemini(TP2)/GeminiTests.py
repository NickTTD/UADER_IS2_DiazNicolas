import os
import readline
from datetime import datetime

import google.generativeai as genai

# Validar que la clave esté presente
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("Error: No se encontró la variable de entorno 'GOOGLE_API_KEY'.")
    exit()

# Configurar la clave de API
genai.configure(api_key=api_key)

# Acceder al modelo Gemini Pro (o el modelo que estés usando)
model_name = "gemini-2.5-flash-preview-04-17"
chat = None  # Inicializar la variable chat fuera del bloque try

try:
    model = genai.GenerativeModel(model_name)

    # Inicializar la sesión de chat la primera vez
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    fecha_actual = now.strftime("%A, %B %d, %Y")
    context_inicial = (
        f"La hora actual es {current_time} del {fecha_actual}. "
        "El usuario se encuentra en Concepción del Uruguay, Entre Ríos Province, Argentina. "
        "Responde a las siguientes consultas teniendo en cuenta esta información:"
    )

    chat = model.start_chat(history=[{"role": "user", "parts": [context_inicial]}])

except Exception as e:
    print(
        f"Error al inicializar el modelo {model_name} o la sesión de chat inicial: {e}"
    )
    exit()

# Bucle principal
while True:
    try:
        user_query = input("Ingresa tu consulta (o 'salir' para terminar): ")
        if user_query.lower() == "salir":
            break

        if user_query.strip():
            print(f"You: {user_query}")
            print("------------------")
            try:
                response = chat.send_message(user_query)
                print(f"Gemini: {response.text}")
                print("------------------")
            except Exception as e:
                print(f"Error al invocar la API de Gemini: {e}")
        else:
            print("La consulta del usuario está vacía.")

    except KeyboardInterrupt:
        print("\nSaliendo del programa.")
        break
    except EOFError:
        print("\nEntrada finalizada.")
        break
    except Exception as e:
        print(f"Error inesperado durante la entrada del usuario: {e}")

print("Programa terminado.")
