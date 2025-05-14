import os


# *--------------------------------------------------------------------
# * Design pattern memento, ejemplo extendido para múltiples estados
# *-------------------------------------------------------------------
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:

    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        """Crea un memento con el estado actual"""
        return Memento(self.file, self.content)

    def undo(self, memento):
        """Restaura el estado a partir del memento dado"""
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:

    def __init__(self):
        # Lista para almacenar hasta 4 mementos
        self.history = []

    def save(self, writer):
        """Guarda un nuevo memento, manteniendo máximo 4 estados"""
        memento = writer.save()
        self.history.append(memento)
        if len(self.history) > 4:
            # Eliminar el estado más antiguo si hay más de 4
            self.history.pop(0)

    def undo(self, writer, index=0):
        """
        Restaura un estado anterior según el índice:
        index=0: estado inmediato anterior
        index=1,2,3: estados más antiguos
        """
        # Validar índice dentro del rango válido
        if not self.history:
            print("No hay estados guardados para restaurar.")
            return

        if index < 0 or index >= len(self.history):
            print(f"Índice inválido {index}. Rango válido: 0 a {len(self.history)-1}")
            return

        # Restaurar el estado deseado
        memento = self.history[-(index + 1)]
        writer.undo(memento)


if __name__ == "__main__":

    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("se invoca al <undo> índice 0 (inmediato anterior)")
    caretaker.undo(writer, 0)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> índice 1 (estado anterior al inmediato)")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("se invoca al <undo> índice 3 (estado más antiguo)")
    caretaker.undo(writer, 3)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
