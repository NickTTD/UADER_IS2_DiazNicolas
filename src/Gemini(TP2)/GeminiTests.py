import os
from datetime import datetime

import google.generativeai as genai

# Configurar la clave de API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Acceder al modelo Gemini Pro (o el modelo que estés usando)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

# Obtener la consulta del usuario
user_query = input("Ingresa tu consulta: ")

# Verificar si la consulta tiene texto
if user_query.strip():
    # Obtener la hora actual
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")

    # Definir el contexto relevante
    context = f"La hora actual es {current_time} del {now.strftime('%A, %B %d, %Y')}. El usuario se encuentra en Concepción del Uruguay, Entre Ríos Province, Argentina. Responde a la siguiente consulta teniendo en cuenta esta información:"

    # Imprimir la consulta del usuario con el prefijo "You:"
    print(f"You: {user_query}")

    # Iniciar una sesión de chat con el contexto en el primer mensaje
    chat = model.start_chat(history=[{"role": "user", "parts": [context]}])

    # Enviar la consulta del usuario al chat
    response = chat.send_message(user_query)

    # Imprimir la respuesta del modelo con el prefijo "Gemini:"
    print(f"Gemini: {response.text}")

else:
    print("La consulta del usuario está vacía.")
