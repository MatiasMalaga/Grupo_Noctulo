import numpy as np


#a) calcular_movimiento(x, y, theta, v, omega, dt=0.1) Calcula la nueva pose del robot.

def calcular_movimiento(x, y, theta, v, omega, dt=0.1):
    #Saturación: Antes de calcular, use np.clip para asegurar que v no supere los 0.8m/s y ω los 0.6 rad/s (Restricciones de la Tabla 1).
    v_limt = np.clip(v, 0, 0.8)
    omega_limt = np.clip(omega, -0.6, 0.6)


    #calculamos x_nuevo segun formula entregada en pdf: xnew = x + v · cos(θ)· dt
    x_nuevo= x+v_limt*np.cos(theta)*dt #aaaaaaaaaaaahhaaaaaaaaaaaaaaaaaah no me acordaba que esta mierda θ se llamaba theta, y yo haciendolo con omega_limt hahaajdnfiwjeviwefviewjo
    #repetimos proceso para y_nuevo con la misma formula
    y_nuevo= y+v_limt*np.sin(theta)*dt

    #θ˙=ω
    #dθ/dt = ω
    #dθ≈ω⋅dt
    #θnew​=θ+dθ pasa a θnew​-θ=dθ, remplazamos
    #θnew​-θ=ω⋅dt
    #odenamos
    #θnew=​θ+ω⋅dt
    theta_nuevo=theta+omega_limt*dt #odio hacer darme la ecuacion no hubiera estado de mas, grax ;)

    #creamos y guardamos la tupla
    tupla_pedida=(x_nuevo, y_nuevo, theta_nuevo)

    #Retorno: La tupla (x_nuevo, y_nuevo, theta_nuevo)
    return tupla_pedida




















































