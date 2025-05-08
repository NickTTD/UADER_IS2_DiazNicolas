from abc import ABC, abstractmethod

# Decidí por una bicicleta que tiene
# Un Cuadro, "transmision", y frenos.
# Añadí un depth-meter que indica en que nivel del árbol estamos
# 0 sería el componente base (O tronco del arbol), y va aumentando.
# Subconjunto es una rama, Pieza es una hoja.


# Componente base
class ComponenteBicicleta(ABC):
    """
    Interfaz base para todos los componentes de la bicicleta,
    ya sean piezas simples o subconjuntos compuestos.
    """

    @abstractmethod
    def mostrar(self, depth=0):
        """
        Muestra el nombre del componente con su depth jerárquico.
        """


# === Hoja ===
class Pieza(ComponenteBicicleta):
    """
    Representa una pieza individual de la bicicleta (hoja del patrón Composite).
    """

    def __init__(self, nombre: str):
        self.nombre = nombre

    def mostrar(self, depth=0):
        print("  " * depth + f"[Depth: {depth}] - Pieza: {self.nombre}")


# === Composite ===
class Subconjunto(ComponenteBicicleta):
    """
    Representa un subconjunto compuesto de varias piezas o incluso otros subconjuntos.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente: ComponenteBicicleta):
        """
        Agrega un componente (pieza o subconjunto) al subconjunto.
        """
        self.componentes.append(componente)

    def mostrar(self, depth=0):
        print("  " * depth + f"[Depth: {depth}] > Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(depth + 1)


# === Producto principal ===
class BicicletaCompleta(Subconjunto):
    """
    Representa la bicicleta completa, que es un subconjunto de alto depth.
    Hereda de Subconjunto para reutilizar la lógica del composite.
    """

    def __init__(self):
        super().__init__("Bicicleta Completa")


# === Test ===
if __name__ == "__main__":
    # Crear subconjuntos principales
    cuadro = Subconjunto("Cuadro")
    cuadro.agregar(Pieza("Tubo superior"))
    cuadro.agregar(Pieza("Tubo inferior"))
    cuadro.agregar(Pieza("Tubo del asiento"))
    cuadro.agregar(Pieza("Soldaduras"))

    transmision = Subconjunto("Transmisión")
    cadena = Subconjunto("Cadena")
    cadena.agregar(Pieza("Eslabón1"))
    cadena.agregar(Pieza("Eslabón2"))
    cadena.agregar(Pieza("Eslabón3"))
    transmision.agregar(cadena)
    transmision.agregar(Pieza("Piñón"))
    transmision.agregar(Pieza("Plato"))
    transmision.agregar(Pieza("Pedales"))

    frenos = Subconjunto("Frenos")
    frenos.agregar(Pieza("Manetas"))
    frenos.agregar(Pieza("Cables"))
    frenos.agregar(Pieza("Zapatas"))
    frenos.agregar(Pieza("Calipers"))

    # Crear el subconjunto opcional
    portabotellas = Subconjunto("Portabotellas (opcional)")
    portabotellas.agregar(Pieza("Soporte metálico"))
    portabotellas.agregar(Pieza("Tornillo 1"))
    portabotellas.agregar(Pieza("Tornillo 2"))
    portabotellas.agregar(Pieza("Abrazadera"))

    # Ensamblar la bicicleta
    bicicleta = BicicletaCompleta()
    bicicleta.agregar(cuadro)
    bicicleta.agregar(transmision)
    bicicleta.agregar(frenos)
    # bicicleta.agregar(portabotellas)  # Agregar el subconjunto opcional

    # Mostrar la estructura jerárquica
    bicicleta.mostrar()
