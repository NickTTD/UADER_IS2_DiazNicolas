from datetime import datetime

# ──────────────────────────────────────────────────────────────────────────────
# INICIALIZACIÓN DEL MODELO Y CONTEXTO
# ──────────────────────────────────────────────────────────────────────────────


def generar_contexto():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    fecha_actual = now.strftime("%A, %B %d, %Y")

    return (
        f"La hora actual es {current_time} del {fecha_actual}. "
        "El usuario se encuentra en Concepción del Uruguay, Entre Ríos Province, Argentina. "
        "Responde a las siguientes consultas teniendo en cuenta esta información:"
    )
