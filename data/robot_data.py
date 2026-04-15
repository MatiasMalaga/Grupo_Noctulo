import numpy as np

print("hola mundo")

#a) extraer datos de las tablas a diccionarios 12 claves con 10 claves internas por cada
def cargar_experimentos(): #extraidos de las tablas 6, 7 y 8 del paper. pd: estoy cansado de los diccionarios
    experimentos = {

        #tabla6 ruta simple
        "exp1": {"politica": "PPO", "ambiente": "real", "ruta": "simple",
                 "ISE": 434.99, "IAE": 135.93, "ITSE": 6932.79, "ITAE": 2601.61,
                 "tiempo_s": None, "pasos": None, "reward_medio": None},

        "exp2": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "simple",
                 "ISE": 362.85, "IAE": 128.92, "ITSE": 5869.30, "ITAE": 2669.86,
                 "tiempo_s": None, "pasos": None, "reward_medio": None},

        "exp3": {"politica": "PPO", "ambiente": "simulated", "ruta": "simple",
                 "ISE": 73.35, "IAE": 24.51, "ITSE": 203.90, "ITAE": 89.73,
                 "tiempo_s": None, "pasos": None, "reward_medio": None},

        "exp4": {"politica": "PPO-Mask", "ambiente": "simulated", "ruta": "simple",
                 "ISE": 73.79, "IAE": 22.91, "ITSE": 200.16, "ITAE": 73.77,
                 "tiempo_s": None, "pasos": None, "reward_medio": None},

        #tabla7 ruta cuadrada
        "exp5": {"politica": "PPO", "ambiente": "simulated", "ruta": "square",
                 "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                 "tiempo_s": 27.89, "pasos": 270, "reward_medio": 7.12},

        "exp6": {"politica": "PPO", "ambiente": "real", "ruta": "square",
                 "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                 "tiempo_s": 112.48, "pasos": 594, "reward_medio": 3.75},

        "exp7": {"politica": "PPO-Mask", "ambiente": "simulated", "ruta": "square",
                 "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                 "tiempo_s": 24.42, "pasos": 235, "reward_medio": 7.94},

        "exp8": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "square",
                 "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                 "tiempo_s": 103.46, "pasos": 569, "reward_medio": 4.13},

        #tabla8 ruta triangular
        "exp9": {"politica": "PPO", "ambiente": "simulated", "ruta": "triangular",
                 "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                 "tiempo_s": 26.20, "pasos": 254, "reward_medio": 7.38},

        "exp10": {"politica": "PPO", "ambiente": "real", "ruta": "triangular",
                  "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                  "tiempo_s": 104.37, "pasos": 581, "reward_medio": 3.92},

        "exp11": {"politica": "PPO-Mask", "ambiente": "simulated", "ruta": "triangular",
                  "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                  "tiempo_s": 22.75, "pasos": 219, "reward_medio": 8.25},

        "exp12": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "triangular",
                  "ISE": None, "IAE": None, "ITSE": None, "ITAE": None,
                  "tiempo_s": 116.71, "pasos": 638, "reward_medio": 4.45},
    }

    return experimentos

#b) 1 generar_trayectoria_ideal(waypoints, puntos_por_segmento=100)
def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100): #entregada en el pdf tarea pag 4 
    #b) 1 crear listas vacias segun pdf
    x_ideal = []
    y_ideal = []

    #b) 2 iterar sobre pares
    for i in range(len(waypoints) - 1): #tomamos los waypoints, "len" nos da la cantidad, "range" genera una lista imaginaria de ese largo, que el "for" recorre, lo del "-1" 
        x, y = waypoints[i] #paso actual
        x1, y1 = waypoints[i+1] #paso siguiente

        #b) 3 usar np.linspace y .extend()
        xruta=np.linspace(x, x1, puntos_por_segmento) #los puntos determinados ya en el argumento de la funcion del pdf, basicamente le damos el punto x actual y el siguiente x1 para que los una con pasos intermedios
        yruta=np.linspace(y,y1,puntos_por_segmento) #los puntos determinados ya en el argumento de la funcion del pdf, basicamente le damos el punto y actual y el siguiente y1 para que los una con pasos intermedios
        
        #aplicamos el .extend()
        x_ideal.extend(xruta) #extend agreda elemento por elemento de una lista a otra, y ya
        y_ideal.extend(yruta) #extend agreda elemento por elemento de una lista a otra, y ya

        
    #b) 4 retorno NumPy: np.array(x_ideal) y np.array(y_ideal). convierte ambas lista a un arreglo de Numpy
    return np.array(x_ideal), np.array(y_ideal)

#c)
def simular_lidar(n_sectores=36, d_min=0.5, d_max=30.0): #distancias en mts, sectores adimencional


    #c) 1 Cree un arreglo de ángulos de 0 a 360◦ usando np.linspace
    angulos_deg=np.linspace(0,360, n_sectores) #no se especifica la cantidad en la que deben de estar divididos los angulos asuminos que son los numero de sectores


    #c) 2 Genere distancias aleatorias uniformes entre d_min y d_max
    distancias=np.random.uniform(d_min,d_max, n_sectores)

    #c) 3 Simulación de Obstáculo: Modifique los índices del [5:9] para que tengan distancias pequeñas (entre 0.5 y 2.0 m), simulando un objeto cercano al robot.
    distancias[5:9] = np.random.uniform(0.5, 2.0, 4) #indexamos y reemplezamos un grupo con valores aleatorios uniformes para emular obstaculo, rango segun pdf
    
    #c) 4 Normalización: Calcule un tercer arreglo distancias_norm aplicando la fórmula (entregada en pdf)
    distancias_norm=(distancias-d_min)/(d_max-d_min)
    
    #c) 5 Retorne: angulos_deg, distancias y distancias_norm.
    return angulos_deg,distancias,distancias_norm