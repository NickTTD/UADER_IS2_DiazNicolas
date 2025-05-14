class CharSequence:
    """
    Clase que representa una secuencia de caracteres con iteradores directos e inversos.
    """

    def __init__(self, data):
        """
        Inicializa la secuencia con una cadena de texto.

        Args:
            data (str): La cadena a almacenar.
        """
        self._data = data

    def __iter__(self):
        """
        Devuelve un iterador para recorrer la cadena en orden directo.
        """
        return ForwardIterator(self._data)

    def reverse_iterator(self):
        """
        Devuelve un iterador para recorrer la cadena en orden inverso.
        """
        return ReverseIterator(self._data)


class ForwardIterator:
    """
    Iterador para recorrer una cadena carácter por carácter en orden directo (izquierda a derecha).
    Se utiliza implícitamente con un bucle `for` sobre una instancia de CharSequence.
    """

    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        char = self._data[self._index]
        self._index += 1
        return char


class ReverseIterator:
    """
    Iterador para recorrer una cadena carácter por carácter en orden inverso (derecha a izquierda).
    Se accede a través del método `reverse_iterator()` de CharSequence.
    """

    def __init__(self, data):
        self._data = data
        self._index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        char = self._data[self._index]
        self._index -= 1
        return char


# === Ejemplo de uso ===

# Crear una secuencia de texto
seq = CharSequence("Hola mundo")

# Recorrer en orden directo
print("Iteración directa:")
for c in seq:  # Usa automáticamente ForwardIterator gracias a __iter__()
    print(c, end=" ")  # End vacío para que lo escriba en una linea y no en vertical

print()
print("\nIteración inversa:")
# Recorrer en orden inverso usando el iterador explícito
for c in seq.reverse_iterator():
    print(c, end=" ")
