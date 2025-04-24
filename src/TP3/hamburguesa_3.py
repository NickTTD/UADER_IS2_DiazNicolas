from __future__ import annotations

from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class HamburguesaCreator(Creator):
    def factory_method(self) -> Product:
        return Hamburguesa()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


class Hamburguesa(Product):
    def operation(self) -> str:
        return "{Hamburguesa lista para ser entregada}"


class EntregaMostrador(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa lista para ser entregada en el mostrador."


class EntregaRetiro(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa lista para ser retirada por el cliente."


class EntregaDelivery(Hamburguesa):
    def operation(self) -> str:
        return "Hamburguesa lista para ser entregada por delivery."


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the Hamburguesa for mostrador delivery.")
    creator = HamburguesaCreator()
    creator.factory_method = EntregaMostrador
    client_code(creator)
    print("\n")

    print("App: Launched with the Hamburguesa for retiro delivery.")
    creator.factory_method = EntregaRetiro
    client_code(creator)
    print("\n")

    print("App: Launched with the Hamburguesa for delivery.")
    creator.factory_method = EntregaDelivery
    client_code(creator)
    print("\n")
