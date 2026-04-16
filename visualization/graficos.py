import matplotlib.pyplot as plt
import os

#(a) plot_metricas(diccionario_experimentos, ambiente, ruta)
def plot_metricas(diccionario_experimentos, ambiente, ruta):
    #a) 1 Filtrado: Use .items() para recorrer el diccionario de experimentos y extraiga solo los datos que coincidan con el ambiente y ruta solicitados.
    valores_limpios=[] #creamos lista vacia para guardar los valores
    for valores in diccionario_experimentos.values(): #entramos a solo los valores del diccionario experimentos que creamos
        if valores["ambiente"]==ambiente and valores["ruta"]==ruta: #la condicion del filto pedida
            valores_limpios.append(valores) #guardamos los valores en la lista que creamos antes
    
    #creamos lo que seran dos diccionarios
    ppo=None 
    mask=None
    #a) 2 Gráficos: Cada subplot debe mostrar un gráfico de barras (plt.bar) comparando PPO vs PPO-Mask para una métrica (ISE, IAE, ITSE, ITAE).
    for valores in valores_limpios: #recorremos los valores limpios 
        if valores["politica"]=="PPO": #extraemos todos los valores para PPO
            ppo=valores #guardamos los valores
        elif valores["politica"]=="PPO-Mask": #extreamos todos los valores para PPO-Mask
            mask=valores #guardamos los valores

    #creamos una figura
    plt.figure(figsize=(10,6))
    plt.gcf().supylabel("valor del indice")
    
    #grafico para ISE
    plt.subplot(1,4,1) #ubicacion del en subplot
    plt.bar(["PPO", "Mask"], [ppo["ISE"], mask["ISE"]]) #grafica dos barras, donde los primeros con los nombres de cada barra y sus respectivos valores para cada una extraida de sus respectivos diccionarios
    plt.title("ISE") #titulo es la metrica sobre la que se compara
    

    #grafico para IAE
    plt.subplot(1,4,2) #ubicacion del en subplot
    plt.bar(["PPO", "Mask"], [ppo["IAE"], mask["IAE"]]) #grafica dos barras, donde los primeros con los nombres de cada barra y sus respectivos valores para cada una extraida de sus respectivos diccionarios
    plt.title("IAE") #titulo es la metrica sobre la que se compara

    #grafico para ITSE
    plt.subplot(1,4,3) #ubicacion del en subplot
    plt.bar(["PPO", "Mask"], [ppo["ITSE"], mask["ITSE"]]) #grafica dos barras, donde los primeros con los nombres de cada barra y sus respectivos valores para cada una extraida de sus respectivos diccionarios
    plt.title("ITSE") #titulo es la metrica sobre la que se compara

    #grafico para ITAE
    plt.subplot(1,4,4) #ubicacion del en subplot
    plt.bar(["PPO", "Mask"], [ppo["ITAE"], mask["ITAE"]]) #grafica dos barras, donde los primeros con los nombres de cada barra y sus respectivos valores para cada una extraida de sus respectivos diccionarios
    plt.title("ITAE") #titulo es la metrica sobre la que se compara

    plt.tight_layout() #mejora de visualizacion
    
    #a) 3 Automatización: Use la librería os para asegurar que la carpeta resultados_graficos/ exista antes de guardar la figura con un nombre descriptivo.
    os.makedirs("resultados_graficos", exist_ok=True) #evalua si la carpeta existe o no
    plt.savefig("resultados_graficos/metricas_grafico_PPO_vs_PPO-Mask.png") #guardamos la figura (graficos) en la carpeta "resultados_graficos" bajo el nombre de "metricas_grafico_PPO_vs_PPO-Mask" en formato .png
    plt.show()
    
#b) plot_lidar(angulos, distancias, distancias_norm) Visualice la percepción del robot para depurar posibles colisiones. Esta función, se utilizaen el código main.py, tiene como argumento de entrada los valores que entrega la función simular_lidar().


def plot_lidar(angulos, distancias, distancias_norm):
    
    plt.figure(figsize=(9,5))

    plt.subplot(1,2,1) #real
    plt.scatter(angulos, distancias)
    plt.xlabel("angulo de giro (0-360°)")
    plt.ylabel("distancia detectada (m)")
    plt.title("distancia de los objetos")

    plt.subplot(1,2,2) #IA
    plt.plot(angulos, distancias_norm,marker="*")
    plt.xlabel("sectores del sensor")
    plt.ylabel("valor (0.0 a1.0)")
    plt.title("datos nomalizados")
    

    plt.tight_layout()
    plt.show()
    
#c) plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre) Genere el mapa de navegación comparativo:
def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):
    plt.figure()
    
    #grafica para PPO
    plt.plot(x_ppo, y_ppo, label="Trayectoria PPO")
    
    #grafica para mask
    plt.plot(x_mask, y_mask, label="Trayectoria PPO-Mask")

    #extraccion rapida de datos
    x_w=[]
    y_w=[]
    for i in range(len(waypoints)): #tomamos los datos de los waypoints
        x, y = waypoints[i] 
        x_w.append(x), y_w.append(y)     #sip, la misma estructura que en "datos" me gusto :)
    
    #grafica waypoints
    plt.scatter(x_w,y_w, marker="s", color="black", label="Waypoints (Metas)")

    plt.axis("equal")
    plt.tight_layout()
    plt.show()





















