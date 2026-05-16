import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod






# Atributos y Encapsulamiento

class RobotBase:
    
    # El constructor __init__ debe recibir: nombre (str) y capacidad_carga (float), la posición inicial x_inicial=0.0, y_inicial=0.0 y el ángulo inicial yaw_inicial=0.0.
    def __init__(self,nombre, capacidad_carga, x_inicial=0.0, y_inicial=0.0, yaw_inicial=0.0):
        

        # Regla estricta: Los siguientes atributos deben ser estrictamente privados (usando doble guion bajo __):
        self.__nombre=nombre # __nombre: el nombre del robot.
        self.__capacidad_carga=capacidad_carga # __capacidad_carga: máximo de basura en kg que puede llevar.
        self.__bateria=100 # __bateria: inicializada en 100,0 (%).
        self.__pos_x=x_inicial # __pos_x,
                                        # posición actual (inician con los valores por defecto).
        self.__pos_y=y_inicial # __pos_y:
        self.__yaw=yaw_inicial # __yaw: ángulo de orientación actual en radianes.
        self.__basura_recolectada=0.0 # __basura_recolectada: inicializada en 0,0.
        self.__step_dt=0.1 # __step_dt: el intervalo de tiempo por cada paso de simulación, fijar en 0,1.
        
        # Además, el robot debe tener dos atributos públicos para almacenar las coordenadas a las que se dirige. Defina target_x = 5.0 y target_y = 5.0.
        self.target_x=5.0
        self.target_y=5.0

    # Para que el exterior (como main.py) pueda acceder a las variables privadas, deben crear los correspondientes getters:
    def get_nombre(self): # get_nombre()
        return self.__nombre 
    
    def get_bateria(self): # get_bateria()
        return self.__bateria
    
    def get_pos_x(self): #  get_pos_x()
        return self.__pos_x
    
    def get_pos_y(self): # get_pos_y()
        return self.__pos_y
    
    def get_yaw(self): # get_yaw()
        return self.__yaw
    
    def get_basura_recolectada(self): #  get_basura_recolectada()
        return self.__basura_recolectada
    
    # También implemente métodos internos protegidos (con un solo guion bajo _) para modificar atributos sin exponerlos al exterior:
    def _actualizar_pose(self,x, y, yaw): # _actualizar_pose(x, y, yaw): sobreescribe la posición y orientación actual.
        self.__pos_x=x
        self.__pos_y=y #setea los valores viejos con los nuevos
        self.__yaw=yaw

    def _reducir_bateria(self, cantidad): # _reducir_bateria(cantidad): resta la cantidad a la batería, asegurando que nunca sea menor a 0.
        if self.__bateria-cantidad>=0: #bueno si la resta es mayor a 0
            self.__bateria-=cantidad #actualiza el valor de la bateria
        else:
            self.__bateria=0 #y si da menor a 0 pues la bateria se setea en cero
    
    def _recolectar_basura(self, cantidad): # _recolectar_basura(cantidad): agrega basura, pero debe verificar que no se supere la __capacidad_carga máxima. Sólo puede sumar el espacio que quede disponible.
        
        if cantidad>0: #bueno este si lo explicare, si la cantidad es mayor a 0, calcula esto:
            
            if self.__capacidad_carga < cantidad+self.get_basura_recolectada(): # aqui comparamos si la cantidad que recolecta ahora, + la que ya tenia almacenada (getter)
                self.__basura_recolectada=self.__capacidad_carga #es mayor a la capacidad de carga del robot, el robot se "llena" a su capacidad maxima
        
            elif self.get_basura_recolectada()+cantidad<=self.__capacidad_carga: # si resuelta que lo suma es menor a la capacidad decarga del robot
                self.__basura_recolectada+=cantidad # entonces solo se la sumamos a la que ya tiene
        else:
            print("error con carga negativa") # y esto? por si acaso, aunque seria raro que el robot recolecte negativo, y no se ya que hice algo similar con la bateria, por que no? 
                                            # no me juzguen que programo en la madrugada y hago cosas por los loles

    # Métodos Estáticos

    # 1)  calc_dist_to_goal(pos_x, pos_y, target_x, target_y) 
    @staticmethod    #metodo estatico
    def calc_dist_to_goal(pos_x,pos_y,target_x,target_y): 
        d=np.sqrt((target_x-pos_x)**2 +(target_y-pos_y)**2) #esto calcula una formula del PDF

        return d # y le puse d como en la ecuacion XD

    # 2)  calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y)
    @staticmethod    #metodo estatico
    def calc_yaw_error(pos_x, pos_y, yaw, target_x, target_y):
        θmeta = np.atan2(target_y - pos_y,target_x - pos_x)  # ecuacion del PDF
        err=θmeta-yaw # El error inicial es err = θmeta − yaw. segun PDF
        err_norm=((err+np.pi) % (2*np.pi))-np.pi # otra ecuacion del PDF, aunque esta costo mas, estaba "mal escrita" y se la tuve que pasar a la IA para que me dijiera que madres era mod, y con acento mód, es modulo, modulo, no mód carajo
        return err_norm # y ya, devuelve el error
    
    # Simulación Cinemática (step(v, w))
    def step(self, v, w):
        #1)  Si la batería ≤ 0, el robot se detiene: retornar recompensa 0,0 y un booleano True (indicando que terminó)
        if self.get_bateria()<=0:
             reward=0.0
             return reward, True 
        
        #2)  Calcular el nuevo yaw: yawnuevo = yaw + w ·dt, y normalizarlo entre [−π,π] (usando la misma fórmula de normalización).
        yaw_nuevo=self.get_yaw()+w*self.__step_dt
        yaw_norm=((yaw_nuevo+np.pi) % (2*np.pi))-np.pi #tambien le pregunte a la IA, no se como se usa esa ecuacion y no se normalizar con ella asique pregunte, ni modo
        
        #3)  Calcular nuevas posiciones (ecuaciones en el PDF)
        x_new=self.get_pos_x()+v*np.cos(yaw_norm)*self.__step_dt
        y_new=self.get_pos_y()+v*np.sin(yaw_norm)*self.__step_dt
        
        #4) Usar _actualizar_pose para guardar los nuevos valores
        self._actualizar_pose(x_new,y_new,yaw_norm)
        
        #5 Calcular la distancia y el error angular actual usando los métodos estáticos implementados anteriormente
        distancia=self.calc_dist_to_goal() # na´ mas se les llama
        erro_angular=self.calc_yaw_error() # ya se actualizaron los valores en el paso anterior 
        
        #6  La recompensa en este paso se calcula penalizando la lejanía y el desvío: reward = −distancia − |error_angular|
        reward=-distancia-np.absolute(erro_angular) #pues esa formula
        
        #7) Determinar si el robot llegó a la meta (llegamos = True) si la distancia es menor a 0,5 metros. Si es así, sumar 100 a la recompensa
        if distancia<0.5:
            reward+=100
            #8) Retornar la tupla (reward, llegamos).
            return reward, True
        
    # Métodos Abstractos

    @abstractmethod #mucho texto, solo quieren que todas las hijas tengan estos metodos si no dan error
    def mover(self):
        pass

    @abstractmethod
    def limpiar(self):
        pass
    


   