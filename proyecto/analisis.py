import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod





def comparar_remdimiento(historial_datos):
    
    # 1) Convertir la lista anidada recibida a una matriz bidimensional (Array) de NumPy.
    matriz=np.array(historial_datos) # convierte la matriz de datos del historial en una arreglo numpy
    
    # 2) Obtener la lista de nombres únicos (investigue sobre el uso de np.unique) de los robots, ubicados en la columna 1 (índice 1)
    nombres=matriz[:,1] # con esto sacamos toda la columna 1 con todos los nombres 
    nombres_f=np.unique(nombres) #esto elimina los nombres repetidos, y los guarda en "nombres_f"

    
    # 3) Crear un diccionario vacío para los resultados.
    dicionario={}
    
    # 4)  Para cada nombre único, ni a palo copio todo ese parrafo aqui, lo leen en el pdf ni modo

    filas_robot=[] #inicializa una lista para guardar los datos de los robots
    
    # a) Usar operaciones booleanas de NumPy (máscaras/filtros) para aislar las filas que correspondan solo a ese robot.
    for robot in nombres_f: #sacamos uno por uno los nombre de los robots de la lista "nombre_f"
        
        filtro=matriz[:,1] == robot # esto es un filtro booleana para filtrar las filas del robot actual
        filas_robot.append(matriz[filtro]) # aplicamos el filtro a la matriz y las filas que cumplen se guardan en la lista "filas_robot" como matriz

    
    for i in range(len(filas_robot)): # esto, es solo un for, que avanza tanto como matrices de robots haya

        # b) Extraer la columna de la batería (índice 4) y la de basura (índice 5), convirtiéndolas a tipo flotante (astype(float)).
        baterias_r=(filas_robot[i][:,4]).astype(float) #esto accede al a la matriz de datos del robot "x" y extrae su historial de baterias. y tambien convierte esos valores a float, por que? ni idea, pero lo piden.
        basuras_r=(filas_robot[i][:,5]).astype(float) # es... lo mismo, pero sacando lo de la basura XD

        # c) Consumo de Batería: Calcular la diferencia entre una batería inicial teórica (100,0) y el último valor registrado de la batería de ese robot en el historial.
        bateria_diferencia=100.0-baterias_r[-1] #nada magico es, una resta de 100.0 - lo que le quede de bateria (que es el ultimo valor, por eso el -1), y si el 100.0 en flotante, que por que? porque me dio la gana XD
        
        # d) Basura Total: Como la basura se va acumulando de forma incremental en el código, simplemente tomar el último elemento de la columna de basura.
        r_basura_total=basuras_r[-1] # bueno... lo que dice el enunciado
        
        # e) Eficiencia: Calcular el cociente entre la Basura Total y el Consumo de Batería. Si el consumo de batería fue 0, evitar la división por cero asignando la eficiencia como 0,0.
        if bateria_diferencia>0: # comprobamos que no sea 0 ni negativo, un 2*1 vamos, yupi...
            eficiencia=r_basura_total/bateria_diferencia #si no es 0 o menor calcula eso
        else:
            eficiencia=0.0 # y si no... pues 0.0 por que flotante? ni idea todo aqui es flotante... quien sabe
        
        # f) Almacenar estos tres cálculos en el diccionario resultante bajo la llave del nombredel robot. El formato debe ser un sub-diccionario: {’consumo_bateria’: float,’basura_total’: float, ’eficiencia’: float}.
        
        dicionario[filas_robot[i][0,1]] = { #bueno, esto es lo que tiene mas chicha, agarra todo los resultados esos de antes y les pone una llave
        "consumo_bateria": bateria_diferencia, #la llave bateria
        "basura_total": r_basura_total, # la llave basura total
        "eficiencia": eficiencia # la llave eficiencia
        } #y todo bajo el nombre del robot que toca, extrayendolo de la columna donde esta el nombre en cada matriz de robot por que... no se ocurrio otra forma de estar seguro de que es ese robot
    
    # 5)  Retornar el diccionario con los resultados de todos los robots.
    return dicionario

























