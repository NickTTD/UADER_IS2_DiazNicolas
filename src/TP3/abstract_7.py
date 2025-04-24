# un juego que puede correr en distintas plataformas (Windows, Mac, Linux).
# Cada plataforma tiene su propia forma de crear ventanas y reproducir sonidos

import platform

# ==== Interfaces abstractas de productos ====


class Window:
    def render(self):
        """Mostrar la ventana en pantalla."""
        pass


class Sound:
    def play(self):
        """Reproducir un sonido."""
        pass


# ==== Interfaces abstractas de la fábrica ====


class GameFactory:
    def create_window(self) -> Window:
        pass

    def create_sound(self) -> Sound:
        pass


# ==== Productos concretos para Windows ====


class WindowsWindow(Window):
    def render(self):
        print("🪟 Renderizando ventana en Windows")


class WindowsSound(Sound):
    def play(self):
        print("🔊 Reproduciendo sonido en Windows")


class WindowsFactory(GameFactory):
    def create_window(self) -> Window:
        return WindowsWindow()

    def create_sound(self) -> Sound:
        return WindowsSound()


# ==== Productos concretos para Mac ====


class MacWindow(Window):
    def render(self):
        print("🖥️ Renderizando ventana en Mac")


class MacSound(Sound):
    def play(self):
        print("🔈 Reproduciendo sonido en Mac")


class MacFactory(GameFactory):
    def create_window(self) -> Window:
        return MacWindow()

    def create_sound(self) -> Sound:
        return MacSound()


# ==== Productos concretos para Linux ====


class LinuxWindow(Window):
    def render(self):
        print("🐧 Renderizando ventana en Linux")


class LinuxSound(Sound):
    def play(self):
        print("🎵 Reproduciendo sonido en Linux")


class LinuxFactory(GameFactory):
    def create_window(self) -> Window:
        return LinuxWindow()

    def create_sound(self) -> Sound:
        return LinuxSound()


# ==== Cliente: el juego ====


class Game:
    def __init__(self, factory: GameFactory):
        self.window = factory.create_window()
        self.sound = factory.create_sound()

    def run(self):
        self.window.render()
        self.sound.play()


# ==== Código de uso ====

if __name__ == "__main__":
    os_type = platform.system()

    if os_type == "Windows":
        factory = WindowsFactory()
    elif os_type == "Darwin":
        factory = MacFactory()
    elif os_type == "Linux":
        factory = LinuxFactory()
    else:
        raise Exception(f"Sistema no soportado: {os_type}")

    game = Game(factory)
    game.run()
