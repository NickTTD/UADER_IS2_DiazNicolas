import platform  # No es necesario pero lo usé para probar algo
import subprocess


class Ping:
    """
    Clase que permite realizar pings a direcciones IP.
    Usa el comando del sistema operativo para hacer 10 intentos de ping.
    """

    def execute(self, ip: str):
        """
        Realiza un ping de 10 intentos a la dirección IP indicada,
        solo si comienza con '192.'.
        """
        if not ip.startswith("192."):
            raise ValueError("Dirección IP no permitida. Debe comenzar con '192.'")
        self._ping(ip)

    def executefree(self, ip: str):
        """
        Realiza un ping de 10 intentos a cualquier dirección IP, sin restricciones.

        Args:
            ip (str): Dirección IP o dominio a la que se desea hacer ping.
        """
        self._ping(ip)

    def _ping(self, ip: str):
        """
        Ejecuta el comando 'ping' del sistema operativo.

        Args:
            ip (str): Dirección IP o dominio a la que se desea hacer ping.
        """
        print(f"Pinging {ip} (10 intentos)...")
        try:
            # Detecta si el sistema es Windows o Unix-like, irrelevante al problema pero
            # quería probar algo
            count_flag = "-n" if platform.system().lower() == "windows" else "-c"
            subprocess.run(["ping", count_flag, "10", ip], check=True)
        except subprocess.CalledProcessError:
            print(f"Error: No se pudo hacer ping a {ip}.")


class PingProxy:
    """
    Clase Proxy para controlar el acceso a la clase Ping.
    Intercepta ciertos valores de IP y redirige el comportamiento.
    """

    def __init__(self):
        """
        Inicializa la instancia real de la clase Ping.
        """
        self._real_ping = Ping()

    def execute(self, ip: str):
        """
        Ejecuta un ping con reglas específicas:
        - Si la IP es '192.168.0.254', hace ping a www.google.com sin restricción.
        - Para otras IPs, delega a Ping.execute().

        Args:
            ip (str): Dirección IP a analizar y a la cual redirigir el ping.
        """
        if ip == "192.168.0.254":
            print(
                "IP especial detectada, haciendo ping a www.google.com usando executefree()"
            )
            self._real_ping.executefree("www.google.com")
        else:
            self._real_ping.execute(ip)


# test
if __name__ == "__main__":
    proxy = PingProxy()
    proxy.execute("192.168.0.254")  # debería ir a .executeFree (google)
    proxy.execute("192.168.100.10")  # ping a mi ip local
    proxy.execute("10.0.0.1")  # except
