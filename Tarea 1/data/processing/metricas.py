import numpy as np



#a) calcular_IAE, calcular_ISE, calcular_ITAE, calcular_ITSE Cada función recibe el arreglo de errores y el escalar dt. Deben retornar un float. Para las métricas con tiempo (IT), 
#generen el arreglo de tiempo usando np.arange(len(errores)

#tiempo = np.arange(len(errores))*dt #tiempo segun pdf

#IAE
def calcular_IAE(errores, dt):
    return np.float(np.sum(np.abs(errores))*dt) #ecuacion del pdf traducida a codigo

#ISE
def calcular_ISE(errores, dt):
    return np.float(np.sum(errores**2)*dt) #ecuacion del pdf a codigo

#ITAE ITAE=∫(t* ∣e(t)∣)*dt (integral de 0 a t) segun lo visto es lo mismo pero se multiplica por t los valores del error aboluto antes de la sumatoria
def calcular_ITAE(errores,dt):
    #tiempo segun pdf
    tiempo = np.arange(len(errores))*dt
    return  np.float(np.sum(tiempo * np.abs(errores))*dt)

#ITSE ITSE=∫ t*(e(t))^2 *dt (integral de 0 a t) segun lo visto es lo mismo pero se multiplica por t los valores del error al cuadrado antes de la sumatoria
def calcular_ITSE(errores,dt):
    #tiempo segun pdf
    tiempo = np.arange(len(errores))*dt #por si solo llaman a esta funcion duplico la del tiempo
    return np.float(tiempo * np.sum(errores**2)*dt)

#b) calcular_todas_las_metricas(errores, dt) Función agrupadora que llama a las 4 anteriores y retorna un diccionario con las llaves:”ISE”, ”IAE”, ”ITSE”, ”ITAE”. Use la función round(valor, 2) para entregar resultados limpios.
def calcular_todas_las_metricas(errores, dt):
    
    #creamos un diccionario para guardar los resultados
    resultados_errores={}

    #llamamos a las funciones anteriores y le damos los argumentos correspondientes y guardamos los resultados en una variable 
    ise=calcular_ISE(errores,dt)
    iae=calcular_IAE(errores,dt)
    itse=calcular_ITSE(errores,dt)
    itae=calcular_ITAE(errores,dt)
    
    #b) Use la función round(valor, 2) para entregar resultados limpios.
    #usa la función round para limitar los resultados a 2 decimales.
    
    #aplicamos el round(valor, 2)
    ise_r=round(ise, 2)
    iae_r=round(iae, 2)
    itse_r=round(itse, 2)
    itae_r=round(itae, 2)

    #guardamos los valores en el diccionario
    resultados_errores["ISE"]  = ise_r
    resultados_errores["IAE"]  = iae_r
    resultados_errores["ITSE"] = itse_r
    resultados_errores["ITAE"] = itae_r

    #retornamos el diccionario
    return resultados_errores

#c) calcular_mejora(valor_ppo, valor_mask)
#Calcula la reducción porcentual del error: (Vbase−Vnuevo)/Vbase× *100. Esta función permite verificar si el PPO-Mask realmente mejora al PPO estándar como dice el paper (16.6 % en ISE).

def calcular_mejora(valor_ppo, valor_mask):
    return ((valor_ppo - valor_mask)/valor_ppo)*100
