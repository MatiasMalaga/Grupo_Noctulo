import random
from robot_base import RobotBase


class RobotTresRuedas(RobotBase):
    """
    Robot de tres ruedas (triciclo). Hereda de RobotBase.
    Movimiento moderado, limpieza ligera.
    """

    def __init__(self, nombre: str, radio_rueda: float):
        # Llamar al constructor padre con capacidad de carga de 20 kg
        super().__init__(nombre, capacidad_carga=20.0)
        self.radio_rueda = radio_rueda
        self.ruedas_calibradas = False

    def calibrar_giro(self):
        """Calibra el giro del triciclo usando el radio de rueda."""
        print(f"[{self.get_nombre()}] Calibrando triciclo con ruedas de {self.radio_rueda} cm...")
        self.ruedas_calibradas = True

    def mover(self) -> tuple:
        """Mueve el triciclo: velocidad moderada, giro suave."""
        return self.step(v=0.8, w=0.2)

    def limpiar(self):
        """Consume poca batería y recoge entre 0.5 y 1.5 kg de basura."""
        self._reducir_bateria(2.0)
        basura = random.uniform(0.5, 1.5)
        self._recolectar_basura(basura)


class RobotOruga(RobotBase):
    """
    Robot tipo oruga (tanque). Hereda de RobotBase.
    Movimiento lento, gran capacidad de limpieza.
    """

    def __init__(self, nombre: str, tension_oruga: float):
        # Llamar al constructor padre con capacidad de carga de 50 kg
        super().__init__(nombre, capacidad_carga=50.0)
        self.tension_oruga = tension_oruga

    def ajustar_tension(self):
        """Muestra la tensión configurada en las orugas."""
        print(f"[{self.get_nombre()}] Ajustando tension de las orugas al {self.tension_oruga} %.")

    def mover(self) -> tuple:
        """Movimiento lento pero con giro fuerte."""
        return self.step(v=0.3, w=0.8)

    def limpiar(self):
        """Consume bastante batería pero recoge entre 2.0 y 4.0 kg de basura."""
        self._reducir_bateria(4.5)
        basura = random.uniform(2.0, 4.0)
        self._recolectar_basura(basura)


class RobotDron(RobotBase):
    """
    Robot dron aéreo. Hereda de RobotBase.
    Muy rápido, poca capacidad de carga.
    """

    def __init__(self, nombre: str, altura_maxima: float):
        # Llamar al constructor padre con capacidad de carga de 5 kg
        super().__init__(nombre, capacidad_carga=5.0)
        self.altura_maxima = altura_maxima
        self.en_vuelo = False

    def despegar(self):
        """Inicia el vuelo del dron."""
        print(f"[{self.get_nombre()}] Despegando hasta {self.altura_maxima} metros de altura.")
        self.en_vuelo = True

    def mover(self) -> tuple:
        """
        Se mueve rápido si está en vuelo.
        Si no está en vuelo, retorna sin moverse.
        """
        if self.en_vuelo:
            return self.step(v=2.5, w=1.0)
        return 0.0, False

    def limpiar(self):
        """Solo limpia si está en vuelo. Consume 3.0 de batería y recoge material ligero."""
        if self.en_vuelo:
            self._reducir_bateria(3.0)
            basura = random.uniform(0.1, 0.4)
            self._recolectar_basura(basura)
