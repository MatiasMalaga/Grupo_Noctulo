import numpy as np


def comparar_rendimiento(datos: list) -> dict:
    """
    Analiza el historial de simulación y calcula métricas de eficiencia por robot.

    Parámetro:
        datos: lista de filas con formato [paso, nombre, x, y, bateria, basura_recolectada]

    Retorna:
        Diccionario con resultados por robot:
        {nombre: {'consumo_bateria': float, 'basura_total': float, 'eficiencia': float}}
    """
    # 1. Convertir la lista anidada a un array NumPy
    matriz = np.array(datos, dtype=object)

    # 2. Obtener nombres únicos de robots (columna índice 1)
    nombres_unicos = np.unique(matriz[:, 1])

    # 3. Diccionario para almacenar resultados
    resultados = {}

    # 4. Procesar cada robot
    for nombre in nombres_unicos:
        # Máscara booleana para filtrar filas de este robot
        mascara = matriz[:, 1] == nombre
        filas_robot = matriz[mascara]

        # Extraer columnas de batería (índice 4) y basura (índice 5) como float
        col_bateria = filas_robot[:, 4].astype(float)
        col_basura = filas_robot[:, 5].astype(float)

        # Consumo de batería: 100% inicial menos el último valor registrado
        consumo_bateria = 100.0 - col_bateria[-1]

        # Basura total: último valor acumulado
        basura_total = col_basura[-1]

        # Eficiencia: basura por unidad de batería consumida
        if consumo_bateria == 0:
            eficiencia = 0.0
        else:
            eficiencia = basura_total / consumo_bateria

        # Guardar en el diccionario
        resultados[nombre] = {
            'consumo_bateria': float(consumo_bateria),
            'basura_total': float(basura_total),
            'eficiencia': float(eficiencia)
        }

    return resultados
