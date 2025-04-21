import os

import google.generativeai as genai

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DEL MODELO
# ──────────────────────────────────────────────────────────────────────────────
# Nombre del modelo a utilizar (puede cambiar según disponibilidad)
MODEL_NAME = "gemini-2.5-flash-preview-04-17"


# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE LA API
# ──────────────────────────────────────────────────────────────────────────────
def configurar_modelo(nombre_modelo=None):
    # Si no se proporciona un nombre específico, usar el predeterminado
    if nombre_modelo is None:
        nombre_modelo = MODEL_NAME

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "No se encontró la variable de entorno 'GOOGLE_API_KEY'."
        )
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(nombre_modelo)
