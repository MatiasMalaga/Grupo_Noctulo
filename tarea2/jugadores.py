# jugadores.py
# Clases para el Simulador Mundialista - Selección España
# EIE 434 – Programación 2


class Jugador:
    """Clase padre que representa a un jugador de fútbol genérico."""

    def __init__(self, nombre, edad, altura, dorsal):
        self.nombre = nombre
        self.edad = edad          # años
        self.altura = altura      # metros
        self.dorsal = dorsal

    def correr(self):
        """Método heredado: el jugador corre por la cancha."""
        return f"{self.nombre} está corriendo por la cancha."

    def mostrar_rol(self):
        """Polimorfismo: retorna el rol genérico del jugador."""
        return f"{self.nombre} - Jugador"

    def saludar(self):
        """El jugador se presenta al público."""
        return (f"Hola, soy {self.nombre}, tengo {self.edad} años "
                f"y llevo el dorsal número {self.dorsal}.")

    def mostrar_info(self):
        """Retorna un resumen de los datos básicos del jugador."""
        return (f"[#{self.dorsal}] {self.nombre} | "
                f"Edad: {self.edad} | Altura: {self.altura} m")


class Portero(Jugador):
    """Clase hija que representa a un portero."""

    def __init__(self, nombre, edad, altura, dorsal, atajadas_historicas, partidos_sin_gol):
        super().__init__(nombre, edad, altura, dorsal)
        self.atajadas_historicas = atajadas_historicas
        self.partidos_sin_gol = partidos_sin_gol

    def atajar(self):
        """El portero realiza una atajada."""
        return f"{self.nombre} lanza las manos y detiene el disparo. ¡Qué atajada!"

    def despejar(self):
        """El portero despeja el balón con el puño."""
        return f"{self.nombre} sale de su área y despeja con el puño."

    def mostrar_rol(self):
        """Sobrescritura del método: retorna el rol específico."""
        return f"{self.nombre} - Portero"


class Defensa(Jugador):
    """Clase hija que representa a un defensa."""

    def __init__(self, nombre, edad, altura, dorsal, balones_recuperados, duelos_ganados):
        super().__init__(nombre, edad, altura, dorsal)
        self.balones_recuperados = balones_recuperados
        self.duelos_ganados = duelos_ganados

    def marcar(self):
        """El defensa marca a un rival."""
        return f"{self.nombre} sigue al delantero rival y le cierra los espacios."

    def cortar_pase(self):
        """El defensa intercepta un pase."""
        return f"{self.nombre} lee el juego y corta el pase en profundidad."

    def mostrar_rol(self):
        return f"{self.nombre} - Defensa"


class Mediocampista(Jugador):
    """Clase hija que representa a un mediocampista."""

    def __init__(self, nombre, edad, altura, dorsal, asistencias, pases_completados):
        super().__init__(nombre, edad, altura, dorsal)
        self.asistencias = asistencias
        self.pases_completados = pases_completados

    def dar_pase(self):
        """El mediocampista da un pase al compañero."""
        return f"{self.nombre} controla el balón y distribuye el juego con precisión."

    def recuperar_balon(self):
        """El mediocampista presiona y recupera el balón."""
        return f"{self.nombre} presiona alto y le roba el balón al rival."

    def mostrar_rol(self):
        return f"{self.nombre} - Mediocampista"


class Delantero(Jugador):
    """Clase hija que representa a un delantero."""

    def __init__(self, nombre, edad, altura, dorsal, goles_anotados, regates_exitosos):
        super().__init__(nombre, edad, altura, dorsal)
        self.goles_anotados = goles_anotados
        self.regates_exitosos = regates_exitosos

    def patear_al_arco(self):
        """El delantero remata al arco."""
        return f"{self.nombre} encara al portero y dispara con potencia al arco."

    def regatear(self):
        """El delantero supera a un rival con regate."""
        return f"{self.nombre} amaga, cambia de dirección y deja al defensa en el piso."

    def mostrar_rol(self):
        return f"{self.nombre} - Delantero"