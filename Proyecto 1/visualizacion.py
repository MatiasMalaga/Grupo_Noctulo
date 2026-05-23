import matplotlib.pyplot as plt
import numpy as np


def graficar_recoleccion_vs_bateria(resultados: dict):
    """
    Genera un gráfico de barras agrupadas comparando basura recolectada
    vs batería consumida para cada robot.

    Parámetro:
        resultados: diccionario con formato
            {nombre: {'basura_total': float, 'consumo_bateria': float, 'eficiencia': float}}
    """
    # 1. Extraer nombres de robots (eje X)
    nombres = list(resultados.keys())

    # 2. Extraer listas paralelas de basura y batería
    basura_total = [resultados[n]['basura_total'] for n in nombres]
    consumo_bateria = [resultados[n]['consumo_bateria'] for n in nombres]

    # 3. Configurar posiciones y ancho de barras
    x = np.arange(len(nombres))
    ancho = 0.35

    # 4. Crear figura y ejes
    fig, ax = plt.subplots()

    # Barra de basura recolectada (verde) ligeramente a la izquierda
    barras_basura = ax.bar(x - ancho / 2, basura_total, ancho,
                           label='Basura Recolectada (kg)', color='green')

    # Barra de batería consumida (rojo) ligeramente a la derecha
    barras_bateria = ax.bar(x + ancho / 2, consumo_bateria, ancho,
                            label='Batería Consumida (%)', color='red')

    # 5. Estilo del gráfico
    ax.set_title('Rendimiento: Recolección vs Consumo Energético')
    ax.set_ylabel('Cantidad')
    ax.set_xticks(x)
    ax.set_xticklabels(nombres)
    ax.legend()

    # Cuadrícula horizontal para mejor lectura
    ax.grid(axis='y')

    plt.tight_layout()
    plt.show()