import math

class RobotBase:
    """
    Clase base (superclase) para todos los robots de limpieza.
    Implementa la cinemática fundamental, encapsulamiento y métodos estáticos.
    """

    def __init__(self, nombre: str, capacidad_carga: float,
                 x_inicial: float = 0.0, y_inicial: float = 0.0, yaw_inicial: float = 0.0):
        # Atributos privados (doble guion bajo)
        self.__nombre = nombre
        self.__capacidad_carga = capacidad_carga
        self.__bateria = 100.0
        self.__pos_x = x_inicial
        self.__pos_y = y_inicial
        self.__yaw = yaw_inicial
        self.__basura_recolectada = 0.0
        self.__step_dt = 0.1  # Intervalo de tiempo por paso de simulación

        # Atributos públicos: coordenadas objetivo
        self.target_x = 5.0
        self.target_y = 5.0

    # -------------------------
    # Getters (acceso público)
    # -------------------------
    def get_nombre(self) -> str:
        return self.__nombre

    def get_bateria(self) -> float:
        return self.__bateria

    def get_pos_x(self) -> float:
        return self.__pos_x

    def get_pos_y(self) -> float:
        return self.__pos_y

    def get_yaw(self) -> float:
        return self.__yaw

    def get_basura_recolectada(self) -> float:
        return self.__basura_recolectada

    # -------------------------
    # Métodos protegidos
    # -------------------------
    def _actualizar_pose(self, x: float, y: float, yaw: float):
        """Sobreescribe la posición y orientación actual del robot."""
        self.__pos_x = x
        self.__pos_y = y
        self.__yaw = yaw

    def _reducir_bateria(self, cantidad: float):
        """Resta la cantidad indicada a la batería, nunca por debajo de 0."""
        self.__bateria = max(0.0, self.__bateria - cantidad)

    def _recolectar_basura(self, cantidad: float):
        """
        Agrega basura recolectada respetando la capacidad máxima.
        Solo suma el espacio disponible restante.
        """
        espacio_disponible = self.__capacidad_carga - self.__basura_recolectada
        if espacio_disponible > 0:
            self.__basura_recolectada += min(cantidad, espacio_disponible)

    # -------------------------
    # Métodos estáticos
    # -------------------------
    @staticmethod
    def calc_dist_to_goal(pos_x: float, pos_y: float, target_x: float, target_y: float) -> float:
        """Calcula la distancia Euclidiana entre la posición actual y la meta."""
        return math.sqrt((target_x - pos_x) ** 2 + (target_y - pos_y) ** 2)

    @staticmethod
    def calc_yaw_error(pos_x: float, pos_y: float, yaw: float,
                       target_x: float, target_y: float) -> float:
        """
        Calcula el error angular hacia el objetivo,
        normalizado al rango [-π, π].
        """
        theta_meta = math.atan2(target_y - pos_y, target_x - pos_x)
        err = theta_meta - yaw
        # Normalizar al rango [-π, π]
        err_norm = (err + math.pi) % (2 * math.pi) - math.pi
        return err_norm

    # -------------------------
    # Simulación cinemática
    # -------------------------
    def step(self, v: float, w: float) -> tuple:
        """
        Avanza un paso de simulación con velocidad lineal v y angular w.
        Retorna (recompensa, llegamos).
        """
        # Si la batería se agotó, el robot se detiene
        if self.__bateria <= 0:
            return 0.0, True

        dt = self.__step_dt

        # Calcular nuevo yaw y normalizar a [-π, π]
        nuevo_yaw = self.__yaw + w * dt
        nuevo_yaw = (nuevo_yaw + math.pi) % (2 * math.pi) - math.pi

        # Calcular nuevas posiciones
        nuevo_x = self.__pos_x + v * math.cos(nuevo_yaw) * dt
        nuevo_y = self.__pos_y + v * math.sin(nuevo_yaw) * dt

        # Guardar la nueva pose
        self._actualizar_pose(nuevo_x, nuevo_y, nuevo_yaw)

        # Calcular distancia y error angular con métodos estáticos
        distancia = RobotBase.calc_dist_to_goal(nuevo_x, nuevo_y, self.target_x, self.target_y)
        error_angular = RobotBase.calc_yaw_error(nuevo_x, nuevo_y, nuevo_yaw,
                                                  self.target_x, self.target_y)

        # Recompensa: penalizar lejanía y desvío
        reward = -distancia - abs(error_angular)

        # Verificar si llegó a la meta (distancia < 0.5 m)
        llegamos = distancia < 0.5
        if llegamos:
            reward += 100

        return reward, llegamos

    # -------------------------
    # Métodos abstractos
    # -------------------------
    def mover(self):
        """Las clases hijas deben implementar este método."""
        raise NotImplementedError("La clase hija debe implementar el método mover().")

    def limpiar(self):
        """Las clases hijas deben implementar este método."""
        raise NotImplementedError("La clase hija debe implementar el método limpiar().")