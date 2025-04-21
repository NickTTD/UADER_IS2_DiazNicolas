import os

import google.generativeai as genai

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE LA API
# ──────────────────────────────────────────────────────────────────────────────


def configurar_modelo(nombre_modelo):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "No se encontró la variable de entorno 'GOOGLE_API_KEY'."
        )

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(nombre_modelo)
