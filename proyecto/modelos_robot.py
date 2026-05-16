import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

from robot_base import RobotBase


class RobotTresRuedas(RobotBase):

    
    def __init__(self, nombre, radio_rueda): #recibe parametros de la clase hija
        
        super().__init__(nombre, capacidad_carga=20.0) #se pasan los datos que maneja el padre a la clase padre
        
        self.ruedas_calibradas=False
        self.radio_rueda=radio_rueda

    def calibrar_giro(self):
        print("calibrando ruedas con su radio")
        self.ruedas_calibradas=True # na´mas un mensaje y actualzacion de estado
        print("ruedas calibradas")

    def mover(self):
        reward,estado=self.step(0.8,0.2)
        return reward, estado
    
    def limpiar(self):
        self._reducir_bateria(2.0)
        self._recolectar_basura(np.random.uniform(0.5,1.5))

class RobotOruga(RobotBase):

    def __init__(self, nombre, tension_oruga): #recibe parametros de la clase hija
        
        super().__init__(nombre, capacidad_carga=50.0) #se pasan los datos que maneja el padre a la clase padre
        
        self.tension_oruga=tension_oruga
    
    def ajustar_tension(self):
        print(f"la tension actual es: {self.tension_oruga}")

    def mover(self):
        reward,estado=self.step(0.3,0.8)
        return reward, estado
    
    def limpiar(self):
        self._reducir_bateria(4.5)
        self._recolectar_basura(np.random.uniform(2.0,4.0))

class RobotDron(RobotBase):
   
    def __init__(self, nombre, altura_maxima): #recibe parametros de la clase hija
        
        super().__init__(nombre, capacidad_carga=5.0) #se pasan los datos que maneja el padre a la clase padre
        
        self.altura_maxima=altura_maxima
        self.en_vuelo=False
    
    def despegar(self):
        print("altura maxima: {self.altura_maxima}")
        self.en_vuelo=True
    
    def mover(self):
        if self.en_vuelo==True:
            reward,estado=self.step(2.5,1.0)
            return reward, estado
        else:
            return 0.0, False
    
    def limpiar(self):
        self._reducir_bateria(3.0)
        self._recolectar_basura(np.random.uniform(0.1,0.4))
