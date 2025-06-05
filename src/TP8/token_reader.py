"""
Este es una modificación del código original de mi get_jason.py del tp6
transformado a singleton
"""

import json
import sys


class JSONTokenReader:
    """
    Lee tokens desde un archivo json.
    Primer argumento es el archivo, segundo argumento (opcional)token, ej:
    python getJasonEdit.py sitedata.json token2
    """

    def __init__(self, filepath):
        """
        Inicializa el lector con la ruta al archivo JSON.

        :param filepath: Ruta al archivo JSON.
        """
        self.filepath = filepath
        self.data = self._load_json()

    def _load_json(self):
        """
        Carga el contenido del archivo JSON y lo parsea.

        :return: Diccionario con los datos del JSON.
        """
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {self.filepath}")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error al parsear el JSON en el archivo: {self.filepath}")
            sys.exit(1)

    def get_token(self, key):
        """
        Devuelve el valor del token para la clave dada.

        :param key: Clave del token a buscar.
        :return: Valor asociado a la clave o None si no existe.
        """
        return self.data.get(key)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python getJason.py <archivo_json> [clave_token]")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) > 2 else "token1"

    reader = JSONTokenReader(jsonfile)
    token = reader.get_token(jsonkey)

    if token is not None:
        print(token)
    else:
        print(f"Clave '{jsonkey}' no encontrada.")
